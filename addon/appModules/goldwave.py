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
	
	def script_dropStartMarker(self, gesture):
		gesture.send()
		speech.speakMessage("Start marked")
	script_dropStartMarker.__doc__="Drops the start marker."
	
	def script_dropFinishMarker(self, gesture):
		gesture.send()
		speech.speakMessage("Finish marked")
	script_dropFinishMarker.__doc__="Drops the finish marker."
	
	def script_playSelection(self, gesture):
		gesture.send()
		speech.speakMessage("Play selection")
	script_playSelection.__doc__="Plays the trakc between start and finish markers."
	
	def script_selectAll(self, gesture):
		gesture.send()
		speech.speakMessage("Select All")
	script_selectAll.__doc__="Selects the entire track."
	
	__gestures={
		"KB:[":"dropStartMarker",
		"KB:]":"dropFinishMarker",
		"KB:control+a":"selectAll",
		"kB:control+[":"playSelection"
	}
	
