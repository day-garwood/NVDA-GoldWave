# Goldwave App Module
# An add-on for NVDA
# Copyright 2013 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import addonHandler
import api
import speech
import braille
from controlTypes import ROLE_BUTTON, ROLE_DIALOG
addonHandler.initTranslation()
from NVDAObjects.IAccessible import IAccessible # Since we're dealing with IAccessible.
import scriptHandler
from NVDAObjects.window import Window # Various buttons.
import ui

# A number of NVDA objects for GoldWave:

class GoldwaveNumericEdit(IAccessible):
	# TNumEdit class. Credit: David P.

	__gestures = {
		"kb:downArrow": "updatevalue",
		"kb:upArrow": "updatevalue",
		"kb:pageUp": "updatevalue",
		"kb:pageDown": "updatevalue"
	}

	def script_updatevalue(self, gesture):
		gesture.send()
		ui.message(self.windowText)

class SoundWindow(IAccessible):
	# The GoldWave's sound window. Here one can play, record and edit audio files.

	scriptCategory = "GoldWave"

	# Announcement of commands is enabled by default.
	commandAnnouncement = True

	def message(self, text):
		braille.handler.message(text)
		if self.commandAnnouncement:
			speech.speakMessage(text)

	def script_toggleCommandAnnouncement(self, gesture):
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

	# Get audio positions.
	def getAudioPos(self):
		# Above the status bar is the audio position and selection info bar. Fetch info from there via object navigation.
		fg = api.getForegroundObject()
		fgChild = fg.children[-3]
		# Current cursor position.
		if not fgChild.displayText: fgChild.redraw()
		audioPos = fgChild.children[3].displayText.replace('\t', '')
		# Translators: Presented when audio track position information can not be located.
		return _("Track position not available") if not audioPos or " " in audioPos else audioPos

	def getAudioSelection(self):
		# A method to get audio selection. Unlike audio position getter, this one requires display text, as info is not obj.name.
		fg = api.getForegroundObject()
		fgChild = fg.children[-3]
		# Audio selection information.
		# What if fgChild returns empty string? (core ticket 3623/2892) If so, redraw (expensive; don't use this a lot).
		if not fgChild.displayText: fgChild.redraw()
		audioSelection = fgChild.children[2].displayText.replace('\t', '')
		return audioSelection

	def getAudioSelectionParsed(self):
		# Continuing from above, get marker positions and selection duration. This is a string parsing problem.
		# Store the parsed strings into a list.
		return self.getAudioSelection().split(" ")

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
		"Right":_("right")
	}

	def getAudioChannels(self):
		# Based on the constants above and the return value below, get channel information.
		fg = api.getForegroundObject()
		fgChild = fg.children[-3]
		if not fgChild.displayText: fgChild.redraw()
		audioChannels = fgChild.children[0].displayText
		return self.audioChannelValues[audioChannels]

	def getTrackLength(self):
		fg = api.getForegroundObject()
		fgChild = fg.children[-3]
		if not fgChild.displayText: fgChild.redraw()
		trackLength = fgChild.children[1].displayText
		return trackLength

	def getZoomLevel(self):
		fg = api.getForegroundObject()
		fgChild = fg.children[-2]
		if not fgChild.displayText: fgChild.redraw()
		zoomLevel = fgChild.children[1].displayText
		return zoomLevel

	# Audio editing scripts:

	def script_dropStartMarker(self, gesture):
		gesture.send()
		# Translators: The start marker position for selecting parts of the audio track (example output: "Start: 0.00").
		marker = _("Start: {startMarkerPos}").format(startMarkerPos = self.getAudioSelectionParsed()[0])
		self.message(marker)
	# Translators: Input help mode message for a Goldwave command.
	script_dropStartMarker.__doc__=_("Drops the start marker and announces start marker position.")

	def script_dropFinishMarker(self, gesture):
		gesture.send()
		# Translators: The finish marker position for selecting parts of the audio track (example output: "Finish: 5.00").
		marker = _("Finish: {finishMarkerPos}").format(finishMarkerPos = self.getAudioSelectionParsed()[2])
		self.message(marker)
	# Translators: Input help mode message for a Goldwave command.
	script_dropFinishMarker.__doc__=_("Drops the finish marker and announces finish marker position.")

	def script_playSelection(self, gesture):
		gesture.send()
		# Translators: Presented when selected audio is playing.
		self.message(_("Play selection"))
	# Translators: Input help mode message for a Goldwave command.
	script_playSelection.__doc__=_("Plays the trakc between start and finish markers.")

	def script_selectAll(self, gesture):
		gesture.send()
		# Translators: Presented when all parts of the audio track is selected.
		self.message(_("Select All"))
	# Translators: Input help mode message for a Goldwave command.
	script_selectAll.__doc__=_("Selects the entire track.")

	def script_dropCue(self, gesture):
		gesture.send()
		# Translators: A message in GoldWave when an audio cue is dropped at the current audio position.
		self.message(_("Cue"))
	# Translators: Input help mode message for a Goldwave command.
	script_dropCue.__doc__=_("Drops a cue point at the current audio position.")

	def script_dropCueAtStartMarker(self, gesture):
		gesture.send()
		# Translators: Presented when audio cue is dropped at the start marker position.
		self.message(_("Cue dropped at start marker"))
	# Translators: Input help mode message for a Goldwave command.
	script_dropCueAtStartMarker.__doc__=_("Drops a cue point at the current start marker position.")

	def script_dropCueAtFinishMarker(self, gesture):
		gesture.send()
		# Translators: Presented when an audio cue is dropped at the finish marker position.
		self.message(_("Cue dropped at finish marker"))
	# Translators: Input help mode message for a Goldwave command.
	script_dropCueAtFinishMarker.__doc__=_("Drops a cue point at the current finish marker position.")

	def script_moveStartMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		self.message(_("Start marker at next cue"))
	script_moveStartMarkerToNextCuePos.__doc__="Moves the start marker to the next cue position."

	def script_moveStartMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
self.message(_("Start marker at previous cue"))
	script_moveStartMarkerToPrevCuePos.__doc__="Moves the start marker to the previous cue position."

	def script_moveFinishMarkerToNextCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the finish marker is moved to the next cue position.
		self.message(_("Finish marker at next cue"))
	script_moveFinishMarkerToNextCuePos.__doc__="Moves the finish marker to the next cue position."

	def script_moveFinishMarkerToPrevCuePos(self, gesture):
		gesture.send()
		# Translators: Presented when the start marker is moved to the next cue position.
		self.message(_("Finish marker at previous cue"))
	script_moveFinishMarkerToPrevCuePos.__doc__="Moves the finish marker to the previous cue position."

	def script_deleteSelection(self, gesture):
		gesture.send()
		# Translators: Presented when audio selection is deleted.
		self.message(_("deleted"))
	# Translators: Input help mode message for a Goldwave command.
	script_deleteSelection.__doc__=_("Deletes the currently selected audio.")

	def script_trimSelection(self, gesture):
		# Cannot just assign function objects to another, so a workaround for this problem.
		self.script_deleteSelection(gesture)
	# Translators: Input help mode message for a Goldwave command.
	script_trimSelection.__doc__=_("Trims the audio outside the selected audio.")

	# Playback and recording:

	def script_play(self, gesture):
		gesture.send()
		# Translators: Presented when a track is playing in Goldwave.
		self.message(_("play"))
	# Translators: Input help mode message for a Goldwave command.
	script_play.__doc__=_("Plays the audio track.")

	def script_rewind(self, gesture):
		gesture.send()
		# Translators: Presented when a track is rewinding in Goldwave.
		self.message(_("rewind"))
	# Translators: Input help mode message for a Goldwave command.
	script_rewind.__doc__=_("Rewinds through an audio track.")

	def script_forward(self, gesture):
		gesture.send()
		# Translators: Presented when fast forwarding a track in Goldwave.
		self.message(_("fast forward"))
	# Translators: Input help mode message for a Goldwave command.
	script_forward.__doc__=_("Fast forwards through an audio track.")

	def script_pause(self, gesture):
		gesture.send()
		# Translators: Presented when pausing a track in Goldwave.
		self.message(_("pause"))
	# Translators: Input help mode message for a Goldwave command.
	script_pause.__doc__=_("Pauses the audio track.")

	def script_stop(self, gesture):
		gesture.send()
		# Translators: Presented when stopping a track in in Goldwave.
		self.message(_("stop"))
	# Translators: Input help mode message for a Goldwave command.
	script_stop.__doc__=_("stops the audio track.")

	def script_startRecord(self, gesture):
		gesture.send()
		# Translators: Presented when starting recording in Goldwave.
		self.message(_("record"))
	# Translators: Input help mode message for a Goldwave command.
	script_startRecord.__doc__=_("Starts recording audio.")

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
			audioSelection = (_("Unable to obtain audio selection summary. Please close and reopen the audio track."))
		else:
			# Translators: The audio selection summary message (example output: "0.00 to 1.00 (1.00)").
			audioSelection = "{audioSelectionStart} to {audioSelectionEnd} {audioSelectionLength}".format(audioSelectionStart = audioSelectionParsed[0], audioSelectionEnd = audioSelectionParsed[2], audioSelectionLength = audioSelectionParsed[3])
		self.message(audioSelection)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioSelection.__doc__=_("Announces a summary on audio selection info such as selection duration.")

	def script_announceTrackLength(self, gesture):
		trackLengthSTR, trackLengthMSG = self.getTrackLength(), ""
		if not trackLengthSTR:
			# Translators: Presented when there is no track length information.
			trackLengthMSG = _("Track length is unavailable. Please close and reopen the audio track.")
		else:
			trackLengthMSG = "Track length: {trackLength}".format(trackLength = trackLengthSTR)
		self.message(trackLengthMSG)
	# Translators: Input help mode message for a Goldwave command.
	script_announceTrackLength.__doc__=_("Announces total length of the audio track.")

	# Audio channels and zoom level.

	def script_announceAudioChannels(self, gesture):
		# Translators: Presented to indicate the selected channel for the track (example output: "Selected channel: mono").
		channel = _("Selected channel: {audioChannel}").format(audioChannel = self.getAudioChannels())
		self.message(channel)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioChannels.__doc__=_("Announces the audio channel you are editing.")

	def script_announceZoomLevel(self, gesture):
		# Translators: Presented to indicate audio selection zoom level (example output: "Zoom level: 10.000").
		zoom = _("Zoom level: {zoomLevel}").format(zoomLevel = self.getZoomLevel())
		self.message(zoom)
	# Translators: Input help mode message for a Goldwave command.
	script_announceZoomLevel.__doc__=_("Announces audio zoom level.")

	def script_changeZoomLevel(self, gesture):
		gesture.send()
		self.script_announceZoomLevel(gesture)
	# Translators: Input help mode message for a Goldwave command.
	script_changeZoomLevel.__doc__=_("Changes zoom level and announces the new level.")

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
		"kb:nvda+shift+c":"toggleCommandAnnouncement",
		"kb:control+shift+p":"announceAudioPosition",
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
		"kb:shift+a":"changeZoomLevel"
	}


class AppModule(appModuleHandler.AppModule):

	# Presets and control windows: Work with buttons with custom window class names.

	def event_NVDAObject_init(self, obj):
		# Provide standardized control roles for the following objects.
		if isinstance(obj, Window):
			# For working with buttons such as presets window and control window.
			if obj.windowClassName == "TBitton" or obj.windowClassName == "TImageButton":
				obj.role = ROLE_BUTTON
			# For windows which NVDA should recognize as dialogs.
			elif "Form" in obj.windowClassName and "MainForm" not in obj.windowClassName or obj.windowClassName == "TEffectWrapper":
				obj.role = ROLE_DIALOG


	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# Custom nvda overlay objects for sound window and edit fields:
		if obj.windowClassName == "TWaveView":
			clsList.insert(0, SoundWindow)
		if obj.windowClassName == 'TNumEdit':
			clsList.insert(0, GoldwaveNumericEdit)

