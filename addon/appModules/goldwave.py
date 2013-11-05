# Goldwave App Module
# An add-on for NVDA
# Copyright 2013 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import addonHandler
import api
import speech # No need for braille yet.
addonHandler.initTranslation()
from NVDAObjects.IAccessible import IAccessible # Since we're dealing with IAccessible.
import scriptHandler
from NVDAObjects.window import Window # Presets controls.

class AppModule(appModuleHandler.AppModule):
	
	# A few variables (mostly to control speech):
	commandAnnouncement = 1 # Announcement of commands is enabled by default, hence value of 1.
	
	# And the toggle method for this variable:
	def script_toggleCommandAnnouncement(self, gesture):
		if self.commandAnnouncement == 1:
			self.commandAnnouncement = 0 # Command announcement off.
			# Translators: Spoken when command announcement messages are turned off in Goldwave.
			speech.speakMessage(_("command announcement off"))
		else:
			self.commandAnnouncement = 1 # Command announcement on.
			# Translators: Spoken when command announcement messages are turned on in Goldwave.
			speech.speakMessage(_("command announcement on"))
	# Translators: Input help mode message for command announcement command in Goldwave.
	script_toggleCommandAnnouncement.__doc__=_("Toggles whether NVDA announces editing commands during audio recording or playback.")
	
	# A number of utility functions follows:
	
	def soundWindow(self):
		obj = api.getFocusObject()
		return 1 if obj.windowClassName == "TWaveView" else 0 # For now, nav obj's name is used; may use other attributes later.
	
	# Get audio positions.
	
	def getAudioPos(self):
		# Above the status bar is the audio position and selection info bar. Fetch info from there via object navigation.
		fg = api.getForegroundObject() # A convenient place to start.
		fgChild = fg.children[1] # Underneath the fg.
		audioPos = fgChild.children[3].name # Current cursor position.
		return audioPos
	
	# A method to get audio selection. Unlike audio position getter, this one requires display text, as info is not obj.name.
	
	def getAudioSelection(self):
		fg = api.getForegroundObject()
		fgChild = fg.children[1] # Underneath the fg.
		audioSelection = fgChild.children[2].displayText # Audio selection information.
		return audioSelection
	
	# Continuing from above, get marker positions and selection duration. This is a string parsing problem.
	# Store the parsed strings into a list.
	
	def getAudioSelectionParsed(self):
		return self.getAudioSelection().split(" ") # Deal with duration string later.
	
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
	# Based on the constants above and the return value below, get channel information.
	
	def getAudioChannels(self):
		fg = api.getForegroundObject()
		fgChild = fg.children[1] # Underneath the fg.
		audioChannels = fgChild.children[0].displayText # Audio channels.
		return self.audioChannelValues[audioChannels] # This is where dictionaries are convenient.
	
	# Presets window: the various controls for presets are buttons, so let NVDA see them as such.
	
	def event_NVDAObject_init(self, obj):
		if isinstance(obj, Window) and obj.windowClassName == "TBitton":
			obj.role = 9 # Applies to presets control buttons
	
	# Audio editing scripts:
	
	def script_dropStartMarker(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: The start marker position for selecting parts of the audio track (example output: "Start: 0.00").
			marker = _("Start: ") + self.getAudioSelectionParsed()[0]
			speech.speakMessage(marker)
	# Translators: Input help mode message for a Goldwave command.
	script_dropStartMarker.__doc__=_("Drops the start marker and announces start marker position.")
	
	def script_dropFinishMarker(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: The finish marker position for selecting parts of the audio track (example output: "Finish: 5.00").
			marker = _("Finish: ") + self.getAudioSelectionParsed()[2]
			speech.speakMessage(marker)
	# Translators: Input help mode message for a Goldwave command.
	script_dropFinishMarker.__doc__=_("Drops the finish marker and announces finish marker position.")
	
	def script_playSelection(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when selected audio is playing.
			speech.speakMessage(_("Play selection"))
	# Translators: Input help mode message for a Goldwave command.
	script_playSelection.__doc__=_("Plays the trakc between start and finish markers.")
	
	def script_selectAll(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when all parts of the audio track is selected.
			speech.speakMessage(_("Select All"))
	# Translators: Input help mode message for a Goldwave command.
	script_selectAll.__doc__=_("Selects the entire track.")
	
	# Playback and recording:
	
	def script_play(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when a track is playing in Goldwave.
			speech.speakMessage(_("play"))
	# Translators: Input help mode message for a Goldwave command.
	script_play.__doc__=_("Plays the audio track.")
	
	def script_rewind(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when a track is rewinding in Goldwave.
			speech.speakMessage("rewind")
	# Translators: Input help mode message for a Goldwave command.
	script_rewind.__doc__=_("Rewinds through an audio track.")
	
	def script_forward(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when fast forwarding a track in Goldwave.
			speech.speakMessage(_("fast forward"))
	# Translators: Input help mode message for a Goldwave command.
	script_forward.__doc__=_("Fast forwards through an audio track.")
	
	def script_pause(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when pasuing a track in Goldwave.
			speech.speakMessage(_("pause"))
# Translators: Input help mode message for a Goldwave command.	
	script_pause.__doc__=_("Pauses the audio track.")
	
	def script_stop(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when stopping a track in in Goldwave.
			speech.speakMessage(_("stop"))
	# Translators: Input help mode message for a Goldwave command.
	script_stop.__doc__=_("stops the audio track.")
	
	def script_startRecord(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			# Translators: Spoken when starting recording in Goldwave.
			speech.speakMessage(_("record"))
	# Translators: Input help mode message for a Goldwave command.
	script_startRecord.__doc__=_("Starts recording audio.")
	
	# Audio position scripts: markers, selection duration.
	
	def script_announceAudioPosition(self, gesture):
		if self.soundWindow() == 1: # Shouldn't say anything unless in audio editing view.
			curAudioPos = self.getAudioPos()
			speech.speakMessage(curAudioPos) # Remove the tab character before release.
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioPosition.__doc__=_("Announces the current audio position in seconds.")
	
	def script_announceAudioSelection(self, gesture):
		if self.soundWindow() == 1: # Again, just like audio position above.
			audioSelection = self.getAudioSelection() # Parse this string to get individual info such as marker positions.
			# Translators: Spoken when there is no audio selection summary available.
			speech.speakMessage(_("Unable to obtain audio selection summary. Please close and reopen the audio track.")) if audioSelection == "" else speech.speakMessage(audioSelection)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioSelection.__doc__=_("Announces a summary on audio selection info such as selection duration.")
	
	def getTrackLength(self):
		fg = api.getForegroundObject() # A convenient place to start.
		fgChild = fg.children[1] # Underneath the fg.
		trackLength = fgChild.children[1].displayText # Audio selection information.
		return trackLength
	
	def script_announceTrackLength(self, gesture):
		if self.soundWindow() == 1:
			trackLength = self.getTrackLength() # Obtain track length.
			# Translators: Spoken when there is no track length information.
			speech.speakMessage(_("Track length is unavailable. Please close and reopen the audio track.")) if trackLength == "" else speech.speakMessage(trackLength)
	# Translators: Input help mode message for a Goldwave command.
	script_announceTrackLength.__doc__=_("Announces total length of the audio track.")
	
	# Audio channels and zoom level.
	
	def script_announceAudioChannels(self, gesture):
		if self.soundWindow() == 1: # Again, just like audio position above.
			# Translators: Spoken to indicate the selected channel for the track (example output: "Selected channel: mono").
			channel = _("Selected channel: ") + self.getAudioChannels()
			speech.speakMessage(channel)
	# Translators: Input help mode message for a Goldwave command.
	script_announceAudioChannels.__doc__=_("Announces the audio channel you are editing.")
	
	def getZoomLevel(self):
		fg = api.getForegroundObject() # A convenient place to start.
		fgChild = fg.children[2] # Underneath the fg.
		# Translators: Spoken to indicate audio selection zoom level (example output: "Zoom level: 10.000").
		return _("Zoom level: ") + fgChild.children[1].displayText # Zoom level.
	
	def script_announceZoomLevel(self, gesture):
		if self.soundWindow() == 1: # Again, just like audio position above.
			zoomLevel = self.getZoomLevel()
			speech.speakMessage(zoomLevel)
	# Translators: Input help mode message for a Goldwave command.
	script_announceZoomLevel.__doc__=_("Announces audio zoom level.")
	
	def script_changeZoomLevel(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			zoomLevel = self.getZoomLevel()
			speech.speakMessage(zoomLevel)
	# Translators: Input help mode message for a Goldwave command.
	script_changeZoomLevel.__doc__=_("Changes zoom level and announces the new level.")
			
	__gestures={
		"KB:[":"dropStartMarker", "KB:]":"dropFinishMarker",
		"KB:control+a":"selectAll",
		"kB:control+[":"playSelection",
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
		"kb:nvda+shift+p":"announceAudioPosition",
		"kb:control+nvda+3":"announceAudioSelection",
		"kb:control+nvda+2":"announceTrackLength",
		"kb:control+nvda+1":"announceAudioChannels",
		"kb:nvda+shift+z":"announceZoomLevel",
		"kb:shift+uparrow":"changeZoomLevel", "kb:shift+downarrow":"changeZoomLevel", "kb:shift+0":"changeZoomLevel", "kb:shift+1":"changeZoomLevel", "kb:shift+2":"changeZoomLevel", "kb:shift+3":"changeZoomLevel", "kb:shift+4":"changeZoomLevel", "kb:shift+5":"changeZoomLevel", "kb:shift+6":"changeZoomLevel"
	}
	
