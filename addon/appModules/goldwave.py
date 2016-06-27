# GoldWave App Module
# An add-on for NVDA
# Copyright 2013-2015 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import addonHandler
import api
import speech
import braille
from controlTypes import ROLE_BUTTON, ROLE_DIALOG, ROLE_PANE, ROLE_GROUPING, ROLE_STATUSBAR
addonHandler.initTranslation()
from NVDAObjects.IAccessible import IAccessible
import scriptHandler
from NVDAObjects.window import Window, DisplayModelEditableText, edit # Various buttons and numeric edit fields.
import ui
import tones

# Detect multiple instances of GoldWave.
multiInstance = 0

# A number of NVDA objects for GoldWave:

class SoundWindow(IAccessible):
	"""The GoldWave's sound window. Here one can play, record and edit audio files.
	"""

	scriptCategory = "GoldWave"

	# Announcement of commands is enabled by default.
	commandAnnouncement = True

	def message(self, text):
		braille.handler.message(text)
		if self.appModule.commandAnnouncement:
			speech.speakMessage(text)

	# A master function to obtain needed info from status bars.
	def getStatusInfo(self, statBarIndex, childIndex):
		fgChild = self.appModule._get_statusBars(statBarIndex)
		if not fgChild.displayText:
			fgChild.redraw()
		#fgChild = self.appModule._get_statusBars(statBarIndex, refill=True)
		try:
			info = fgChild.getChild(childIndex).displayText
		except IndexError:
			return ""
		return info

	# Get audio positions.
	def getAudioPos(self, raw=False):
		# Above the status bar is the audio position and selection info bar. See if this control can be fetched.
		global multiInstance
		# Have to definitely call the info getter twice.
		audioPos = self.getStatusInfo(0, 3)
		if multiInstance > 1: audioPos = self.getStatusInfo(0, 3)
		# Raw means return just the raw text, used in remaining time and other position scripts.
		if raw: return audioPos
		"""fgChild = self.appModule._get_statusBars(0)
		# Current cursor position.
		if not fgChild.displayText:
			fgChild.redraw()
		audioPos = fgChild.getChild(3).displayText.replace('\t', '')"""
		# Translators: Presented when audio track position information can not be located.
		return _("Track position not available") if not audioPos or " " in audioPos else audioPos

	def getAudioSelection(self):
		# Call the info getter twice to obtain audio selection (relies on display text).
		global multiInstance
		audioSelection = self.getStatusInfo(0, 2)
		if multiInstance > 1: audioSelection = self.getStatusInfo(0, 2)
		"""try:
			if not fgChild.displayText: fgChild.redraw()
		except AttributeError:
			fgChild = self.appModule._get_statusBars(0, refill=True)
		try:
			audioSelection = fgChild.getChild(2).displayText
		except IndexError:
			pass"""
		return audioSelection

	def getAudioSelectionParsed(self):
		# Get marker positions and selection duration.
		# Store the parsed strings into a list.
		parsed = self.getAudioSelection()
		return parsed.split()


	# Get channel information. But first, a few constants (to help translators):
	audioChannelValues={
		# Translators: One of the channel values when editing audio track in Goldwave.
		"":_("Channel information unavailable"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Mono":_("mono"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Stereo":_("stereo"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Left":_("left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Right":_("right"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Center":_("center"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"w frequenc":_("low frequency"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Back left":_("back left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Back right":_("back right"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Side left":_("side left"),
		# Translators: One of the channel values when editing audio track in Goldwave.
		"Side right":_("side right"),
		# Translators: Presented when multiple channels are selected (GoldWave 6 and higher).
		"Multiple":_("Multiple channels selected"),
		# Translators: Presented when all channels (3.1, 5.1, 7.1) are selected (GoldWave 6 and higher).
		"All":_("All channels selected")
	}

	def getAudioChannels(self):
		# Based on the constants above and the return value below, get channel information.
		audioChannels = self.getStatusInfo(0, 0)
		if audioChannels not in self.audioChannelValues.keys():
			audioChannels = self.getStatusInfo(0, 0)
		"""try:
			if not fgChild.displayText: fgChild.redraw()
		except AttributeError:
			fgChild = self.appModule._get_statusBars(0, refill=True)
		try:
			audioChannels = fgChild.firstChild.displayText
		except IndexError:
			return"""
		return audioChannels

	def getTrackLength(self):
		fgChild = self.appModule._get_statusBars(0)
		try:
			if not fgChild.displayText: fgChild.redraw()
		except AttributeError:
			fgChild = self.appModule._get_statusBars(0)
		trackLength = fgChild.getChild(1).displayText
		return trackLength

	# Convert time to seconds: Convert hh:mm:ss to seconds.
	# Needed in various functions.
	def convertTime2Sec(self, *times):
		timeList = []
		for time in times:
			if len(time) == 1:
				timeList.append(float(time[0]))
			elif len(time) == 2:
				min = float(time[0])*60.0
				timeList.append(min+float(time[1]))
			else:
				hour, min = float(time[0])*3600.0, float(time[1])*60.0
				timeList.append(hour+min+float(time[2]))
		return timeList

	def getRemainingTime(self, audioPos):
		trackLengthParsed = self.getTrackLength().split(":")
		audioPosParsed = audioPos.split(":")
		# An obvious solution is to use recursive subtraction.
		# That is, subtract the last elements, and if audio pos is greater than track length for that particular cell, move to the left.
		# However, a simpler solution is to convert the time value to seconds, subtract then format it back to hh:mm:ss format.
		timesec = self.convertTime2Sec(audioPosParsed, trackLengthParsed)
		remainingTimeSec = timesec[1]-timesec[0]
		# Now convert the seconds back to hh:mm:ss format.
		if remainingTimeSec < 60.0:
			return str(remainingTimeSec)
		elif 60.0 <= remainingTimeSec < 3600.0:
			min, sec = divmod(remainingTimeSec, 60.0)
			mm, ss = str(int(min)).zfill(2), str(sec).zfill(2)
			return ":".join([mm, ss])
		else:
			hour, min = divmod(remainingTimeSec, 3600.0)
			min, sec = divmod(min, 60.0)
			hh, mm, ss = str(int(hour)), str(int(min)).zfill(2), str(sec).zfill(2)
			return ":".join([hh, mm, ss])

	def getZoomLevel(self):
		try:
			zoomLevel = self.getStatusInfo(1, 1)
		except IndexError:
			zoomLevel = self.getStatusInfo(1, 1)
		"""try:
			if not fgChild.displayText: fgChild.redraw()
		except AttributeError:
			fgChild = self.appModule._get_statusBars(1, refill=True)
		zoomLevel = fgChild.getChild(1).displayText"""
		return zoomLevel

	# Audio editing scripts:

	def script_dropStartMarker(self, gesture):
		gesture.send()
		# Translators: The start marker position for selecting parts of the audio track (example output: "Start: 0.00").
		marker = _("Start: {startMarkerPos}").format(startMarkerPos = self.getAudioSelectionParsed()[0])
		self.message(marker)

	def script_dropFinishMarker(self, gesture):
		gesture.send()
		# Translators: The finish marker position for selecting parts of the audio track (example output: "Finish: 5.00").
		marker = _("Finish: {finishMarkerPos}").format(finishMarkerPos = self.getAudioSelectionParsed()[2])
		self.message(marker)

	def script_playSelection(self, gesture):
		gesture.send()
		# Translators: Presented when selected audio is playing.
		self.message(_("Play selection"))

	def script_selectAll(self, gesture):
		gesture.send()
		# Translators: Presented when all parts of the audio track is selected.
		self.message(_("Select All"))

	def script_dropCue(self, gesture):
		gesture.send()
		# Translators: A message in GoldWave when an audio cue is dropped at the current audio position.
		self.message(_("Cue"))

	def script_dropCueAtStartMarker(self, gesture):
		gesture.send()
		# Translators: Presented when audio cue is dropped at the start marker position.
		self.message(_("Cue dropped at start marker"))

	def script_dropCueAtFinishMarker(self, gesture):
		gesture.send()
		# Translators: Presented when an audio cue is dropped at the finish marker position.
		self.message(_("Cue dropped at finish marker"))

	def script_moveStartMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		self.message(_("Start marker at next cue"))

	def script_moveStartMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		self.message(_("Start marker at previous cue"))

	def script_moveFinishMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the finish marker is moved to the next cue position.
		self.message(_("Finish marker at next cue"))

	def script_moveFinishMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		self.message(_("Finish marker at previous cue"))

	def script_deleteSelection(self, gesture):
		gesture.send()
		# Translators: Presented when audio selection is deleted.
		self.message(_("deleted"))

	def script_trimSelection(self, gesture):
		# Cannot just assign function objects to another, so a workaround for this problem.
		self.script_deleteSelection(gesture)

	# Playback and recording:

	def script_play(self, gesture):
		gesture.send()
		# Translators: Presented when a track is playing in Goldwave.
		self.message(_("play"))

	def script_rewind(self, gesture):
		gesture.send()
		# Translators: Presented when a track is rewinding in Goldwave.
		self.message(_("rewind"))

	def script_forward(self, gesture):
		gesture.send()
		# Translators: Presented when fast forwarding a track in Goldwave.
		self.message(_("fast forward"))

	def script_pause(self, gesture):
		gesture.send()
		# Translators: Presented when pausing a track in Goldwave.
		self.message(_("pause"))

	def script_stop(self, gesture):
		gesture.send()
		# Translators: Presented when stopping a track in in Goldwave.
		self.message(_("stop"))

	def script_startRecord(self, gesture):
		gesture.send()
		# Translators: Presented when starting recording in Goldwave.
		self.message(_("record"))

	# Audio position scripts: markers, selection duration.

	def script_announceAudioPosition(self, gesture):
		# Shouldn't say anything unless in audio editing view.
		curAudioPos = self.getAudioPos()
		self.message(curAudioPos)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioPosition.__doc__=_("Announces the current audio position in seconds.")

	def script_announceAudioSelection(self, gesture):
		# Parse this string to get individual info such as marker positions.
		audioSelectionParsed, audioSelection = self.getAudioSelectionParsed(), ""
		if not audioSelectionParsed:
			# Translators: Presented when there is no audio selection summary available.
			audioSelection = _("Unable to obtain audio selection summary. Please close and reopen the audio track.")
		else:
			# Translators: The audio selection summary message (example output: "0.00 to 1.00 (1.00)").
			audioSelection = _("{audioSelectionStart} to {audioSelectionEnd} {audioSelectionLength}").format(audioSelectionStart = audioSelectionParsed[0], audioSelectionEnd = audioSelectionParsed[2], audioSelectionLength = audioSelectionParsed[3])
		self.message(audioSelection)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioSelection.__doc__=_("Announces a summary on audio selection info such as selection duration.")

	def script_announceTrackLength(self, gesture):
		trackLengthSTR, trackLengthMSG = self.getTrackLength(), ""
		if not trackLengthSTR:
			# Translators: Presented when there is no track length information.
			trackLengthMSG = _("Track length is unavailable. Please close and reopen the audio track.")
		else:
			trackLengthMSG = _("Track length: {trackLength}").format(trackLength = trackLengthSTR)
		self.message(trackLengthMSG)
	# Translators: Input help mode message for a Goldwave command.
	script_announceTrackLength.__doc__=_("Announces total length of the audio track.")

	def script_announceRemainingTime(self, gesture):
		audioPos = self.getAudioPos(raw=True)
		if not audioPos or " " in audioPos or not self.getTrackLength():
			# Translators: An error message presented when remaining time cannot be anounced.
			ui.message(_("Cannot tell you remaining time for the current track"))
		else:
			if ":" in audioPos:
				ui.message(self.getRemainingTime(audioPos))
			elif float(audioPos) == 0.0:
				ui.message(self.getTrackLength())
			else:
				ui.message(self.getRemainingTime(audioPos))

	# Audio channels and zoom level.

	def script_announceAudioChannels(self, gesture):
		channelSTR = self.getAudioChannels()
		if channelSTR in ["Multiple", "All"]:
			# Translators: Presented when all or multiple channels (in 3.1, 5.1 or 7.1 channels) are selected (GoldWave 6 and higher).
			channel = self.audioChannelValues[channelSTR]
		else:
			# Translators: Presented to indicate the selected channel for the track (example output: "Selected channel: mono").
			channel = _("Selected channel: {audioChannel}").format(audioChannel = self.audioChannelValues[channelSTR])
		self.message(channel)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioChannels.__doc__=_("Announces the audio channel you are editing.")

	def script_selectChannel(self, gesture):
		gesture.send()
		if (gesture.displayName == "ctrl+shift+a" and self.appModule.productVersion.startswith("5")) or (gesture.displayName == "ctrl+shift+b" and self.appModule.productVersion.startswith("6")): return
		else: self.script_announceAudioChannels(gesture)

	def script_announceZoomLevel(self, gesture):
		# Translators: Presented to indicate audio selection zoom level (example output: "Zoom level: 10.000").
		zoom = _("Zoom level: {zoomLevel}").format(zoomLevel = self.getZoomLevel())
		self.message(zoom)
	# Translators: Input help mode message for a Goldwave command.
	script_announceZoomLevel.__doc__=_("Announces audio zoom level.")

	def script_changeZoomLevel(self, gesture):
		gesture.send()
		self.script_announceZoomLevel(gesture)

	__gestures={
		"KB:[":"dropStartMarker",
		"KB:]":"dropFinishMarker",
		"KB:control+a":"selectAll",
		"kB:control+[":"playSelection",
		"kb:control+q":"dropCue",
		"KB:q":"dropCueAtStartMarker",
		"KB:shift+q":"dropCueAtFinishMarker",
		"kb:control+j":"moveStartMarkerToNextCuePos",
		"kb:control+shift+j":"moveStartMarkerToPrevCuePos",
		"kb:alt+j":"moveFinishMarkerToNextCuePos",
		"kb:alt+shift+j":"moveFinishMarkerToPrevCuePos",
		"kb:delete":"deleteSelection",
		"kb:control+t":"trimSelection",
		"KB:f2":"play",
		"KB:f3":"play",
		"kb:f4":"play",
		"kb:f5":"rewind",
		"kb:f6":"forward",
		"kb:f7":"pause",
		"kb:control+f7":"pause",
		"kb:f8":"stop",
		"kb:control+f8":"stop",
		"kb:control+f9":"startRecord",
		"kb:control+shift+p":"announceAudioPosition",
		"kb:NVDA+shift+r":"announceRemainingTime",
		"kb:control+nvda+3":"announceAudioSelection",
		"kb:control+nvda+2":"announceTrackLength",
		"kb:control+nvda+1":"announceAudioChannels",
		"kb:control+nvda+4":"announceZoomLevel",
		"kb:shift+uparrow":"changeZoomLevel",
		"kb:shift+downarrow":"changeZoomLevel",
		"kb:shift+0":"changeZoomLevel",
		"kb:shift+1":"changeZoomLevel",
		"kb:shift+2":"changeZoomLevel",
		"kb:shift+3":"changeZoomLevel",
		"kb:shift+4":"changeZoomLevel",
		"kb:shift+5":"changeZoomLevel",
		"kb:shift+6":"changeZoomLevel",
		"kb:shift+a":"changeZoomLevel",
		"kb:control+shift+l":"selectChannel",
		"kb:control+shift+r":"selectChannel",
		"kb:control+shift+a":"selectChannel",
		"kb:control+shift+b":"selectChannel"
	}


class AppModule(appModuleHandler.AppModule):

	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		global multiInstance
		multiInstance+=1

	# Announcement of commands is enabled by default.
	commandAnnouncement = True

	def script_toggleCommandAnnouncement(self, gesture):
		focus = api.getFocusObject()
		if focus.windowClassName not in ("TWaveView", "TSoundForm"):
			# Translators: Presented when command announcement toggle is unavailable.
			text = _("You need to be in sound window to toggle command announcement")
		else:
			self.commandAnnouncement = not self.commandAnnouncement
			# Handle the announcement of this script separately, since we need to speak even when false.
			if self.commandAnnouncement:
				# Translators: Presented when command announcement messages are turned on in Goldwave.
				text = _("command announcement on")
			else:
				# Translators: Presented when command announcement messages are turned off in Goldwave.
				text = _("command announcement off")
		ui.message(text)
	# Translators: Input help mode message for command announcement command in Goldwave.
	script_toggleCommandAnnouncement.__doc__=_("Toggles whether NVDA announces editing commands during audio recording or playback.")

	# Presets and control windows: Work with buttons with custom window class names.

	def event_NVDAObject_init(self, obj):
		# Provide standardized control roles for the following objects.
		if isinstance(obj, Window):
			# For working with buttons such as presets window and control window.
			if obj.windowClassName == "TBitton" or obj.windowClassName == "TImageButton":
				obj.role = ROLE_BUTTON
			# For windows which NVDA should recognize as dialogs.
			elif "Form" in obj.windowClassName and "MainForm" not in obj.windowClassName or obj.windowClassName == "TEffectWrapper":
				# In GoldWave 6, the sound window has the window class name of "tSoundForm" and should not be recognized as a dialog.
				if obj.windowClassName != "TSoundForm":
					obj.role = ROLE_DIALOG
		if obj.windowClassName == 'TNumEdit' and self.productVersion.startswith("5"):
			# Get the correct edit field name in GoldWave 5.x.
			fieldNameObj = obj.parent.parent
			if fieldNameObj.role == ROLE_PANE and fieldNameObj.name:
				obj.name = fieldNameObj.name if not obj.name else fieldNameObj.name + " " + obj.name

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Custom NVDA overlay objects for sound window and edit fields:
		if obj.windowClassName in ("TWaveView", "TSoundForm"):
			# TWaveView = 5.x, TSoundForm = 6.x.
			clsList.insert(0, SoundWindow)
		elif obj.windowClassName in ("TNumEdit", "TTimeEdit"):
			try:
				clsList.remove(DisplayModelEditableText)
				clsList.insert(0, edit.Edit)
			except ValueError:
				pass

	# Cache the needed status bar objects.
	statusBarCache = {}

	def _get_statusBars(self, statBarIndex, refill=False):
		global multiInstance
		# In case multiple instances of GoldWave are running, flush the status bar cache.
		index = 0
		if refill or multiInstance > 1 or not len(self.statusBarCache):
			for child in api.getForegroundObject().children:
				if child.role == ROLE_STATUSBAR:
					if not child.displayText: child.redraw()
					self.statusBarCache[index] = child
					index+=1
		return self.statusBarCache[statBarIndex]

	__gestures={
		"kb:nvda+shift+c":"toggleCommandAnnouncement",
	}
