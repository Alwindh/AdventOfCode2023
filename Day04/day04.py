import os
from pprint import pprint


def openFile(fileName):
    cwd = os.path.dirname(os.path.realpath(__file__))
    completePath = os.path.join(cwd, fileName)
    with open(completePath, "r") as readFile:
        return readFile.read().split("\n")


def getWinningNumbers(inputLine):
    numbers = inputLine.split(" | ")[0]
    while "  " in numbers:
        numbers = numbers.replace("  ", " ")
    numbers = numbers.split(": ")[-1].split(" ")
    return numbers


def getCardNumbers(inputLine):
    numbers = inputLine.split(" | ")[-1]
    while "  " in numbers:
        numbers = numbers.replace("  ", " ")
    numberList = numbers.split(" ")
    return numberList


def getGameWins(inputLine):
    winningNumbers = getWinningNumbers(inputLine)
    gameNumbers = getCardNumbers(inputLine)
    wins = 0
    for number in gameNumbers:
        if number in winningNumbers:
            wins += 1
    return wins


def getGamePoints(inputLine):
    wins = getGameWins(inputLine)
    if wins == 0:
        return 0
    if wins == 1:
        return 1
    if wins == 2:
        return 2
    score = 2
    score = 2 ** (wins - 1)
    return score


testInput = openFile("test.txt")
testScore = 0
for line in testInput:
    gamePoints = getGamePoints(line)
    testScore += gamePoints
print(testScore)


inputLines = openFile("input.txt")
inputScore = 0
for line in inputLines:
    gamePoints = getGamePoints(line)
    inputScore += gamePoints
print(inputScore)


countScore = 0
countDict = {}
for key, value in enumerate(inputLines):
    countDict[key] = {"value": value, "amount": 1}
for key in countDict.keys():
    value = countDict[key]["value"]
    wins = getGameWins(value)
    nextGames = []
    for i in range(1, wins + 1):
        nextGames.append(key + i)
    for game in nextGames:
        countDict[game]["amount"] += countDict[key]["amount"]
    countScore += countDict[key]["amount"]
print(countScore)
