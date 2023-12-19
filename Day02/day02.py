import os


def openFile(fileName):
    cwd = os.path.dirname(os.path.realpath(__file__))
    completePath = os.path.join(cwd, fileName)
    with open(completePath, "r") as readFile:
        return readFile.read().split("\n")


def getGameId(inputString):
    splitList = inputString.split(":")
    gamePart = splitList[0]

    gameId = int(gamePart[5:])
    return gameId


def getRounds(inputString):
    gamePart = inputString.split(":")[-1]
    rounds = gamePart.split(";")
    return rounds


def parseRound(round):
    splitRound = round.split(",")
    roundDict = {}
    for split in splitRound:
        split = split[1:]
        number = int(split.split(" ")[0])
        color = split.split(" ")[-1]
        if color not in roundDict:
            roundDict[color] = 0
        roundDict[color] += number
    return roundDict


def parseGame(inputString):
    gameId = getGameId(inputString)
    rounds = getRounds(inputString)
    gameDict = False
    for round in rounds:
        roundDict = parseRound(round)
        if gameDict == False:
            gameDict = roundDict
        else:
            for color in roundDict.keys():
                if color not in gameDict:
                    gameDict[color] = 0
                if roundDict[color] > gameDict[color]:
                    gameDict[color] = roundDict[color]
    return gameId, gameDict


def checkLimitValid(limit, game):
    for color in limit.keys():
        if color in game.keys():
            if game[color] > limit[color]:
                return False
    return True


testLimit = {"red": 12, "green": 13, "blue": 14}


testStrings = openFile("test.txt")
testSolution = 0
for line in testStrings:
    gameId, gameDict = parseGame(line)
    validGame = checkLimitValid(testLimit, gameDict)
    if validGame:
        testSolution += gameId
print(testSolution)

inputSolution = 0
partbSolution = 0

inputStrings = openFile("input.txt")
for line in inputStrings:
    gameId, gameDict = parseGame(line)
    partBScore = gameDict["red"] * gameDict["blue"] * gameDict["green"]
    partbSolution += partBScore
    validGame = checkLimitValid(testLimit, gameDict)
    if validGame:
        inputSolution += gameId
print(inputSolution)

print(partbSolution)
