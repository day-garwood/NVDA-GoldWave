# GoldWave App Module
# An add-on for NVDA
# Copyright 2013-2026 Joseph Lee and contributors, released under GPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import api
import scriptHandler
import controlTypes
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.window import Window, DisplayModelEditableText, edit
from NVDAObjects import NVDAObject
from logHandler import log
import ui
import addonHandler
import time

addonHandler.initTranslation()

# Detect multiple instances of GoldWave.
multiInstance = 0


class SoundWindow(IAccessible):
	"""The GoldWave's sound window. Here one can play, record and edit audio files."""

	scriptCategory = "GoldWave"

	# GoldWave 6.57 raises name change event whenever play/rewind/stop keys are pressed.
	event_nameChange = None

	# Track playback state for spacebar toggle
	_isPlaying = False

	def _get_helpText(self) -> str:
		# Translators: general help message for GoldWave sound window.
		return _(
			"This is GoldWave's sound window. "
			"You can use GoldWave commands to listen to and edit sound files. "
			"See GoldWave help for details."
		)

	# A master function to obtain needed info from status bars.
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
		global multiInstance
		audioPos = self.getStatusInfo(0, -2)
		if multiInstance > 1:
			audioPos = self.getStatusInfo(0, -2)
		if raw:
			return audioPos
		# Translators: Presented when audio track position information can not be located.
		return _("Track position not available") if not audioPos or " " in audioPos else audioPos

	def getAudioSelection(self) -> str:
		global multiInstance
		audioSelection = self.getStatusInfo(0, 2)
		if multiInstance > 1:
			audioSelection = self.getStatusInfo(0, 2)
		log.debug(f"GWV: status bar length: {len(audioSelection)}")
		return audioSelection

	def getAudioSelectionParsed(self) -> list[str]:
		audioSelectionParsed = self.getAudioSelection().split()
		log.debug(f"GWV: parsed status bar length: {len(audioSelectionParsed)}")
		return audioSelectionParsed

	# Get channel information.
	audioChannelValues = {
		"": _("Channel information unavailable"),
		"Mono": _("mono"),
		"Stereo": _("stereo"),
		"Left": _("left"),
		"Right": _("right"),
		"Center": _("center"),
		"Low frequency": _("low frequency"),
		"Back left": _("back left"),
		"Back right": _("back right"),
		"Side left": _("side left"),
		"Side right": _("side right"),
		"Multiple": _("Multiple channels selected"),
		"All": _("All channels selected"),
	}

	def getAudioChannels(self) -> str:
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
		if raw:
			statusBarComponents = fgChild.displayText.split()
			return statusBarComponents[1] if len(statusBarComponents) > 1 else ""
		else:
			try:
				return fgChild.getChild(1).displayText
			except:
				return ""

	def isTrackLoaded(self) -> bool:
		"""Check if a track is loaded"""
		try:
			trackLength = self.getTrackLength(raw=True)
			return bool(trackLength and trackLength != "0.000")
		except:
			return False

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
		timesec = self.convertTime2Sec([audioPosParsed, trackLengthParsed])
		remainingTimeSec = timesec[1] - timesec[0]
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
		if self.appModule.productVersion >= "7":
			zoomDisplayText = self.getStatusInfoDisplayText(1)
			if zoomLevel in zoomDisplayText:
				zoomLevel = zoomDisplayText.split()[1]
		return zoomLevel

	# Audio editing scripts:

	@scriptHandler.script(gesture="KB:[")
	def script_dropStartMarker(self, gesture):
		gesture.send()
		time.sleep(0.1)
		try:
			ui.message(
				_("Start marker: {startMarkerPos}").format(startMarkerPos=self.getAudioSelectionParsed()[0])
			)
		except Exception:
			pass

	@scriptHandler.script(gesture="KB:]")
	def script_dropFinishMarker(self, gesture):
		gesture.send()
		time.sleep(0.1)
		try:
			ui.message(
				_("Finish marker: {finishMarkerPos}").format(finishMarkerPos=self.getAudioSelectionParsed()[2])
			)
		except Exception:
			pass

	@scriptHandler.script(gesture="kB:control+[")
	def script_playSelection(self, gesture):
		gesture.send()
		ui.message(_("Play selection"))

	@scriptHandler.script(gesture="KB:control+a")
	def script_selectAll(self, gesture):
		gesture.send()
		ui.message(_("Select all"))

	@scriptHandler.script(gesture="kb:control+q")
	def script_dropCue(self, gesture):
		gesture.send()
		ui.message(_("Cue"))

	@scriptHandler.script(gesture="KB:q")
	def script_dropCueAtStartMarker(self, gesture):
		gesture.send()
		ui.message(_("Cue dropped at start marker"))

	@scriptHandler.script(gesture="KB:shift+q")
	def script_dropCueAtFinishMarker(self, gesture):
		gesture.send()
		ui.message(_("Cue dropped at finish marker"))

	@scriptHandler.script(gesture="kb:control+j")
	def script_moveStartMarkerToNextCuePos(self, gesture):
		gesture.send()
		ui.message(_("Start marker at next cue"))

	@scriptHandler.script(gesture="kb:control+shift+j")
	def script_moveStartMarkerToPrevCuePos(self, gesture):
		gesture.send()
		ui.message(_("Start marker at previous cue"))

	@scriptHandler.script(gesture="kb:alt+j")
	def script_moveFinishMarkerToNextCuePos(self, gesture):
		gesture.send()
		ui.message(_("Finish marker at next cue"))

	@scriptHandler.script(gesture="kb:alt+shift+j")
	def script_moveFinishMarkerToPrevCuePos(self, gesture):
		gesture.send()
		ui.message(_("Finish marker at previous cue"))

	@scriptHandler.script(gestures=["kb:delete", "kb:control+t"])
	def script_deleteSelection(self, gesture):
		gesture.send()
		ui.message(_("Deleted"))

	# Copy, Cut, Paste, Undo, Redo operations

	@scriptHandler.script(gesture="KB:control+c")
	def script_copy(self, gesture):
		gesture.send()
		ui.message(_("Copied"))

	@scriptHandler.script(gesture="KB:control+x")
	def script_cut(self, gesture):
		gesture.send()
		ui.message(_("Cut"))

	@scriptHandler.script(gesture="KB:control+v")
	def script_paste(self, gesture):
		gesture.send()
		ui.message(_("Pasted"))

	@scriptHandler.script(gesture="KB:control+b")
	def script_pasteAtBeginning(self, gesture):
		gesture.send()
		ui.message(_("Pasted at beginning"))

	@scriptHandler.script(gesture="KB:control+e")
	def script_pasteAtEnd(self, gesture):
		gesture.send()
		ui.message(_("Pasted at end"))

	@scriptHandler.script(gesture="KB:control+f")
	def script_pasteAtFinishMarker(self, gesture):
		gesture.send()
		ui.message(_("Pasted at finish marker"))

	@scriptHandler.script(gesture="KB:control+z")
	def script_undo(self, gesture):
		gesture.send()
		ui.message(_("Undo"))

	@scriptHandler.script(gesture="KB:control+y")
	def script_redo(self, gesture):
		gesture.send()
		ui.message(_("Redo"))

	# Playback and recording:

	@scriptHandler.script(gestures=["KB:f2", "KB:f3", "kb:f4"])
	def script_play(self, gesture):
		gesture.send()
		self._isPlaying = True
		ui.message(_("Play"))

	@scriptHandler.script(gesture="kb:f5")
	def script_rewind(self, gesture):
		gesture.send()
		ui.message(_("Rewind"))

	@scriptHandler.script(gesture="kb:f6")
	def script_forward(self, gesture):
		gesture.send()
		ui.message(_("Fast forward"))

	@scriptHandler.script(gestures=["kb:f7", "kb:control+f7"])
	def script_pause(self, gesture):
		gesture.send()
		ui.message(_("Pause"))

	@scriptHandler.script(gestures=["kb:f8", "kb:control+f8"])
	def script_stop(self, gesture):
		gesture.send()
		self._isPlaying = False
		ui.message(_("Stop"))

	@scriptHandler.script(gesture="kb:control+f9")
	def script_startRecord(self, gesture):
		gesture.send()
		ui.message(_("Record"))

	@scriptHandler.script(gesture="KB:space")
	def script_togglePlayStop(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
			return
		gesture.send()
		self._isPlaying = not self._isPlaying
		if self._isPlaying:
			ui.message(_("Play"))
		else:
			ui.message(_("Pause"))

	@scriptHandler.script(gesture="KB:control+home")
	def script_goToBeginning(self, gesture):
		gesture.send()
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
		else:
			ui.message(_("Beginning: 0.000 seconds"))

	# NEW: Alt+Shift gesture scripts for status bar information

	@scriptHandler.script(
		description=_("Announces the current file title."),
		gesture="kb:alt+shift+o",
		speakOnDemand=True,
	)
	def script_announceFileTitle(self, gesture):
		try:
			fg = api.getForegroundObject()
			windowTitle = fg.name
			if " - " in windowTitle:
				filename = windowTitle.split(" - ")[0]
			else:
				filename = windowTitle.split(".")[0] if "." in windowTitle else windowTitle
			ui.message(_("File: {filename}").format(filename=filename))
		except Exception:
			ui.message(_("Filename unavailable"))

	@scriptHandler.script(
		description=_("Announces the file type and audio properties."),
		gesture="kb:alt+shift+i",
		speakOnDemand=True,
	)
	def script_announceFileType(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
			return
		try:
			fg = api.getForegroundObject()
			windowTitle = fg.name

			if " - " in windowTitle and " Hz" in windowTitle:
				properties = windowTitle.split(" - ", 1)[-1]
				ui.message(properties)
			elif "." in windowTitle:
				extension = windowTitle.split(".")[-1].split()[0]
				ui.message(_("File type: {fileType}").format(fileType=extension.upper()))
			else:
				ui.message(_("File type unavailable"))
		except Exception:
			ui.message(_("Error getting file type"))

	@scriptHandler.script(
		description=_("Announces start marker position."),
		gesture="kb:alt+shift+s",
		speakOnDemand=True,
	)
	def script_announceStartMarker(self, gesture):
		try:
			audioSelectionParsed = self.getAudioSelectionParsed()
			if not audioSelectionParsed or len(audioSelectionParsed) < 1:
				ui.message(_("Start marker position unavailable"))
			else:
				ui.message(_("Start marker: {position}").format(position=audioSelectionParsed[0]))
		except Exception:
			ui.message(_("Start marker position unavailable"))

	@scriptHandler.script(
		description=_("Announces finish marker position."),
		gesture="kb:alt+shift+f",
		speakOnDemand=True,
	)
	def script_announceFinishMarker(self, gesture):
		try:
			audioSelectionParsed = self.getAudioSelectionParsed()
			if not audioSelectionParsed or len(audioSelectionParsed) < 3:
				ui.message(_("Finish marker position unavailable"))
			else:
				ui.message(_("Finish marker: {position}").format(position=audioSelectionParsed[2]))
		except Exception:
			ui.message(_("Finish marker position unavailable"))

	@scriptHandler.script(
		description=_("Announces selected duration."),
		gesture="kb:alt+shift+d",
		speakOnDemand=True,
	)
	def script_announceSelectionDuration(self, gesture):
		try:
			audioSelectionParsed = self.getAudioSelectionParsed()
			if not audioSelectionParsed or len(audioSelectionParsed) < 4:
				ui.message(_("Selection duration unavailable"))
			else:
				ui.message(_("Selection duration: {duration}").format(duration=audioSelectionParsed[3]))
		except Exception:
			ui.message(_("Selection duration unavailable"))

	@scriptHandler.script(
		description=_("Announces the active control."),
		gesture="kb:alt+shift+a",
		speakOnDemand=True,
	)
	def script_announceActiveControl(self, gesture):
		try:
			focus = api.getFocusObject()
			controlName = focus.name if focus.name else "Unnamed"
			controlType = focus.role.displayString if hasattr(focus.role, 'displayString') else str(focus.role)
			ui.message(f"{controlName} {controlType}")
		except Exception:
			ui.message(_("Active control unavailable"))

	@scriptHandler.script(
		description=_("Announces the cursor position in seconds."),
		gesture="kb:alt+shift+u",
		speakOnDemand=True,
	)
	def script_announceAudioPosition(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
		else:
			ui.message(self.getAudioPos())

	@scriptHandler.script(
		description=_("Announces elapsed time."),
		gesture="kb:alt+shift+e",
		speakOnDemand=True,
	)
	def script_announceElapsedTime(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
		else:
			audioPos = self.getAudioPos()
			ui.message(_("Elapsed: {elapsed}").format(elapsed=audioPos))

	@scriptHandler.script(
		description=_("Announces remaining length of the audio track."),
		gesture="kb:alt+shift+r",
		speakOnDemand=True,
	)
	def script_announceRemainingTime(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
			return
		audioPos = self.getAudioPos(raw=True)
		if not audioPos or " " in audioPos or not self.getTrackLength():
			ui.message(_("Cannot tell you remaining time for the current track"))
		else:
			if ":" in audioPos:
				remainingTime = self.getRemainingTime(audioPos)
				ui.message(_("Remaining: {remaining}").format(remaining=remainingTime))
			elif float(audioPos) == 0.0:
				ui.message(_("Remaining: {remaining}").format(remaining=self.getTrackLength(raw=self.appModule.productVersion >= "7")))
			else:
				remainingTime = self.getRemainingTime(audioPos)
				ui.message(_("Remaining: {remaining}").format(remaining=remainingTime))

	# Audio selection summary
	@scriptHandler.script(
		description=_("Announces a summary on audio selection info such as selection duration."),
		gesture="kb:control+nvda+3",
		speakOnDemand=True,
	)
	def script_announceAudioSelection(self, gesture):
		try:
			audioSelectionParsed = self.getAudioSelectionParsed()
			if not audioSelectionParsed or len(audioSelectionParsed) < 4:
				ui.message(
					_("Unable to obtain audio selection summary. Please close and reopen the audio track.")
				)
			else:
				ui.message(
					_("{audioSelectionStart} to {audioSelectionEnd} {audioSelectionLength}").format(
						audioSelectionStart=audioSelectionParsed[0],
						audioSelectionEnd=audioSelectionParsed[2],
						audioSelectionLength=audioSelectionParsed[3],
					)
				)
		except Exception:
			pass

	# Track length
	@scriptHandler.script(
		description=_("Announces total length of the audio track."),
		gesture="kb:control+nvda+2",
		speakOnDemand=True,
	)
	def script_announceTrackLength(self, gesture):
		if not self.isTrackLoaded():
			ui.message(_("No track loaded"))
		else:
			trackLengthSTR = self.getTrackLength(raw=self.appModule.productVersion >= "7")
			if not trackLengthSTR:
				ui.message(_("Track length is unavailable. Please close and reopen the audio track."))
			else:
				ui.message(_("Track length: {trackLength}").format(trackLength=trackLengthSTR))

	# Audio channels and zoom level.

	@scriptHandler.script(
		description=_("Announces the audio channel you are editing."),
		gesture="kb:control+nvda+1",
		speakOnDemand=True,
	)
	def script_announceAudioChannels(self, gesture):
		channelSTR = self.getAudioChannels()
		if channelSTR in ["Multiple", "All"]:
			ui.message(self.audioChannelValues[channelSTR])
		else:
			ui.message(
				_("Selected channel: {audioChannel}").format(
					audioChannel=self.audioChannelValues.get(channelSTR, channelSTR)
				)
			)

	@scriptHandler.script(gestures=["kb:control+shift+l", "kb:control+shift+r", "kb:control+shift+a"])
	def script_selectChannel(self, gesture):
		gesture.send()
		time.sleep(0.05)
		self.script_announceAudioChannels(gesture)

	@scriptHandler.script(
		description=_("Announces audio zoom level."),
		gesture="kb:control+nvda+4",
		speakOnDemand=True,
	)
	def script_announceZoomLevel(self, gesture):
		ui.message(_("Zoom level: {zoomLevel}").format(zoomLevel=self.getZoomLevel()))

	@scriptHandler.script(
		gestures=[
			f"kb:shift+{command}"
			for command in ["upArrow", "downArrow", "0", "1", "2", "3", "4", "5", "6", "a"]
		]
	)
	def script_changeZoomLevel(self, gesture):
		gesture.send()
		time.sleep(0.05)
		self.script_announceZoomLevel(gesture)


class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		global multiInstance
		multiInstance += 1

	def event_NVDAObject_init(self, obj: NVDAObject):
		if isinstance(obj, Window):
			if obj.windowClassName in ("TBitton", "TImageButton"):
				obj.role = controlTypes.Role.BUTTON
			elif (
				"Form" in obj.windowClassName
				and "MainForm" not in obj.windowClassName
				or obj.windowClassName == "TEffectWrapper"
			):
				if obj.windowClassName != "TSoundForm":
					obj.role = controlTypes.Role.DIALOG

	def chooseNVDAObjectOverlayClasses(self, obj: NVDAObject, clsList: list[NVDAObject]) -> None:
		if obj.windowClassName == "TSoundForm":
			clsList.insert(0, SoundWindow)
		elif obj.windowClassName in ("TNumEdit", "TTimeEdit"):
			try:
				clsList.remove(DisplayModelEditableText)
				clsList.insert(0, edit.Edit)
			except ValueError:
				pass

	statusBarCache: dict[int, NVDAObject] = {}

	def _get_statusBars(self, statBarIndex: int, refill: bool = False) -> NVDAObject:
		global multiInstance
		index = 0
		if refill or multiInstance > 1 or not len(self.statusBarCache):
			for child in api.getForegroundObject().children:
				if child.role == controlTypes.Role.STATUSBAR:
					if not child.displayText:
						child.redraw()
					self.statusBarCache[index] = child
					index += 1
		return self.statusBarCache[statBarIndex]
