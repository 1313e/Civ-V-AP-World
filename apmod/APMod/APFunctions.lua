local CLIENT_PREFIX = "APSTART:"
local CLIENT_POSTFIX = ":APEND"
local LOWER_POLICY_BRANCH_ID = 0
local UPPER_POLICY_BRANCH_ID = 8
local POLICY_BRANCH_FINISHER_OFFSET = 12
local LOWER_POLICY_ID = 111
local UPPER_POLICY_ID = 155
local LOWER_TECH_ID = 83
local UPPER_TECH_ID = 168

local player = Players[Game.GetActivePlayer()];
local team = Teams[player:GetTeam()];
local teamTechs = team:GetTeamTechs();
local maxNumberOfTeams = 22;

local pushTable = {}
local pushTableTableKeys = {policy=true, policy_branch=true, tech=true, national_wonder=true, world_wonder=true}
local techIdsToEraIds = {
	[0]=0, [1]=0, [2]=0, [3]=0, [4]=0, [5]=0, [6]=0, [7]=0, [8]=0, [9]=0, [10]=0, [11]=0,
	[12]=1, [13]=1, [14]=1, [15]=1, [16]=1, [17]=1, [18]=1, [19]=1, [20]=1,
	[21]=2, [22]=2, [23]=2, [24]=2, [25]=2, [26]=2, [27]=2, [28]=2, [29]=2, [30]=2,
	[31]=3, [32]=3, [33]=3, [34]=3, [35]=3, [36]=3, [37]=3, [38]=3, [39]=3, [40]=3,
	[41]=4, [42]=4, [43]=4, [44]=4, [45]=4, [46]=4, [47]=4, [48]=4, [49]=4, [50]=4,
	[51]=5, [52]=5, [53]=5, [54]=5, [55]=5, [56]=5, [57]=5, [58]=5, [59]=5,
	[60]=6, [61]=6, [62]=6, [63]=6, [64]=6, [65]=6, [66]=6, [67]=6,
	[68]=7, [69]=7, [70]=7, [71]=7, [72]=7, [73]=7, [74]=7, [75]=7, [76]=7, [77]=7, [78]=7, [79]=7, [80]=7,
}
local policyIdToPolicyBranchId = {
	[7]=0, [8]=0, [9]=0, [10]=0, [11]=0, [111]=0, [112]=0, [113]=0, [114]=0, [115]=0,
	[1]=1, [2]=1, [3]=1, [4]=1, [5]=1, [116]=1, [117]=1, [118]=1, [119]=1, [120]=1,
	[13]=2, [14]=2, [15]=2, [16]=2, [17]=2, [121]=2, [122]=2, [123]=2, [124]=2, [125]=2,
	[19]=3, [20]=3, [21]=3, [22]=3, [23]=3, [126]=3, [127]=3, [128]=3, [129]=3, [130]=3,
	[25]=4, [26]=4, [27]=4, [28]=4, [29]=4, [131]=4, [132]=4, [133]=4, [134]=4, [135]=4,
	[50]=5, [51]=5, [52]=5, [53]=5, [54]=5, [136]=5, [137]=5, [138]=5, [139]=5, [140]=5,
	[31]=6, [32]=6, [33]=6, [34]=6, [35]=6, [141]=6, [142]=6, [153]=6, [144]=6, [145]=6,
	[57]=7, [58]=7, [59]=7, [60]=7, [61]=7, [146]=7, [147]=7, [148]=7, [149]=7, [150]=7,
	[37]=8, [38]=8, [39]=8, [40]=8, [41]=8, [151]=8, [152]=8, [153]=8, [154]=8, [155]=8,
}
local policyBranchIdToAPPolicyIds = {
	[0]={111, 112, 113, 114, 115},
	[1]={116, 117, 118, 119, 120},
	[2]={121, 122, 123, 124, 125},
	[3]={126, 127, 128, 129, 130},
	[4]={131, 132, 133, 134, 135},
	[5]={136, 137, 138, 139, 140},
	[6]={141, 142, 143, 144, 145},
	[7]={146, 147, 148, 149, 150},
	[8]={151, 152, 153, 154, 155},
}
local policyBranchIdToPolicyBranchStarterId ={
	[0]=6, [1]=0, [2]=12, [3]=18, [4]=24, [5]=49, [6]=30, [7]=56, [8]=36,
}
local policyBranchIdToPolicyBranchFinisherId = {
	[0]=42, [1]=43, [2]=44, [3]=45, [4]=46, [5]=55, [6]=47, [7]=62, [8]=48,
}
local nationalWonderBuildingIds = {
	[55]=true, [56]=true, [57]=true, [58]=true, [59]=true, [60]=true,
	[61]=true, [62]=true,
	[127]=true,
	[141]=true, [142]=true, [148]=true, [149]=true, [150]=true,
}
local worldWonderBuildingIds = {
	[63]=true, [64]=true, [65]=true, [66]=true, [67]=true, [68]=true, [69]=true, [70]=true,
	[71]=true, [72]=true, [73]=true, [74]=true, [75]=true, [76]=true, [77]=true, [78]=true, [79]=true, [80]=true,
	[81]=true, [82]=true, [83]=true, [84]=true, [85]=true, [86]=true, [87]=true, [88]=true, [90]=true,
	[93]=true, [94]=true, [95]=true,
	[128]=true, [129]=true, [130]=true,
	[131]=true, [132]=true, [133]=true, [134]=true, [135]=true, [136]=true,
	[154]=true, [155]=true, [156]=true, [157]=true, [158]=true, [159]=true, [160]=true,
	[161]=true,
}


-- EVENTS
function OnPolicyAdopted(playerId, policyId)
    -- If the player gets a policy, add it to the push table
    if(playerId == player:GetID() and policyId >= LOWER_POLICY_ID and policyId <= UPPER_POLICY_ID) then
        table.insert(pushTable["policy"], policyId)

		-- If the player finished the branch with this policy, add branch finisher to the push table
		policyBranchId = policyIdToPolicyBranchId[policyId]
		for _, apPolicyId in ipairs(policyBranchIdToAPPolicyIds[policyBranchId]) do
			if not player:HasPolicy(apPolicyId) then
				return
			end
		end
		table.insert(pushTable["policy_branch"], policyBranchId+POLICY_BRANCH_FINISHER_OFFSET)
    end

	-- If the AI finished the branch with this policy, grant them the branch finisher
	if(playerId ~= player:GetID()) then
		aiPlayer = Players[playerId]
		policyBranchId = policyIdToPolicyBranchId[policyId]
		if(aiPlayer:GetNumPoliciesInBranch(policyBranchId) == 5) then
			aiPlayer:SetHasPolicy(policyBranchIdToPolicyBranchFinisherId[policyBranchId], true)
		end
	end
end

function OnPolicyBranchAdopted(playerId, policyBranchId)
	-- If one of the default 9 branches was adopted
	if(policyBranchId >= LOWER_POLICY_BRANCH_ID and policyBranchId <= UPPER_POLICY_BRANCH_ID) then
		-- If the player adopts a policy branch, add it to the push table
		if(playerId == player:GetID()) then
			table.insert(pushTable["policy_branch"], policyBranchId)

		-- Else, grant the AI the branch starter
		else
			Players[playerId]:SetHasPolicy(policyBranchIdToPolicyBranchStarterId[policyBranchId], true)
		end
	end
end

function OnTechAcquired(playerId, techId)
	-- If the player gets an AP tech, add it to the push table
	if(playerId == player:GetID() and techId >= LOWER_TECH_ID and techId <= UPPER_TECH_ID) then
		table.insert(pushTable["tech"], techId)
	end

	-- If the AI gets a non-AP tech that should have given access to the next era, grant that
	if(playerId ~= player:GetID() and techId < LOWER_TECH_ID-2) then
		aiTeam = Teams[Players[playerId]:GetTeam()]
		if(aiTeam:GetCurrentEra() < techIdsToEraIds[techId]) then
			aiTeam:SetCurrentEra(techIdsToEraIds[techId])
		end
	end
end

function OnCityBuildingConstructed(playerId, cityId, buildingId, gold, faithOrCulture)
	-- If the player constructs a building, add it to the push table if it is a wonder
	if(playerId == player:GetID()) then
		if(nationalWonderBuildingIds[buildingId]) then
			table.insert(pushTable["national_wonder"], buildingId)
		elseif(worldWonderBuildingIds[buildingId]) then
			table.insert(pushTable["world_wonder"], buildingId)
		end
	end
end

function OnEndGameShow(endGameType, teamId)
	-- If the player's team wins, add that to the push table
	if(teamId == player:GetTeam()) then
		pushTable["victory"] = true
	end
end


-- CALLABLES
function printResponse(response)
	-- Define format for all function responses
	print(CLIENT_PREFIX .. response .. CLIENT_POSTFIX)
end

function IsModReady()
	-- If this function can be reached and executed, the APMod is ready
	printResponse('{"ready": true}')
end

function GrantPolicies(policyIds)
	-- Grant all given policy IDs to the player
	for _, policyId in ipairs(policyIds) do
		-- If this policy is a non-AP policy, we want to give it to the player for free
		-- This avoids the policy culture cost going up when receiving policy items
		-- For whatever reason, the following marks the next policy granted as free
		if(policyId < LOWER_POLICY_ID) then
			player:ChangeNumFreePolicies(1);
			player:ChangeNumFreePolicies(-1);
		end
		player:SetHasPolicy(policyId, true);
	end
end

function UnlockPolicyBranches(policyBranchIds)
	-- Unlock all given policy branch IDs for the player
	-- This is only used for syncing
	for _, policyBranchId in ipairs(policyBranchIds) do
		player:SetPolicyBranchUnlocked(policyBranchId, true);
	end
end

function GrantTechs(techIds)
	-- Grant all given tech IDs to the player
	for _, techId in ipairs(techIds) do
		team:SetHasTech(techId, true);
	end
end

function ChangeGold(value)
	-- Change gold for player by given value
	player:ChangeGold(value)
end

function ChangeCulture(value)
	-- Change culture for player by given value
	player:ChangeJONSCulture(value)
end

function ChangeFaith(value)
	-- Change faith for player by given value
	player:ChangeFaith(value)
end

function ChangeNumFreeGreatPeople(value)
	-- Change number of free people to choose for player by given value
	player:ChangeNumFreeGreatPeople(value)
end

function ChangeNumFreePolicies(value)
	-- Change number of free policies to choose for player by given value
	player:ChangeNumFreePolicies(value)
end

function ChangeNumFreeTechs(value)
	-- Change number of free people to choose for player by given value
	player:SetNumFreeTechs(player:GetNumFreeTechs()+value)
	player:AddNotification(NotificationTypes.NOTIFICATION_FREE_TECH, "You may choose a free Tech!")
end

function ChangeNewCityExtraPopulation(value)
	-- Change the extra population a new city is given for the player by given value
	player:ChangeNewCityExtraPopulation(value)
end

function ChangeCulturePerTurnForFree(value)
	-- Change the amount of free culture the player gets per turn by given value
	player:ChangeJONSCulturePerTurnForFree(value)
end

function ChangeExtraHappinessPerCity(value)
	-- Change the amount of extra happiness the player gets per city by given value
	player:ChangeExtraHappinessPerCity(value)
end

function StartGoldenAge(n)
	-- Immediately start a golden age for the player n times
	for _=1, n do
		player:ChangeGoldenAgeTurns(player:GetGoldenAgeLength())
	end
end

function DeclareWarRandom(n)
	-- Get the IDs of all teams that are still alive that are not the player
	aiTeamIds = {}
	for i=1, maxNumberOfTeams-1 do
		if Teams[i]:IsAlive() then
			table.insert(aiTeamIds, i)
		end
	end

	-- Pick n times a random team that declares war on the player
	for _=1, n do
		Teams[aiTeamIds[math.random(1, #aiTeamIds)]]:DeclareWar(team:GetID())
	end
end

function InitPushTable()
	-- Empty the table
	for key, _ in pairs(pushTable) do
		pushTable[key] = nil
	end

	-- Init all keys that should be tables
	for key, _ in pairs(pushTableTableKeys) do
		pushTable[key] = {}
	end
end

function GetPushTable()
	-- Loop over all pairs in the push table
	jsonStrings = {}
	for key, value in pairs(pushTable) do
		-- If this key is another table, add as JSON array
		if(pushTableTableKeys[key]) then
			table.insert(jsonStrings, table.concat({'"', key, '": [', table.concat(value, ","), "]"}))

		-- If this key is a string, add it as a scalar with surrounding quotations
		elseif(type(value) == "string") then
			table.insert(jsonStrings, table.concat({'"', key, '": "', value, '"'}))

		-- Else, add the value as a scalar as is
		else
			table.insert(jsonStrings, table.concat({'"', key, '": ', tostring(value)}))
		end
	end

	-- Print the response as a single JSON object and reset the push table
	printResponse(table.concat({"{", table.concat(jsonStrings, ","), "}"}))
	InitPushTable()
end

function RequestSync()
	-- Request the syncing of all locations
	pushTable["sync"] = true

	-- Add all adopted policies to the push table
	for i=LOWER_POLICY_ID, UPPER_POLICY_ID do
		if player:HasPolicy(i) then
			table.insert(pushTable["policy"], i)
		end
	end

	-- Add all unlocked and finished policy branches to the push table
	for i=LOWER_POLICY_BRANCH_ID, UPPER_POLICY_BRANCH_ID do
		if player:IsPolicyBranchUnlocked(i) then
			table.insert(pushTable["policy_branch"], i)
			if player:IsPolicyBranchFinished(i) then
				table.insert(pushTable["policy_branch"], i+POLICY_BRANCH_FINISHER_OFFSET)
			end
		end
	end

	-- Add all researched technologies to the push table
	for i=LOWER_TECH_ID, UPPER_TECH_ID do
		if teamTechs:HasTech(i) then
		    table.insert(pushTable["tech"], i)
		end
	end
end


-- INIT FUNCTION
function Init()
	-- Register event function
	Events.TechAcquired.Add(OnTechAcquired)
	Events.EndGameShow.Add(OnEndGameShow)
	GameEvents.PlayerAdoptPolicy.Add(OnPolicyAdopted)
	GameEvents.PlayerAdoptPolicyBranch.Add(OnPolicyBranchAdopted)
	GameEvents.CityConstructed.Add(OnCityBuildingConstructed)

	-- Give player and AI their corresponding modified techs at the start
	for i = 0, GameDefines.MAX_CIV_PLAYERS-1, 1 do
		pPlayer = Players[i]
		pTeam = Teams[pPlayer:GetTeam()]
		if pPlayer:IsHuman() then
			pTeam:SetHasTech(81, true)
		else
			pTeam:SetHasTech(82, true)
		end
	end

	-- Initialize pushTable
	InitPushTable()

	-- Request a sync between game and client
	RequestSync()
	
	-- Send notification to player that APMod was loaded successfully
	player:AddNotification(NotificationTypes.NOTIFICATION_GENERIC, "APMod was loaded successfully", "APMod loaded")
end

Init()

Game.IsModReady = IsModReady
Game.GrantTechs = GrantTechs
Game.GrantPolicies = GrantPolicies
Game.UnlockPolicyBranches = UnlockPolicyBranches
Game.ChangeGold = ChangeGold
Game.ChangeCulture = ChangeCulture
Game.ChangeFaith = ChangeFaith
Game.ChangeNumFreeGreatPeople = ChangeNumFreeGreatPeople
Game.ChangeNumFreePolicies = ChangeNumFreePolicies
Game.ChangeNumFreeTechs = ChangeNumFreeTechs
Game.ChangeNewCityExtraPopulation = ChangeNewCityExtraPopulation
Game.ChangeCulturePerTurnForFree = ChangeCulturePerTurnForFree
Game.ChangeExtraHappinessPerCity = ChangeExtraHappinessPerCity
Game.ChangeCulturePerTurnForFree = ChangeCulturePerTurnForFree
Game.StartGoldenAge = StartGoldenAge
Game.DeclareWarRandom = DeclareWarRandom
Game.GetPushTable = GetPushTable