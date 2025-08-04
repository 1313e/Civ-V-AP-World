local CLIENT_PREFIX = "APSTART:"
local CLIENT_POSTFIX = ":APEND"
local LOWER_POLICY_BRANCH_ID = 0
local UPPER_POLICY_BRANCH_ID = 8
local POLICY_BRANCH_FINISHER_OFFSET = 12
local LOWER_POLICY_ID = 111
local UPPER_POLICY_ID = 156
local LOWER_TECH_ID = 83
local UPPER_TECH_ID = 168

local player = Players[Game.GetActivePlayer()];
local team = Teams[player:GetTeam()];
local teamTechs = team:GetTeamTechs();

local pushTable = {}
local pushTableTableKeys = {policy=true, policy_branch=true, tech=true}
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
	[1]=1,
	[2]=1,
	[3]=1,
	[4]=1,
	[5]=1,
}


-- EVENTS
function OnPolicyAdopted(playerId, policyId)
    -- If the player gets a policy, add it to the push table
    if(playerId == player:GetID() and policyBranchId >= LOWER_POLICY_ID and policyBranchId <= UPPER_POLICY_ID) then
        table.insert(pushTable["policy"], policyId)

		-- If the player finished the branch with this policy, add branch finisher to the push table
		if(player:GetNumPoliciesInBranch(policyIdToPolicyBranchId[policyId]) == 5) then
			table.insert(pushTable["policy_branch"], policyIdToPolicyBranchId[policyId]+POLICY_BRANCH_FINISHER_OFFSET)
		end
    end
end

function OnPolicyBranchAdopted(playerId, policyBranchId)
    -- If the player adopts a policy branch, add it to the push table
    if(playerId == player:GetID() and policyBranchId >= LOWER_POLICY_BRANCH_ID and policyBranchId <= UPPER_POLICY_BRANCH_ID) then
        table.insert(pushTable["policy_branch"], policyBranchId)
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
		-- This avoids the policy culture cost going up when receiving checks
		-- For whatever reason, the following marks the next policy granted as free
		if(policyId <= LOWER_POLICY_ID) then
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
	--InitPushTable()
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
Game.GetPushTable = GetPushTable