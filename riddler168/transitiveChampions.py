from sys import argv

if argv[1] == "mens":
    readFile = open("mensNcaa.txt")
elif argv[1] == "womens":
    readFile = open("womensNcaa.txt")
else:
    print('Enter either mens or womens for the first argument')
    exit()


if len(argv) < 3:
    print("Enter a team name as the second argument")
    exit()


teamOfInterest = argv[2]
resultLog = {}


# build up a dictionary of all the teams a given team lost to
for line in readFile:
    losingTeam = line[41:65].strip()
    teamThatBeat = line[12:35].strip()
    
    if losingTeam in resultLog:
        winningTeamList = resultLog[losingTeam]
        resultLog[losingTeam] = list(set(winningTeamList + [teamThatBeat]))
    else:
        resultLog[losingTeam] = [teamThatBeat]


# recursively walk through all the teams that beat teams that beat Virginia
if teamOfInterest not in resultLog:
    print("%s is not a team. Try again" % teamOfInterest)
    exit()
else:
    teamsLostTo = resultLog[teamOfInterest]

teamsAlreadyLookedAt = [teamOfInterest]

for team in teamsLostTo:
    if team not in teamsAlreadyLookedAt:
        if team not in resultLog:
            teamsLostTo += [team]
            resultLog[team] = []
        else:
            teamsLostTo += resultLog[team]
        
        teamsAlreadyLookedAt += [team]

transitiveWinningTeams = set(teamsLostTo)
nonTransitiveWinningTeams = set(resultLog.keys()) - set(teamsLostTo)

print("Total teams: %d" % len(resultLog.keys()))
print("Transitive Champion Teams: %d" % len(set(teamsLostTo)))
print("Not Transitive Champion Teams: %d" % len(nonTransitiveWinningTeams) )


# print("Transitive National Champions:")
# for team in transitiveWinningTeams:
#     print("\t-%s" % team)

# print("Non-Transitive National Champions:")
# for team in nonTransitiveWinningTeams:
#     print("\t-%s" % team)
