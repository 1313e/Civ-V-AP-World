include( "SaveUtils" ); MY_MOD_NAME = "APMod";
include( "json" );

AP = {}
Game.AP = AP

local CLIENT_PREFIX = "APSTART:"
local CLIENT_POSTFIX = ":APEND"
local LOWER_POLICY_BRANCH_ID = 0
local UPPER_POLICY_BRANCH_ID = 8
local POLICY_BRANCH_FINISHER_OFFSET = 12
local LOWER_POLICY_ID = 111
local UPPER_POLICY_ID = 155
local LOWER_PROMOTION_ID = 229
local UPPER_PROMOTION_ID = 311
local LOWER_TECH_ID = 83
local UPPER_TECH_ID = 168
local LOWER_TEAM_ID = 0
local UPPER_TEAM_ID = 62
local BASE_CULTURE_TECH_YIELD = 1800

local player = Players[Game.GetActivePlayer()]
local team = Teams[player:GetTeam()]

local optionsTable = {
    promotion_sanity=false, satellites_meets_all=nil, settler_sanity=false, settler_sanity_amount=0,
}
local pushTable = {}
local pushTableTableKeys = {
    building=true, national_wonder=true, policy=true, policy_branch=true, promotion=true, settler=true, tech=true,
    unit=true, world_wonder=true,
}
local textInfoTableNames = {
    building="Buildings", national_wonder="Buildings", policy=nil, policy_branch=nil, promotion="UnitPromotions",
    settler="Units", tech=nil, unit="Units", world_wonder="Buildings",
}
local freePoliciesToGrant = 0
local itemTable = {}
local locationTable = {}
for key, _ in pairs(pushTableTableKeys) do
    locationTable[key] = {}
end
local promotionTable = {}
local techIdToEraId = {
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
local policyBranchIdToEraId = {
    [0]=0, [1]=1, [2]=2, [3]=3, [4]=4, [5]=5, [6]=6, [7]=7, [8]=7,
}
local policyBranchIdToPolicyBranchStarterId = {
    [0]=6, [1]=0, [2]=12, [3]=18, [4]=24, [5]=49, [6]=30, [7]=56, [8]=36,
}
local policyBranchIdToPolicyBranchFinisherId = {
    [0]=42, [1]=43, [2]=44, [3]=45, [4]=46, [5]=55, [6]=47, [7]=62, [8]=48,
}
local buildingIds = {
    [11]=true, [12]=true, [13]=true, [14]=true, [15]=true, [16]=true, [17]=true, [18]=true, [19]=true,
    [20]=true, [22]=true, [23]=true, [24]=true, [25]=true, [26]=true, [27]=true, [28]=true, [29]=true,
    [30]=true, [31]=true, [32]=true, [33]=true, [34]=true, [35]=true, [36]=true, [37]=true, [38]=true, [39]=true,
    [40]=true, [41]=true, [42]=true, [43]=true, [44]=true, [45]=true, [46]=true, [47]=true, [48]=true, [49]=true,
    [50]=true, [51]=true, [52]=true, [53]=true,
    [91]=true, [92]=true,
    [121]=true, [122]=true, [123]=true, [124]=true, [125]=true, [126]=true,
    [151]=true, [152]=true, [153]=true,
}
local civUniqueBuildingIdToBuildingId = {
    [0]=13, [2]=38, [3]=33, [4]=43, [5]=47, [6]=48, [7]=50, [8]=51, [9]=29,
    [10]=29,
    [96]=37,
    [116]=30, [117]=16, [119]=122,
    [140]=28, [143]=33, [144]=12, [145]=50, [146]=22, [147]=48,
}
local nationalWonderBuildingIds = {
    [55]=true, [56]=true, [57]=true, [58]=true, [59]=true,
    [60]=true, [61]=true, [62]=true,
    [127]=true,
    [141]=true, [142]=true, [148]=true, [149]=true,
    [150]=true,
}
local worldWonderBuildingIds = {
    [63]=true, [64]=true, [65]=true, [66]=true, [67]=true, [68]=true, [69]=true,
    [70]=true, [71]=true, [72]=true, [73]=true, [74]=true, [75]=true, [76]=true, [77]=true, [78]=true, [79]=true,
    [80]=true, [81]=true, [82]=true, [83]=true, [84]=true, [85]=true, [86]=true, [87]=true, [88]=true,
    [90]=true, [93]=true, [94]=true, [95]=true,
    [128]=true, [129]=true,
    [130]=true, [131]=true, [132]=true, [133]=true, [134]=true, [135]=true, [136]=true,
    [154]=true, [155]=true, [156]=true, [157]=true, [158]=true, [159]=true,
    [160]=true, [161]=true,
}
local worldWonderIdToFreeBuildingId = {
    [63]=23, [65]=50, [69]=22,
    [70]=37, [72]=29, [77]=38,
    [128]=38, [129]=32,
    [130]=46,
}
local unitIds = {
    [0]=true, [1]=true, [2]=true,
    [12]=true, [13]=true, [14]=true, [15]=true, [16]=true, [17]=true, [18]=true, [19]=true,
    [21]=true, [22]=true, [23]=true, [24]=true, [25]=true, [26]=true, [27]=true, [28]=true, [29]=true,
    [30]=true, [31]=true, [32]=true, [33]=true, [34]=true, [36]=true, [38]=true, [39]=true,
    [41]=true, [42]=true, [43]=true, [44]=true, [46]=true, [48]=true, [49]=true,
    [51]=true, [52]=true, [56]=true, [58]=true, [59]=true,
    [63]=true, [66]=true, [67]=true, [68]=true,
    [70]=true, [72]=true, [75]=true, [78]=true,
    [81]=true, [82]=true, [83]=true,
    [130]=true, [131]=true, [132]=true, [133]=true, [134]=true, [135]=true, [136]=true, [137]=true, [138]=true,
    [141]=true, [145]=true, [146]=true, [149]=true,
    [157]=true,
    [161]=true,
}
local civUniqueUnitIdToUnitId = {
    [20]=19,
    [35]=34, [37]=36,
    [40]=39, [47]=46,
    [50]=49, [53]=52, [54]=52, [55]=52, [57]=56,
    [60]=59, [61]=59, [62]=59, [64]=63, [65]=63, [69]=68,
    [71]=70, [73]=72, [74]=72, [76]=75, [77]=75, [79]=78,
    [80]=78, [84]=83,
    [90]=59, [92]=81, [93]=52, [94]=59, [95]=83, [96]=56, [97]=48, [98]=21, [99]=58,
    [100]=81, [102]=78, [103]=81, [105]=70, [106]=70, [107]=22, [108]=75, [109]=46,
    [110]=48,
    [120]=48, [121]=49, [122]=78, [124]=138,
    [142]=66, [144]=49,
    [150]=68, [151]=44, [152]=21, [153]=46, [154]=131, [155]=82, [156]=46, [158]=72,
}
local unitIdToObsoleteTechId = {
    [16]=68, [18]=59, [19]=57,
    [20]=57, [21]=49, [22]=31,
    [42]=66, [44]=69, [45]=56, [46]=59, [47]=59, [48]=53, [49]=63,
    [50]=63, [51]=50, [52]=44, [53]=44, [54]=44, [55]=44, [56]=35, [57]=44, [58]=40, [59]=45,
    [60]=45, [61]=45, [62]=45, [63]=43, [64]=43, [65]=43, [66]=39, [68]=29, [69]=29,
    [70]=27, [71]=27, [72]=30, [73]=35, [74]=35, [75]=27, [76]=27, [77]=27, [78]=22, [79]=22,
    [80]=22, [81]=15, [82]=42, [83]=24, [84]=24,
    [90]=45, [92]=15, [93]=44, [94]=45, [95]=24, [96]=39, [97]=53, [98]=53, [99]=40,
    [100]=15, [102]=22, [103]=15, [104]=31, [105]=27, [106]=27, [107]=31, [108]=27, [109]=59,
    [110]=53,
    [120]=53, [121]=63, [122]=29, [124]=59,
    [130]=28, [131]=36, [132]=56, [134]=62, [135]=62, [136]=63, [137]=65, [138]=59,
    [141]=58, [142]=44, [144]=63,
    [150]=29, [151]=69, [152]=49, [153]=59, [154]=36, [155]=42, [156]=59, [158]=30,
}
local textInfoLinkedIds = {
    Buildings={
        [12]={144}, [13]={0}, [16]={117},
        [22]={146}, [28]={140}, [29]={9, 10},
        [30]={116}, [33]={3, 143}, [37]={96}, [38]={2},
        [43]={4}, [47]={5}, [48]={6, 147},
        [50]={7, 145}, [51]={8},
        [122]={119},
    },
    Units={
        [19]={20},
        [21]={98, 152}, [22]={107},
        [34]={35}, [36]={37}, [39]={40},
        [44]={151}, [46]={47, 109, 153, 156}, [48]={97, 110, 120}, [49]={50, 121, 144},
        [52]={53, 54, 55, 93}, [56]={57, 96}, [58]={99}, [59]={60, 61, 62, 90, 94},
        [63]={64, 65}, [66]={142}, [68]={69, 150},
        [70]={71, 105, 106}, [72]={73, 74, 158}, [75]={76, 77, 108}, [78]={79, 80, 102, 122},
        [81]={92, 100, 103}, [82]={155}, [83]={84, 95},
        [131]={154}, [138]={124},
    },
}
local notificationTypes = {
    [0]=NotificationTypes.NOTIFICATION_GENERIC,		-- generic
    [1]=NotificationTypes.NOTIFICATION_CITY_GROWTH,	-- positive
    [2]=NotificationTypes.NOTIFICATION_STARVING,	-- negative
}
local cultureTechYieldSpeedModifier = {
    [0]=3, [1]=1.5, [2]=1, [3]=0.67
}
local cultureTechYieldDifficultyModifier = {
    [0]=0.5, [1]=0.67, [2]=0.85, [3]=1, [4]=1, [5]=1, [6]=1, [7]=1,
}
local cultureTechYield = 0


-- EVENTS
function OnPolicyAdopted(playerId, policyId)
    -- If the player gets a policy, send it
    if(playerId == player:GetID() and policyId >= LOWER_POLICY_ID and policyId <= UPPER_POLICY_ID) then
        SendLocation("policy", policyId)

        -- If the player finished the branch with this policy, send branch finisher location
        policyBranchId = policyIdToPolicyBranchId[policyId]
        for _, apPolicyId in ipairs(policyBranchIdToAPPolicyIds[policyBranchId]) do
            if not player:HasPolicy(apPolicyId) then
                return
            end
        end
        SendLocation("policy_branch", policyBranchId+POLICY_BRANCH_FINISHER_OFFSET)
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
        -- If the player adopts a policy branch, send it
        if(playerId == player:GetID()) then
            SendLocation("policy_branch", policyBranchId)

            -- Else, grant the AI the branch starter
        else
            Players[playerId]:SetHasPolicy(policyBranchIdToPolicyBranchStarterId[policyBranchId], true)
        end
    end
end

function OnTechAcquired(playerId, techId)
    -- If the player received this tech
    if playerId == player:GetID() then
        -- If the player gets an AP tech, send it
        if(techId >= LOWER_TECH_ID and techId <= UPPER_TECH_ID) then
            SendLocation("tech", techId)

            -- Upon acquiring Satellites, make sure the player's team discovers/meets all other teams
        elseif(techId == 71 and optionsTable["satellites_meets_all"]) then
            for i=LOWER_TEAM_ID, UPPER_TEAM_ID do
                team:Meet(i)
            end

            -- Upon acquiring Industrial Era, if player has not founded a religion yet, provide player with a free Great Prophet
        elseif(techId == 172 and not player:HasCreatedReligion()) then
            player:AddFreeUnit(128)

            -- Upon acquiring Culture Boost, grant culture to player
        elseif(techId == 176) then
            AP.ChangeCulture(cultureTechYield)
        end
    end

    -- If the AI gets a non-AP tech that should have given access to the next era, grant that
    if(playerId ~= player:GetID() and techId < LOWER_TECH_ID-2) then
        aiTeam = Teams[Players[playerId]:GetTeam()]
        if(aiTeam:GetCurrentEra() < techIdToEraId[techId]) then
            aiTeam:SetCurrentEra(techIdToEraId[techId])
        end
    end
end

function OnCityBuildingConstructed(playerId, cityId, buildingId, gold, faithOrCulture)
    -- If the player constructs a building, send it if it is a supported building
    if(playerId == player:GetID()) then
        -- Standard buildings
        if(buildingIds[buildingId]) then
            SendLocation("building", buildingId)

            -- Civ-unique buildings
        elseif(civUniqueBuildingIdToBuildingId[buildingId] ~= nil) then
            SendLocation("building", civUniqueBuildingIdToBuildingId[buildingId])

            -- National Wonders
        elseif(nationalWonderBuildingIds[buildingId]) then
            SendLocation("national_wonder", buildingId)

            -- World Wonders
        elseif(worldWonderBuildingIds[buildingId]) then
            SendLocation("world_wonder", buildingId)

            -- If this world wonder provides a free building, send it as well
            if(worldWonderIdToFreeBuildingId[buildingId] ~= nil) then
                SendLocation("building", worldWonderIdToFreeBuildingId[buildingId])
            end
        end
    end
end

function OnCityCaptured(playerId, isCapital, plotX, plotY, newPlayerId)
    -- If the player captures a city, check it for any world wonders and send them
    if(newPlayerId == player:GetID()) then
        city = Map.GetPlot(plotX, plotY):GetPlotCity()
        for i, _ in pairs(worldWonderBuildingIds) do
            if city:IsHasBuilding(i) then
                SendLocation("world_wonder", i)
            end
        end
    end
end

function OnCityUnitTrained(playerId, cityId, unitId, gold, faithOrCulture)
    -- If the player trains a unit, send it if it is a supported unit
    if(playerId == player:GetID()) then
        -- Given unitId is the ID of the unit instance. Convert to the ID of its type
        unit = player:GetUnitByID(unitId)
        unitId = unit:GetUnitType()

        -- If the unit is a settler and settler sanity is turned on, remove unit immediately and send as location
        if(unitId == 0 and optionsTable["settler_sanity"]) then
            unit:Kill(false)
            SendLocation("settler", #locationTable["settler"]+1, 0)

        -- Standard units
        elseif(unitIds[unitId]) then
            SendLocation("unit", unitId)

        -- Civ-unique units
        elseif(civUniqueUnitIdToUnitId[unitId] ~= nil) then
            SendLocation("unit", civUniqueUnitIdToUnitId[unitId])
        end
    end
end

function OnCityCanTrain(playerId, cityId, unitId)
    -- If settler sanity is on, settlers may not be trained by the player if maximum has been reached
    if(playerId == player:GetID()
            and unitId == 0
            and optionsTable["settler_sanity"]
            and #locationTable["settler"] == optionsTable["settler_sanity_amount"]) then
        return false

    -- If the AI has the tech that makes this unit obsolete, unit cannot be trained
    elseif(playerId ~= player:GetID()
            and unitIdToObsoleteTechId[unitId] ~= nil
            and Teams[Players[playerId]:GetTeam()]:IsHasTech(unitIdToObsoleteTechId[unitId])) then
        return false
    end

    -- In all other cases, unit can be trained
    return true
end

function OnUnitPromoted(playerId, unitId, promotionId)
    -- If the player received this promotion and it is an earnable promotion, send it
    if(playerId == player:GetID() and optionsTable["promotion_sanity"]
            and (promotionId >= LOWER_PROMOTION_ID and promotionId <= UPPER_PROMOTION_ID)) then
        SendLocation("promotion", promotionId)
    end
end

function OnUnitUpgraded(playerId, oldUnitId, unitId, goodyHut)
    -- If the player upgrades a unit to a new unit without using a goody hut, send it if it is a supported unit
    if(playerId == player:GetID() and not goodyHut) then
        -- Given unitId is the ID of the unit instance. Convert to the ID of its type
        unit = player:GetUnitByID(unitId)
        unitId = unit:GetUnitType()

        -- Standard units
        if(unitIds[unitId]) then
            SendLocation("unit", unitId)

        -- Civ-unique units
        elseif(civUniqueUnitIdToUnitId[unitId] ~= nil) then
            SendLocation("unit", civUniqueUnitIdToUnitId[unitId])
        end
    end
end

function OnNotificationAdded(notification, notificationType, toolTip, summary, gameValue, extraGameData)
    -- If the player gets a free social policy but has none to pick, set number of free policies to zero
    if(notificationType == NotificationTypes.NOTIFICATION_FREE_POLICY and not HasPolicyToUnlock()) then
        ChangeFreePoliciesToGrant(player:GetNumFreePolicies())
        player:SetNumFreePolicies(0);
    end

    -- If the player gets the "Can adopt policy" notification but has none to pick, remove the notification
    if(notificationType == NotificationTypes.NOTIFICATION_POLICY and not HasPolicyToUnlock()) then
        UI.RemoveNotification(notification)
    end
end

function OnTurnStart()
    -- If the player has any waiting free policies and can unlock one currently, grant a free policy
    if(freePoliciesToGrant > 0 and HasPolicyToUnlock()) then
        player:ChangeNumFreePolicies(1)
        ChangeFreePoliciesToGrant(-1)
    end
end

function OnEndGameShow(endGameType, teamId)
    -- If the player's team wins, add that to the push table
    if(teamId == player:GetTeam()) then
        pushTable["victory"] = true
    end
end


-- INTERNAL CALLABLES
function LoadScriptData(key)
    -- Retrieve value and return it
    return load(player, key)
end

function SaveScriptData(key, value)
    -- Store the value given
    save(player, key, value)
end

function UpdateTextInfos(tableName, locationId)
    -- If this table plus location ID has linked IDs, update those first
    if(textInfoLinkedIds[tableName] ~= nil and textInfoLinkedIds[tableName][locationId] ~= nil) then
        for _, linkedId in ipairs(textInfoLinkedIds[tableName][locationId]) do
            UpdateTextInfos(tableName, linkedId)
        end
    end

    -- Update the description and help text infos keys to their clean versions if possible
    clean_description_key = GameInfo[tableName][locationId].Description .. "_CLEAN"
    if Locale.ConvertTextKey(clean_description_key) ~= clean_description_key then
        ReplaceTextKey(GameInfo[tableName][locationId].Description, Locale.ConvertTextKey(clean_description_key))
        GameInfo[tableName][locationId].Description = clean_description_key
    end
    clean_help_key = GameInfo[tableName][locationId].Help .. "_CLEAN"
    if Locale.ConvertTextKey(clean_help_key) ~= clean_help_key then
        ReplaceTextKey(GameInfo[tableName][locationId].Help, Locale.ConvertTextKey(clean_help_key))
        GameInfo[tableName][locationId].Help = clean_help_key
    end
end

function ReplaceTextKey(key, value)
	-- Replace text for given 'key' with provided value. Escape single quotation marks
	DB.Query(table.concat({"UPDATE Language_en_US SET Text = '", value:gsub("'", "''"), "' WHERE Tag = '", key, "'"}))()
end

function RefreshLocale()
	-- Refresh the Locale language
	Locale.SetCurrentLanguage(Locale.GetCurrentLanguage().Type)
end

function SyncTextInfos()
    -- Update all text infos according to the values in the location table
    for type, tableName in pairs(textInfoTableNames) do
        if tableName ~= nil then
            for locationId, _ in pairs(locationTable[type]) do
                UpdateTextInfos(tableName, locationId)
            end
        end
    end

    -- If promotion sanity is enabled, refresh the locale such that promotion action buttons are updated
    if optionsTable["promotion_sanity"] then
        RefreshLocale()
    end
end

function SendLocation(type, locationId, textInfoId)
    -- If this location has been sent already, return immediately
    if locationTable[type][locationId] then
        return
    end

    -- Add location to location and push tables
    locationTable[type][locationId] = true
    table.insert(pushTable[type], locationId)

    -- Update the text infos for this location if there is a table to update for this type, using textInfoId if given
    if textInfoTableNames[type] ~= nil then
        UpdateTextInfos(textInfoTableNames[type], textInfoId ~= nil and textInfoId or locationId)
    end

    -- Save the location table
    SaveScriptData("location_table", locationTable)

    -- If promotion sanity is enabled, refresh the locale such that promotion action buttons are updated
    if type == "promotion" and optionsTable["promotion_sanity"] then
        RefreshLocale()
    end
end

function PrintResponse(response)
    -- Define format for all function responses
    print(CLIENT_PREFIX .. response .. CLIENT_POSTFIX)
end

function HasPolicyToUnlock()
    -- Return whether the player has ANY unlockable policy (branch) given the current state
    currentEra = player:GetCurrentEra()
    for policyBranchId, apPolicyIds in ipairs(policyBranchIdToAPPolicyIds) do
        -- If the player has this policy branch already unlocked and can unlock a policy in it, return true
        if player:IsPolicyBranchUnlocked(policyBranchId) then
            for _, apPolicyId in ipairs(apPolicyIds) do
                if player:CanAdoptPolicy(apPolicyId, true) then
                    return true
                end
            end

            -- If this policy branch is not unlocked yet, but the era allows for it, return true
        elseif(policyBranchIdToEraId[policyBranchId] <= currentEra) then
            return true
        end
    end

    -- If we are still here, then nothing can be unlocked, so return false
    return false
end

function ChangeFreePoliciesToGrant(value)
    -- Changes the number of free policies to grant by the given value for current session AND save file
    freePoliciesToGrant = freePoliciesToGrant + value
    SaveScriptData("free_policies_to_grant", freePoliciesToGrant)
end

function SetCultureTechYield()
    -- Set the culture yield for the culture tech to a value based on game speed and difficulty
    speedModifier = cultureTechYieldSpeedModifier[Game.GetGameSpeedType()]
    difficultyModifier = cultureTechYieldDifficultyModifier[Game.GetHandicapType()]
    cultureTechYield = math.floor(BASE_CULTURE_TECH_YIELD * speedModifier * difficultyModifier)

    -- Update the text info entry for this tech to state how much culture is rewarded
    GameInfo["Technologies"][176].Help = table.concat({
        "A repeatable technology that grants ",
        cultureTechYield,
        " [ICON_CULTURE] Culture each time it is researched."
    })
end

function SyncPromotions()
    -- Grant all promotion IDs in the promotion table to the player
    for _, promotionId in ipairs(promotionTable) do
        player:ChangeFreePromotionCount(promotionId, 1)
    end
end

function RequestSync()
    -- Request the syncing of all locations
    pushTable["sync"] = true

    -- Add all entries in the location table to the push table
    for type, locationIds in pairs(locationTable) do
        for locationId, _ in pairs(locationIds) do
            table.insert(pushTable[type], locationId)
        end
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

function SyncScriptData()
    -- Retrieve the number of free policies to grant to the player from the script data
    value = LoadScriptData("free_policies_to_grant")
    if value ~= nil then
        freePoliciesToGrant = value
    end

    -- Retrieve the item table from the script data
    value = LoadScriptData("item_table")
    if value ~= nil then
        itemTable = value
    end

    -- Retrieve the location table from the script data
    value = LoadScriptData("location_table")
    if value ~= nil then
        locationTable = value
        SyncTextInfos()
    end

    -- Retrieve the promotion table from the script data
    value = LoadScriptData("promotion_table")
    if value ~= nil then
        promotionTable = value
        SyncPromotions()
    end
end

function LoadOptionsTable()
    -- Load the options table from the SQL database
    for row in DB.Query("SELECT Key, Value FROM APOptions") do
        optionsTable[row.Key] = json.decode(json.decode(row.Value))
    end
end


-- PUBLIC CALLABLES
function AP.IsModReady()
    -- If this function can be reached and executed, the APMod is ready. Return the ID of this mod version
    PrintResponse('{"id": "<insert_output_file_id>"}')
end

function AP.SendAlert(message)
    -- Send a simple alert to the player with provided message
    Events.GameplayAlertMessage(message)
end

function AP.SendNotification(title, message, type)
    -- Send a notification to the player of the given type with provided title and message
    if type == nil then
        type = 0
    end
    player:AddNotification(notificationTypes[type], message, title)
end

function AP.SendPopup(message)
    -- Send a popup to the player with provided message
    Events.SerialEventGameMessagePopup({
        Type=ButtonPopupTypes.BUTTONPOPUP_TEXT,
        Data1=-1,
        Text=message
    })
end

function AP.GrantPolicies(policyIds)
    -- Grant all given policy IDs to the player
    for _, policyId in ipairs(policyIds) do
        -- If this policy is a non-AP policy, we want to give it to the player for free
        -- This avoids the policy culture cost going up when receiving policy items
        -- For whatever reason, the following marks the next policy granted as free
        if(policyId < LOWER_POLICY_ID and not player:HasPolicy(policyId)) then
            player:ChangeNumFreePolicies(1);
            player:ChangeNumFreePolicies(-1);
        end
        player:SetHasPolicy(policyId, true);

        -- If this policy is the Tradition finisher policy, the player gets a free Aqueduct. Send that as a location
        if(policyId == 42) then
            SendLocation("building", 91)
        end
    end
end

function AP.UnlockPolicyBranches(policyBranchIds)
    -- Unlock all given policy branch IDs for the player
    -- This is only used for syncing
    for _, policyBranchId in ipairs(policyBranchIds) do
        player:SetPolicyBranchUnlocked(policyBranchId, true);
    end
end

function AP.GrantPromotions(promotionIds)
    -- Grant all given promotion IDs to the player
    for _, promotionId in ipairs(promotionIds) do
        player:ChangeFreePromotionCount(promotionId, 1)
        table.insert(promotionTable, promotionId)
    end

    -- Save the promotion table
    SaveScriptData("promotion_table", promotionTable)
end

function AP.GrantTechs(techIds)
    -- Grant all given tech IDs to the player
    for _, techId in ipairs(techIds) do
        team:SetHasTech(techId, true);
    end
end

function AP.GrantSettlers(n)
    -- Grant n free settlers to the player
    for _=0, n-1 do
        player:AddFreeUnit(0)
    end
end

function AP.ChangeGold(value)
    -- Change gold for player by given value
    player:ChangeGold(math.max(value, -player:GetGold()))
end

function AP.ChangeCulture(value)
    -- Change culture for player by given value
    player:ChangeJONSCulture(math.max(value, -player:GetJONSCulture()))
end

function AP.ChangeFaith(value)
    -- Change faith for player by given value
    player:ChangeFaith(math.max(value, -player:GetFaith()))
end

function AP.ChangeNumFreeGreatPeople(value)
    -- Change number of free people to choose for player by given value
    player:ChangeNumFreeGreatPeople(value)
end

function AP.ChangeNumFreePolicies(value)
    -- Change number of free policies to choose for player by given value
    player:ChangeNumFreePolicies(value)
end

function AP.ChangeNumFreeTechs(value)
    -- Change number of free techs to choose for player by given value
    player:SetNumFreeTechs(player:GetNumFreeTechs()+value)
    player:AddNotification(NotificationTypes.NOTIFICATION_FREE_TECH, "You may choose a free Tech!")
end

function AP.ChangeAllCityPopulation(value)
    -- Change the population in each city of the player by given value
    for city in player:Cities() do
        city:ChangePopulation(math.max(value, -city:GetPopulation()+1), true)
    end
end

function AP.ChangeNewCityExtraPopulation(value)
    -- Change the extra population a new city is given for the player by given value
    player:ChangeNewCityExtraPopulation(value)
end

function AP.ChangeAllUnitExperience(value)
    -- Change the experience of all units of the player by given value
    for unit in player:Units() do
        unit:ChangeExperience(math.max(value, -unit:GetExperience()))
    end
end

function AP.AllUnitFreePromotion(n)
    -- Grant all units of the player a free promotion, n times
    for _=1, n do
        for unit in player:Units() do
            unit:ChangeExperience(unit:ExperienceNeeded())
        end
    end
end

function AP.ChangeCulturePerTurnForFree(value)
    -- Change the amount of free culture the player gets per turn by given value
    player:ChangeJONSCulturePerTurnForFree(value)
end

function AP.ChangeExtraHappinessPerCity(value)
    -- Change the amount of extra happiness the player gets per city by given value
    player:ChangeExtraHappinessPerCity(value)
end

function AP.StartGoldenAge(n)
    -- Immediately start a golden age for the player n times
    for _=1, n do
        player:ChangeGoldenAgeTurns(player:GetGoldenAgeLength())
    end
end

function AP.DenounceRandom(n)
    -- Get the IDs of all players that are still alive that are not the player or in the team of the player
    aiPlayerIds = {}
    for i=1, GameDefines.MAX_MAJOR_CIVS-1 do
        if(Players[i]:IsAlive() and Players[i]:GetTeam() ~= player:GetTeam()) then
            table.insert(aiPlayerIds, i)
        end
    end

    -- Pick n times a random AI player that denounces the player
    for _=1, n do
        Players[aiPlayerIds[math.random(1, #aiPlayerIds)]]:DoForceDenounce(player:GetID())
    end
end

function AP.DeclareWarRandom(n)
    -- Get the IDs of all teams that are still alive that are not the player
    aiTeamIds = {}
    for i=1, GameDefines.MAX_MAJOR_CIVS-1 do
        if Teams[i]:IsAlive() then
            table.insert(aiTeamIds, i)
        end
    end

    -- Pick n times a random AI team that declares war on the player
    for _=1, n do
        Teams[aiTeamIds[math.random(1, #aiTeamIds)]]:DeclareWar(team:GetID())
    end
end

function AP.UpdateItemTable(apItemIds)
    -- Store in item table that these AP items have been received
    for _, apItemId in ipairs(apItemIds) do
        table.insert(itemTable, apItemId)
    end
    SaveScriptData("item_table", itemTable)
end

function AP.UpdateLocationTable(type, locationIds, is_finished)
    -- Mark all locations with given IDs of the provided type as checked
    for _, locationId in ipairs(locationIds) do
        if locationTable[type][locationId] == nil then
            locationTable[type][locationId] = true
            if textInfoTableNames[type] ~= nil then
                UpdateTextInfos(textInfoTableNames[type], locationId)
            end
        end
    end

    -- If this was the final update to be performed, save the location table
    if is_finished then
        SaveScriptData("location_table", locationTable)
    end

    -- If promotion sanity is enabled, refresh the locale such that promotion action buttons are updated
    if optionsTable["promotion_sanity"] then
        RefreshLocale()
    end
end

function AP.GetPushTable()
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
    PrintResponse(table.concat({"{", table.concat(jsonStrings, ","), "}"}))
    InitPushTable()
end

function AP.GetItemTable()
    -- Print the item table contents as a single JSON array in a JSON object
    PrintResponse(table.concat({'{"items": [', table.concat(itemTable, ","), "]}"}))
end


-- INIT FUNCTION
function Init()
    -- Register event functions
    Events.ActivePlayerTurnStart.Add(OnTurnStart)
    Events.TechAcquired.Add(OnTechAcquired)
    Events.EndGameShow.Add(OnEndGameShow)
    Events.NotificationAdded.Add(OnNotificationAdded)
    GameEvents.PlayerAdoptPolicy.Add(OnPolicyAdopted)
    GameEvents.PlayerAdoptPolicyBranch.Add(OnPolicyBranchAdopted)
    GameEvents.CityConstructed.Add(OnCityBuildingConstructed)
    GameEvents.CityCaptureComplete.Add(OnCityCaptured)
    GameEvents.CityTrained.Add(OnCityUnitTrained)
    GameEvents.CityCanTrain.Add(OnCityCanTrain)
    GameEvents.UnitPromoted.Add(OnUnitPromoted)
    GameEvents.UnitUpgraded.Add(OnUnitUpgraded)

    -- Make sure that allow policy saving is turned on
    Game.SetOption(GameOptionTypes.GAMEOPTION_POLICY_SAVING, true)

    -- Set the culture tech yield
    SetCultureTechYield()

    -- Initialize push table
    InitPushTable()

    -- Load options table
    LoadOptionsTable()

    -- Synchronize all local variables with the script data
    SyncScriptData()

    -- Request a sync between game and client
    RequestSync()

    -- Give player and AI their corresponding modified techs at the start
    for i = 0, GameDefines.MAX_CIV_PLAYERS-1, 1 do
        pPlayer = Players[i]
        pTeam = Teams[pPlayer:GetTeam()]
        if pPlayer:IsHuman() then
            pTeam:SetHasTech(81, true)
            pPlayer:ChangeFreePromotionCount(optionsTable["promotion_sanity"] and 228 or 227, 1)
        else
            pTeam:SetHasTech(82, true)
            pPlayer:ChangeFreePromotionCount(227, 1)
        end
    end

    -- Send notification to player that APMod was loaded successfully
    AP.SendNotification("AP Mod loaded", "AP Mod was loaded successfully.")
end

Init()
