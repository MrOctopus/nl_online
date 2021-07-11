;/ Decompiled by Champollion V1.0.1
Source   : SKI_QuestBase.psc
Modified : 2013-03-06 17:33:50
Compiled : 2017-10-03 22:48:11
User     : Sebastian
Computer : SEBASTIAN-PC
/;
scriptName SKI_QuestBase extends Quest hidden

;-- Properties --------------------------------------
Int property CurrentVersion auto hidden

;-- Variables ---------------------------------------

;-- Functions ---------------------------------------

function OnGameReload()

	; Empty function
endFunction

; Skipped compiler generated GetState

function OnVersionUpdateBase(Int a_version)

	; Empty function
endFunction

Int function GetVersion()

	return 1
endFunction

; Skipped compiler generated GotoState

function OnVersionUpdate(Int a_version)

	; Empty function
endFunction

function CheckVersion()

	Int version = self.GetVersion()
	if CurrentVersion < version
		self.OnVersionUpdateBase(version)
		self.OnVersionUpdate(version)
		CurrentVersion = version
	endIf
endFunction
