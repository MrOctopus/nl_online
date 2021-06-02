;/ Decompiled by Champollion V1.0.1
Source   : SKI_QF_ConfigManagerInstance.psc
Modified : 2013-03-06 17:26:06
Compiled : 2017-10-03 22:48:11
User     : Sebastian
Computer : SEBASTIAN-PC
/;
scriptName SKI_QF_ConfigManagerInstance extends Quest hidden

;-- Properties --------------------------------------
referencealias property Alias_PlayerRef auto

;-- Variables ---------------------------------------

;-- Functions ---------------------------------------

function Fragment_0()

	Quest __temp = self as Quest
	ski_configmanager kmyQuest = __temp as ski_configmanager
	kmyQuest.ForceReset()
endFunction

; Skipped compiler generated GetState

; Skipped compiler generated GotoState
