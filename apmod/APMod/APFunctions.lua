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
local teamTechs = team:GetTeamTechs();

function printResponse(response)
	print(CLIENT_PREFIX .. response .. CLIENT_POSTFIX)
end

function IsModReady()
	printResponse('{"ready": true}')
end

function GrantTechs(techIds)
	for i, techId in ipairs(techIds) do
		team:SetHasTech(techId, true);
	end
end

function GetItemsToSend()
	techs = {}
	for i=1, 80 do
		if teamTechs:HasTech(i) then
		    table.insert(techs, i)
		end
	end
	printResponse('{"tech": [' .. table.concat(techs, ',') .. ']}')
end

function HasAchievedVictory()
	if(player:GetTeam() == Game:GetWinner()) then
		printResponse('{"victory": true}')
	else
		printResponse('{"victory": false}')
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

Game.IsModReady = IsModReady
Game.GrantTechs = GrantTechs
Game.GetItemsToSend = GetItemsToSend
Game.HasAchievedVictory = HasAchievedVictory