# goldwave/installTasks.py
# Copyright 2022-2025 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import addonHandler
import gui
import winVersion

addonHandler.initTranslation()


def onInstall():
	currentWinVer = winVersion.getWinVer()
	# GoldWave add-on requires Windows 10 21H2 or later.
	minimumWinVer = winVersion.WIN10_21H2
	if currentWinVer < minimumWinVer:
		gui.messageBox(
			_(
				# Translators: Dialog text shown when trying to install the add-on on
				# releases earlier than minimum supported release.
				"You are using {releaseName} ({build}), a Windows release not supported by this add-on.\n"
				"This add-on requires {supportedReleaseName} ({supportedBuild}) or later."
			).format(
				releaseName=currentWinVer.releaseName,
				build=currentWinVer.build,
				supportedReleaseName=minimumWinVer.releaseName,
				supportedBuild=minimumWinVer.build,
			),
			# Translators: dialog title shown when trying to install the add-on in unsupported systems.
			_("Unsupported Windows release"),
		)
		raise RuntimeError("Attempting to install GoldWave add-on on Windows releases earlier than 10")
