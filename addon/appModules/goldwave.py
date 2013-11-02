# Goldwave App Module
# An add-on for NVDA
# Copyright 2013 Joseph Lee and contributors, released under gPL.
# Functionality is based on JFW scripts for Goldwave by Jim Grimsby, Jr.

import appModuleHandler
import addonHandler
import api
import speech # No need for braille yet.
from logHandler import log
addonHandler.initTranslation()
import scriptHandler

class AppModule(appModuleHandler.AppModule):
	
	# A number of utility functions follows:
	
	def soundWindow(self):
		obj = api.getNavigatorObject()
		return 1 if obj.name != "Workspace" else 0 # For now, nav obj's name is used; may use other attributes later.
	
	# Audio editing scripts:
	
	def script_dropStartMarker(self, gesture):
		gesture.send()
		# Find out whether we're in the main window or the sound window.
		if self.soundWindow() == 1:
			speech.speakMessage("Start marked")
	script_dropStartMarker.__doc__="Drops the start marker."
	
	def script_dropFinishMarker(self, gesture):
		gesture.send()
		if self.soundWindow() == 1: # Are we?
			speech.speakMessage("Finish marked")
	script_dropFinishMarker.__doc__="Drops the finish marker."
	
	def script_playSelection(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("Play selection")
	script_playSelection.__doc__="Plays the trakc between start and finish markers."
	
	def script_selectAll(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("Select All")
	script_selectAll.__doc__="Selects the entire track."
	
	# Playback and recording:
	
	def script_play(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("play")
	script_play.__doc__="Plays the audio track."
	
	def script_rewind(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("rewind")
	script_rewind.__doc__="Rewinds through an audio track."
	
	def script_forward(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("fast forward")
	script_forward.__doc__="Fast forwards through an audio track."
	
	
	def script_pause(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("pause")
	script_pause.__doc__="Pauses the audio track."
	
	def script_stop(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("stop")
	script_stop.__doc__="stops the audio track."
	
	def script_startRecord(self, gesture):
		gesture.send()
		if self.soundWindow() == 1:
			speech.speakMessage("record")
	script_startRecord.__doc__="Starts recording audio."
	
	
		
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
		"kb:control+f9":"startRecord"
		
	}
	
