import os


def openFile(fileName):
    cwd = os.path.dirname(os.path.realpath(__file__))
    completePath = os.path.join(cwd, fileName)
    with open(completePath, "r") as readFile:
        return readFile.read().split("\n")


def buildGrid(inputLines):
    grid = {}
    for i in range(len(inputLines)):
        for j in range(len(inputLines[i])):
            grid[(i, j)] = inputLines[i][j]
    return grid


def getSegments(inputString, index, grid, stars=None):
    validNumbers = 0
    currentRunner = ""
    currentStart = ""
    for key, value in enumerate(inputString):
        if value.isdigit():
            if currentStart == "":
                currentStart = key
            currentRunner += value
        else:
            if currentRunner != "":
                numberValid = checkIfDigitsAreValid(
                    index, len(currentRunner), currentStart, grid
                )
                if numberValid:
                    starCoords = getStarCoords(
                        index, len(currentRunner), currentStart, grid
                    )
                    for star in starCoords:
                        if star not in stars.keys():
                            stars[star] = []
                        stars[star].append(currentRunner)
                    validNumbers += int(currentRunner)
                currentRunner = ""
                currentStart = ""
    if currentRunner != "":
        numberValid = checkIfDigitsAreValid(
            index, len(currentRunner), currentStart, grid
        )
        if numberValid:
            validNumbers += int(currentRunner)
            starCoords = getStarCoords(index, len(currentRunner), currentStart, grid)
            for star in starCoords:
                if star not in stars.keys():
                    stars[star] = []
                stars[star].append(currentRunner)
    return validNumbers, stars


def generateCheckList(index, start, length):
    toCheckList = []
    toCheckList.append((index, start - 1))
    toCheckList.append((index, start + length))
    for i in range(start - 1, start + length + 1):
        toCheckList.append((index - 1, i))
        toCheckList.append((index + 1, i))
    return toCheckList


def getGridCharacters(coordList, grid):
    gridCharacters = ""
    for coord in coordList:
        if coord in grid.keys():
            gridCharacters += grid[coord]
    return gridCharacters


def checkIfDigitsAreValid(index, length, start, grid):
    toCheckList = generateCheckList(index, start, length)
    gridCharacters = getGridCharacters(toCheckList, grid)
    while "." in gridCharacters:
        gridCharacters = gridCharacters.replace(".", "")
    newGridCharacters = ""
    for i in gridCharacters:
        if i.isdigit() == False:
            newGridCharacters += i
    if len(gridCharacters) > 0:
        return True
    return False


def getStarCoords(index, length, start, grid):
    starCoords = []
    toCheckList = generateCheckList(index, start, length)
    for coord in toCheckList:
        character = getGridCharacters([coord], grid)
        if character == "*":
            starCoords.append(coord)

    return starCoords


def solveInput(inputLines):
    grid = buildGrid(inputLines)
    solution = 0
    starGrid = {}
    starSolution = 0
    for key, value in enumerate(inputLines):
        solutionAmount, starGrid = getSegments(value, key, grid, starGrid)
        solution += solutionAmount
    print(solution)
    for star in starGrid.keys():
        if len(starGrid[star]) == 2:
            starValue = int(starGrid[star][0]) * int(starGrid[star][-1])
            starSolution += starValue
    print(starSolution)


testLines = openFile("test.txt")
solveInput(testLines)
print()
inputLines = openFile("input.txt")
solveInput(inputLines)
