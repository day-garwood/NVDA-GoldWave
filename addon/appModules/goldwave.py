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
			speech.speakMessage("command announcement off")
		else:
			self.commandAnnouncement = 1 # Command announcement on.
			speech.speakMessage("command announcement on")
	script_toggleCommandAnnouncement.__doc__="Toggles whether NVDA announces editing commands during audio recording or playback."
	
	# A number of utility functions follows:
	
	def soundWindow(self):
		obj = api.getNavigatorObject()
		return 1 if obj.name != "Workspace" else 0 # For now, nav obj's name is used; may use other attributes later.
	
	# Get audio positions.
	
	def getAudioPos(self):
		# Above the status bar is the audio position and selection info bar. Fetch info from there via object navigation.
		fg = api.getForegroundObject() # A convenient place to start.
		fgChild = fg.children[1] # Underneath the fg.
		audioPos = fgChild.children[3].name # Current cursor position.
		return audioPos
	
	# Presets window: the various controls for presets are buttons, so let NVDA see them as such.
	
	def event_NVDAObject_init(self, obj):
		if isinstance(obj, Window) and obj.windowClassName == "TBitton":
			obj.role = 9 # Applies to presets control buttons.
>>>>>>> presetWindowControls
	
	
	# Audio editing scripts:
	
	def script_dropStartMarker(self, gesture):
		gesture.send()
		# Find out whether we're in the main window or the sound window.
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("Start marked")
	script_dropStartMarker.__doc__="Drops the start marker."
	
	def script_dropFinishMarker(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("Finish marked")
	script_dropFinishMarker.__doc__="Drops the finish marker."
	
	def script_playSelection(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("Play selection")
	script_playSelection.__doc__="Plays the trakc between start and finish markers."
	
	def script_selectAll(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("Select All")
	script_selectAll.__doc__="Selects the entire track."
	
	# Playback and recording:
	
	def script_play(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("play")
	script_play.__doc__="Plays the audio track."
	
	def script_rewind(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("rewind")
	script_rewind.__doc__="Rewinds through an audio track."
	
	def script_forward(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("fast forward")
	script_forward.__doc__="Fast forwards through an audio track."
	
	
	def script_pause(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("pause")
	script_pause.__doc__="Pauses the audio track."
	
	def script_stop(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("stop")
	script_stop.__doc__="stops the audio track."
	
	def script_startRecord(self, gesture):
		gesture.send()
		if self.soundWindow() == 1 and self.commandAnnouncement == 1:
			speech.speakMessage("record")
	script_startRecord.__doc__="Starts recording audio."
	
	# Audio position scripts: markers, selection duration.
	
	def script_announceAudioPosition(self, gesture):
		curAudioPos = self.getAudioPos()
		speech.speakMessage(curAudioPos) # Remove the tab character before beta.
	script_announceAudioPosition.__doc__="Announces the current audio position in seconds."
	
	# A method to get audio selection. Unlike audio position getter, this one requires display text, as info is not obj.name.
	
	def getAudioSelection(self):
		fg = api.getForegroundObject() # A convenient place to start.
		fgChild = fg.children[1] # Underneath the fg.
		audioSelection = fgChild.children[2].displayText # Audio selection information.
		return audioSelection
	
	def script_announceAudioSelection(self, gesture):
		audioSelection = self.getAudioSelection()
		speech.speakMessage(audioSelection)
	script_announceAudioSelection.__doc__="Announces a summary on audio selection info such as selection duration."
	
	
	
	__gestures={
		"KB:[":"dropStartMarker",
		"KB:]":"dropFinishMarker",
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
		"kb:control+nvda+3":"announceAudioSelection"
		
	}
	
