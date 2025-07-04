# GoldWave App Module
# An add-on for NVDA
# Copyright 2013-2025 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import api
import scriptHandler
import controlTypes
from NVDAObjects.IAccessible import IAccessible

# Various buttons and numeric edit fields.
from NVDAObjects.window import Window, DisplayModelEditableText, edit
from NVDAObjects import NVDAObject
from logHandler import log
import ui
import addonHandler

addonHandler.initTranslation()

# Detect multiple instances of GoldWave.
multiInstance = 0


class SoundWindow(IAccessible):
	"""The GoldWave's sound window. Here one can play, record and edit audio files."""

	scriptCategory = "GoldWave"

	# GoldWave 6.57 raises name change event whenever play/rewind/stop keys are pressed.
	event_nameChange = None

	def _get_helpText(self) -> str:
		# Translators: general help message for GoldWave sound window.
		return _(
			"This is GoldWave's sound window. "
			"You can use GoldWave commands to listen to and edit sound files. "
			"See GoldWave help for details."
		)

	# A master function to obtain needed info from status bars.
	# #17.05: because this is prone to failure, insert debug messages if asked.
	def getStatusInfo(self, statBarIndex: int, childIndex: int) -> str:
		log.debug("GWV: Status bar object fetcher")
		log.debug(f"GWV: Status {statBarIndex}, child index {childIndex}")
		fgChild = self.appModule._get_statusBars(statBarIndex)
		log.debug(
			"GWV: Status bar found" if fgChild.role == controlTypes.Role.STATUSBAR else "Status bar not found"
		)
		if not fgChild.displayText:
			fgChild.redraw()
		try:
			info = fgChild.getChild(childIndex).displayText
		except IndexError:
			log.debug("GWV: Object cannot be located")
			return ""
		return info

	# An alternative function to obtain needed info from status bars.
	# Unlike the method above, this function will parse status bar display text (applies to GoldWave 7).
	def getStatusInfoDisplayText(self, statBarIndex: int) -> str:
		log.debug("GWV: Status bar display text fetcher")
		log.debug(f"GWV: Status {statBarIndex}")
		fgChild = self.appModule._get_statusBars(statBarIndex)
		log.debug(
			"GWV: Status bar found" if fgChild.role == controlTypes.Role.STATUSBAR else "Status bar not found"
		)
		if not fgChild.displayText:
			fgChild.redraw()
		try:
			return fgChild.displayText
		except IndexError:
			log.debug("GWV: Object cannot be located")
			return ""

	# Get audio positions.
	def getAudioPos(self, raw: bool = False) -> str:
		# Above the status bar is the audio position and selection info bar. See if this control can be fetched.
		global multiInstance
		# Have to definitely call the info getter twice.
		# Status bar position has changed in GoldWave 7 (last item across releases).
		audioPos = self.getStatusInfo(0, -1)
		if multiInstance > 1:
			audioPos = self.getStatusInfo(0, -1)
		# Raw means return just the raw text, used in remaining time and other position scripts.
		if raw:
			return audioPos
		# Translators: Presented when audio track position information can not be located.
		return _("Track position not available") if not audioPos or " " in audioPos else audioPos

	def getAudioSelection(self) -> str:
		# Call the info getter twice to obtain audio selection (relies on display text).
		global multiInstance
		audioSelection = self.getStatusInfo(0, 2)
		if multiInstance > 1:
			audioSelection = self.getStatusInfo(0, 2)
		# In GoldWave 7, audio selection text is split over two or more elements with missing text.
		# Therefore, join the partial string with the next item display text and fil in the missing text.
		if self.appModule.productVersion >= "7":
			audioSelectionDisplayText = self.getStatusInfoDisplayText(0)
			displayTextStart = audioSelectionDisplayText.find(audioSelection)
			audioSelection2 = self.getStatusInfo(0, 3)
			displayTextEnd = audioSelectionDisplayText.rfind(audioSelection2[-1])
			audioSelectionDisplayText= audioSelectionDisplayText[displayTextStart:displayTextEnd+1]
			# Then remove extraneous text in the beginning.
			audioSelection = audioSelectionDisplayText.partition(" ")[-1]
		log.debug(f"GWV: status bar length: {len(audioSelection)}")
		return audioSelection

	def getAudioSelectionParsed(self) -> list[str]:
		# Get marker positions and selection duration.
		# Return the list of substrings to be handled by individual scripts.
		audioSelectionParsed = self.getAudioSelection().split()
		log.debug(f"GWV: parsed status bar length: {len(audioSelectionParsed)}")
		return audioSelectionParsed

	# Get channel information. But first, a few constants (to help translators):
	audioChannelValues = {
		# Translators: One of the channel values when editing audio track in Goldwave.
		"": _("Channel information unavailable"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Mono": _("mono"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Stereo": _("stereo"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Left": _("left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Right": _("right"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Center": _("center"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"w frequenc": _("low frequency"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Back left": _("back left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Back right": _("back right"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Side left": _("side left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Side right": _("side right"),
		# Translators: Presented when multiple channels are selected (GoldWave 6 and higher).
		"Multiple": _("Multiple channels selected"),
		# Translators: Presented when all channels (3.1, 5.1, 7.1) are selected (GoldWave 6 and higher).
		"All": _("All channels selected"),
	}

	def getAudioChannels(self) -> str:
		# Based on the constants above and the return value below, get channel information.
		audioChannels = self.getStatusInfo(0, 0)
		if audioChannels not in self.audioChannelValues:
			audioChannels = self.getStatusInfo(0, 0)
		return audioChannels

	def getTrackLength(self, raw: bool = False) -> str:
		fgChild = self.appModule._get_statusBars(0)
		try:
			if not fgChild.displayText:
				fgChild.redraw()
		except AttributeError:
			fgChild = self.appModule._get_statusBars(0)
		# In recent GoldWave releases, raw display text must be parsed
		# as display text for individual components are incomplete.
		if raw:
			statusBarComponents = fgChild.displayText.split()
			return statusBarComponents[1]
		else:
			return fgChild.getChild(1).displayText

	# Convert time to seconds: Convert hh:mm:ss to seconds.
	# Needed in various functions.
	def convertTime2Sec(self, times: list[list[str]]) -> list[float]:
		timeList = []
		for time in times:
			if len(time) == 1:
				timeList.append(float(time[0]))
			elif len(time) == 2:
				min = float(time[0]) * 60.0
				timeList.append(min + float(time[1]))
			else:
				hour, min = float(time[0]) * 3600.0, float(time[1]) * 60.0
				timeList.append(hour + min + float(time[2]))
		return timeList

	def getRemainingTime(self, audioPos: str) -> str:
		trackLengthParsed = self.getTrackLength().split(":")
		audioPosParsed = audioPos.split(":")
		# An obvious solution is to use recursive subtraction.
		# That is, subtract the last elements,
		# and if audio pos is greater than track length for that particular cell, move to the left.
		# However, a simpler solution is to convert the time value to seconds,
		# subtract then format it back to hh:mm:ss format.
		timesec = self.convertTime2Sec([audioPosParsed, trackLengthParsed])
		remainingTimeSec = timesec[1] - timesec[0]
		# Now convert the seconds back to hh:mm:ss format.
		if remainingTimeSec < 60.0:
			return str(remainingTimeSec)
		elif 60.0 <= remainingTimeSec < 3600.0:
			remainingTime = divmod(remainingTimeSec, 60.0)
			mm = int(remainingTime[0])
			sec, ms = str(remainingTime[1]).split(".")
			ss = int(sec)
			return f"{mm:02d}:{ss:02d}.{ms}"
		else:
			remainingTime = divmod(remainingTimeSec, 3600.0)
			hh = int(remainingTime[0])
			remainingTime = divmod(remainingTime[1], 60.0)
			mm = int(remainingTime[0])
			ss, ms = str(remainingTime[1]).split(".")
			return f"{hh:02d}:{mm:02d}:{ss:02d}.{ms}"

	def getZoomLevel(self) -> str:
		try:
			zoomLevel = self.getStatusInfo(1, 1)
		except IndexError:
			zoomLevel = self.getStatusInfo(1, 1)
		print(zoomLevel)
		# In GoldWave 7, zoom text element does not expose name correctly.
		# Therefore, parse the second status bar display text.
		if self.appModule.productVersion >= "7":
			zoomDisplayText = self.getStatusInfoDisplayText(1)
			# Zoom text is second element if the element text is present.
			if zoomLevel in zoomDisplayText:
				zoomLevel = zoomDisplayText.split()[1]
		return zoomLevel

	# Audio editing scripts:

	@scriptHandler.script(gesture="KB:[")
	def script_dropStartMarker(self, gesture):
		try:
			gesture.send()
			# Translators: The start marker position for selecting parts of the audio track
			# (example output: "Start: 0.00").
			ui.message(
				_("Start: {startMarkerPos}").format(startMarkerPos=self.getAudioSelectionParsed()[0])
			)
		except Exception:
			pass

	@scriptHandler.script(gesture="KB:]")
	def script_dropFinishMarker(self, gesture):
		try:
			gesture.send()
			# Translators: The finish marker position for selecting parts of the audio track
			# (example output: "Finish: 5.00").
			ui.message(
				_("Finish: {finishMarkerPos}").format(finishMarkerPos=self.getAudioSelectionParsed()[2])
			)
		except Exception:
			pass

	@scriptHandler.script(gesture="kB:control+[")
	def script_playSelection(self, gesture):
		gesture.send()
		# Translators: Presented when selected audio is playing.
		ui.message(_("Play selection"))

	@scriptHandler.script(gesture="KB:control+a")
	def script_selectAll(self, gesture):
		gesture.send()
		# Translators: Presented when all parts of the audio track is selected.
		ui.message(_("Select All"))

	@scriptHandler.script(gesture="kb:control+q")
	def script_dropCue(self, gesture):
		gesture.send()
		# Translators: A message in GoldWave when an audio cue is dropped at the current audio position.
		ui.message(_("Cue"))

	@scriptHandler.script(gesture="KB:q")
	def script_dropCueAtStartMarker(self, gesture):
		gesture.send()
		# Translators: Presented when audio cue is dropped at the start marker position.
		ui.message(_("Cue dropped at start marker"))

	@scriptHandler.script(gesture="KB:shift+q")
	def script_dropCueAtFinishMarker(self, gesture):
		gesture.send()
		# Translators: Presented when an audio cue is dropped at the finish marker position.
		ui.message(_("Cue dropped at finish marker"))

	@scriptHandler.script(gesture="kb:control+j")
	def script_moveStartMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		ui.message(_("Start marker at next cue"))

	@scriptHandler.script(gesture="kb:control+shift+j")
	def script_moveStartMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		ui.message(_("Start marker at previous cue"))

	@scriptHandler.script(gesture="kb:alt+j")
	def script_moveFinishMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the finish marker is moved to the next cue position.
		ui.message(_("Finish marker at next cue"))

	@scriptHandler.script(gesture="kb:alt+shift+j")
	def script_moveFinishMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		ui.message(_("Finish marker at previous cue"))

	# Handle both delete and trim.
	@scriptHandler.script(gestures=["kb:delete", "kb:control+t"])
	def script_deleteSelection(self, gesture):
		gesture.send()
		# Translators: Presented when audio selection is deleted.
		ui.message(_("deleted"))

	# Playback and recording:

	@scriptHandler.script(gestures=["KB:f2", "KB:f3", "kb:f4"])
	def script_play(self, gesture):
		gesture.send()
		# Translators: Presented when a track is playing in Goldwave.
		ui.message(_("play"))

	@scriptHandler.script(gesture="kb:f5")
	def script_rewind(self, gesture):
		gesture.send()
		# Translators: Presented when a track is rewinding in Goldwave.
		ui.message(_("rewind"))

	@scriptHandler.script(gesture="kb:f6")
	def script_forward(self, gesture):
		gesture.send()
		# Translators: Presented when fast forwarding a track in Goldwave.
		ui.message(_("fast forward"))

	@scriptHandler.script(gestures=["kb:f7", "kb:control+f7"])
	def script_pause(self, gesture):
		gesture.send()
		# Translators: Presented when pausing a track in Goldwave.
		ui.message(_("pause"))

	@scriptHandler.script(gestures=["kb:f8", "kb:control+f8"])
	def script_stop(self, gesture):
		gesture.send()
		# Translators: Presented when stopping a track in in Goldwave.
		ui.message(_("stop"))

	@scriptHandler.script(gesture="kb:control+f9")
	def script_startRecord(self, gesture):
		gesture.send()
		# Translators: Presented when starting recording in Goldwave.
		ui.message(_("record"))

	# Audio position scripts: markers, selection duration.

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces the current audio position in seconds."),
		gesture="kb:control+shift+p",
		speakOnDemand=True,
	)
	def script_announceAudioPosition(self, gesture):
		# Shouldn't say anything unless in audio editing view.
		ui.message(self.getAudioPos())

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces a summary on audio selection info such as selection duration."),
		gesture="kb:control+nvda+3",
		speakOnDemand=True,
	)
	def script_announceAudioSelection(self, gesture):
		try:
			# Parse this string to get individual info such as marker positions.
			audioSelectionParsed = self.getAudioSelectionParsed()
			if not audioSelectionParsed:
				# Translators: Presented when there is no audio selection summary available.
				ui.message(
					_("Unable to obtain audio selection summary. Please close and reopen the audio track.")
				)
			else:
				ui.message(
					# Translators: The audio selection summary message (example output: "0.00 to 1.00 (1.00)").
					_("{audioSelectionStart} to {audioSelectionEnd} {audioSelectionLength}").format(
						audioSelectionStart=audioSelectionParsed[0],
						audioSelectionEnd=audioSelectionParsed[2],
						audioSelectionLength=audioSelectionParsed[3],
					)
				)
		except Exception:
			pass

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces total length of the audio track."),
		gesture="kb:control+nvda+2",
		speakOnDemand=True,
	)
	def script_announceTrackLength(self, gesture):
		trackLengthSTR = self.getTrackLength(raw=self.appModule.productVersion >= "7")
		if not trackLengthSTR:
			# Translators: Presented when there is no track length information.
			ui.message(_("Track length is unavailable. Please close and reopen the audio track."))
		else:
			ui.message(_("Track length: {trackLength}").format(trackLength=trackLengthSTR))

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces remaining length of the audio track."),
		gesture="kb:NVDA+shift+r",
		speakOnDemand=True,
	)
	def script_announceRemainingTime(self, gesture):
		audioPos = self.getAudioPos(raw=True)
		if not audioPos or " " in audioPos or not self.getTrackLength():
			# Translators: An error message presented when remaining time cannot be anounced.
			ui.message(_("Cannot tell you remaining time for the current track"))
		else:
			if ":" in audioPos:
				ui.message(self.getRemainingTime(audioPos))
			elif float(audioPos) == 0.0:
				ui.message(self.getTrackLength(raw=self.appModule.productVersion >= "7"))
			else:
				ui.message(self.getRemainingTime(audioPos))

	# Audio channels and zoom level.

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces the audio channel you are editing."),
		gesture="kb:control+nvda+1",
		speakOnDemand=True,
	)
	def script_announceAudioChannels(self, gesture):
		channelSTR = self.getAudioChannels()
		if channelSTR in ["Multiple", "All"]:
			# Translators: Presented when all or multiple channels (in 3.1, 5.1 or 7.1 channels) are selected
			# (GoldWave 6 and higher).
			ui.message(self.audioChannelValues[channelSTR])
		else:
			ui.message(
				# Translators: Presented to indicate the selected channel for the track
				# (example output: "Selected channel: mono").
				_("Selected channel: {audioChannel}").format(audioChannel=self.audioChannelValues[channelSTR])
			)

	# Change and announce audio channels.
	@scriptHandler.script(gestures=["kb:control+shift+l", "kb:control+shift+r", "kb:control+shift+a"])
	def script_selectChannel(self, gesture):
		gesture.send()
		self.script_announceAudioChannels(gesture)

	@scriptHandler.script(
		# Translators: Input help mode message for a Goldwave command.
		description=_("Announces audio zoom level."),
		gesture="kb:control+nvda+4",
		speakOnDemand=True,
	)
	def script_announceZoomLevel(self, gesture):
		# Translators: Presented to indicate audio selection zoom level (example output: "Zoom level: 10.000").
		ui.message(_("Zoom level: {zoomLevel}").format(zoomLevel=self.getZoomLevel()))

	# Change and announce zoom levels.
	# All of them involve pressing the shift key, so just use a creative list comprehension.
	@scriptHandler.script(
		gestures=[
			f"kb:shift+{command}"
			for command in ["upArrow", "downArrow", "0", "1", "2", "3", "4", "5", "6", "a"]
		]
	)
	def script_changeZoomLevel(self, gesture):
		gesture.send()
		self.script_announceZoomLevel(gesture)


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		global multiInstance
		multiInstance += 1

	# Presets and control windows: Work with buttons with custom window class names.

	def event_NVDAObject_init(self, obj: NVDAObject):
		# Provide standardized control roles for the following objects.
		if isinstance(obj, Window):
			# For working with buttons such as presets window and control window.
			if obj.windowClassName in ("TBitton", "TImageButton"):
				obj.role = controlTypes.Role.BUTTON
			# For windows which NVDA should recognize as dialogs.
			elif (
				"Form" in obj.windowClassName
				and "MainForm" not in obj.windowClassName
				or obj.windowClassName == "TEffectWrapper"
			):
				# In GoldWave 6, the sound window has the window class name of "tSoundForm"
				# and should not be recognized as a dialog.
				if obj.windowClassName != "TSoundForm":
					obj.role = controlTypes.Role.DIALOG

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		# Custom NVDA overlay objects for sound window and edit fields:
		if obj.windowClassName == "TSoundForm":
			clsList.insert(0, SoundWindow)
		elif obj.windowClassName in ("TNumEdit", "TTimeEdit"):
			try:
				clsList.remove(DisplayModelEditableText)
				clsList.insert(0, edit.Edit)
			except ValueError:
				pass

	# Cache the needed status bar objects.
	statusBarCache: dict[int, NVDAObject] = {}

	def _get_statusBars(self, statBarIndex: int, refill: bool = False) -> NVDAObject:
		global multiInstance
		# In case multiple instances of GoldWave are running, flush the status bar cache.
		index = 0
		if refill or multiInstance > 1 or not len(self.statusBarCache):
			for child in api.getForegroundObject().children:
				if child.role == controlTypes.Role.STATUSBAR:
					if not child.displayText:
						child.redraw()
					self.statusBarCache[index] = child
					index += 1
		return self.statusBarCache[statBarIndex]
