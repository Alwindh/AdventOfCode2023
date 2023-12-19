import os


def openFile(fileName):
    cwd = os.path.dirname(os.path.realpath(__file__))
    completePath = os.path.join(cwd, fileName)
    with open(completePath, "r") as readFile:
        return readFile.read().split("\n")


def removeLetters(inputString):
    digitsOnly = ""
    for i in inputString:
        if i.isdigit():
            digitsOnly += i
    return digitsOnly


def getLineNumber(inputString):
    digits = removeLetters(line)
    twoDigits = digits[0] + digits[-1]
    return twoDigits


testLines = openFile("test.txt")
testTotal = 0
for line in testLines:
    twoDigits = getLineNumber(line)
    testTotal += int(twoDigits)

inputLines = openFile("input.txt")
inputTotal = 0
for line in inputLines:
    twoDigits = getLineNumber(line)
    inputTotal += int(twoDigits)

stringCypher = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

newInputTotal = 0
for line in inputLines:
    for cypher in stringCypher.keys():
        line = line.replace(cypher, stringCypher[cypher])
    twoDigits = getLineNumber(line)
    newInputTotal += int(twoDigits)

print(testTotal)

print(inputTotal)

print(newInputTotal)
