-- APFunctions
-- Author: brian
-- DateCreated: 2/17/2025 12:08:04 PM
--------------------------------------------------------------
-- Hello_World
-- Author: brian
-- DateCreated: 1/18/2025 3:44:52 PM
--------------------------------------------------------------
local CLIENT_PREFIX = "APSTART:"
local CLIENT_POSTFIX = ":APEND"

local player = Players[Game.GetActivePlayer()];
local team = Teams[player:GetTeam()];
local teamtechs = team:GetTeamTechs();

function ModIsReady()
	str_to_send = CLIENT_PREFIX .. "True" .. CLIENT_POSTFIX
	print(str_to_send)
end

function AddTech(id)
	team:SetHasTech(id, true);
end

function GetItemsToSend()
	iTechLoop = 0;
	str_to_send = ''
	pTechInfo = GameInfo.Technologies[iTechLoop];

	while( pTechInfo ~= nil ) do
		pTechInfo = GameInfo.Technologies[iTechLoop];
		if teamtechs:HasTech(iTechLoop) then
			str_to_send = str_to_send .. iTechLoop .. ','
			end
		iTechLoop = iTechLoop + 1
	end
	str_to_send = CLIENT_PREFIX .. str_to_send .. CLIENT_POSTFIX
	print(str_to_send)
end

function IsVictory()
	str_to_send = ''
	victory = false
	if(player:GetTeam() == Game:GetWinner()) then
		str_to_send = CLIENT_PREFIX .. "True" .. CLIENT_POSTFIX
		print(str_to_send)
	else
		str_to_send = CLIENT_PREFIX .. "False" .. CLIENT_POSTFIX
		print(str_to_send)
	end
end

function Init()
	i = 0
	for i = 0, GameDefines.MAX_CIV_PLAYERS-1, 1 do
		pPlayer = Players[i]
		pTeam = Teams[pPlayer:GetTeam()]
		if pPlayer:IsHuman() then
			pTeam:SetHasTech(161, true)
		else
			pTeam:SetHasTech(162, true)
		end
	end
end

Init()

Game.ModIsReady = ModIsReady
Game.AddTech = AddTech
Game.GetItemsToSend = GetItemsToSend
Game.IsVictory = IsVictory