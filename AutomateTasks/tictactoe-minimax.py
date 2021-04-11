from math import inf as infinity
import copy

gameState = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
human = ""
algorithm = ""


def setValues():
    choice = input("Enter choice (X/O) : ").upper()

    if choice == "X":
        globals()["human"] = "X"
        globals()["algorithm"] = "O"
    elif choice == "O":
        globals()["human"] = "O"
        globals()["algorithm"] = "X"
    else:
        setValues()


def getHumanInput():
    return int(input("Enter location (1-9) : "))


def playMove(state, player, index):
    row = int((index - 1) / 3)
    col = (index - 1) % 3

    if state[row][col] == " ":
        state[row][col] = player

    else:
        index = getHumanInput()
        playMove(state, player, index)


def checkState(gameState):
    isDraw = True

    for i in range(3):
        for j in range(3):
            if gameState[i][j] == " ":
                isDraw = False

    if isDraw:
        return None, "Draw"

    # Check horizontals
    if (
        gameState[0][0] == gameState[0][1]
        and gameState[0][1] == gameState[0][2]
        and gameState[0][0] != " "
    ):
        return gameState[0][0], "Done"
    if (
        gameState[1][0] == gameState[1][1]
        and gameState[1][1] == gameState[1][2]
        and gameState[1][0] != " "
    ):
        return gameState[1][0], "Done"
    if (
        gameState[2][0] == gameState[2][1]
        and gameState[2][1] == gameState[2][2]
        and gameState[2][0] != " "
    ):
        return gameState[2][0], "Done"

    # Check verticals
    if (
        gameState[0][0] == gameState[1][0]
        and gameState[1][0] == gameState[2][0]
        and gameState[0][0] != " "
    ):
        return gameState[0][0], "Done"
    if (
        gameState[0][1] == gameState[1][1]
        and gameState[1][1] == gameState[2][1]
        and gameState[0][1] != " "
    ):
        return gameState[0][1], "Done"
    if (
        gameState[0][2] == gameState[1][2]
        and gameState[1][2] == gameState[2][2]
        and gameState[0][2] != " "
    ):
        return gameState[0][2], "Done"

    # Check diagonals
    if (
        gameState[0][0] == gameState[1][1]
        and gameState[1][1] == gameState[2][2]
        and gameState[0][0] != " "
    ):
        return gameState[1][1], "Done"
    if (
        gameState[2][0] == gameState[1][1]
        and gameState[1][1] == gameState[0][2]
        and gameState[2][0] != " "
    ):
        return gameState[1][1], "Done"

    return None, "Not Done"


def printBoard(gameState):
    print("----------------")
    print(
        "| "
        + str(gameState[0][0])
        + " || "
        + str(gameState[0][1])
        + " || "
        + str(gameState[0][2])
        + " |"
    )
    print("----------------")
    print(
        "| "
        + str(gameState[1][0])
        + " || "
        + str(gameState[1][1])
        + " || "
        + str(gameState[1][2])
        + " |"
    )
    print("----------------")
    print(
        "| "
        + str(gameState[2][0])
        + " || "
        + str(gameState[2][1])
        + " || "
        + str(gameState[2][2])
        + " |"
    )
    print("----------------")


def getBestMove(state):
    bestScore = -infinity
    bestMove = None

    for i in range(3):
        for j in range(3):
            if state[i][j] == " ":
                cell = (i * 3) + (j + 1)
                newState = copy.deepcopy(state)
                playMove(newState, algorithm, cell)
                result = minimax(newState, 0, False)
                if result > bestScore:
                    bestScore = result
                    bestMove = cell

    return bestMove


def minimax(state, depth, isMaximising):
    result, done = checkState(state)
    if done == "Done":
        if result == algorithm:
            return 1
        elif result == human:
            return -1
    elif done == "Draw":
        return 0

    bestScore = None
    if isMaximising:
        bestScore = -infinity
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    cell = (i * 3) + (j + 1)
                    newState = copy.deepcopy(state)
                    playMove(newState, algorithm, cell)
                    result = minimax(newState, depth + 1, False)
                    if result > bestScore:
                        bestScore = result

        return bestScore
    else:
        bestScore = infinity
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    cell = (i * 3) + (j + 1)
                    newState = copy.deepcopy(state)
                    playMove(newState, human, cell)
                    result = minimax(newState, depth + 1, True)
                    if result < bestScore:
                        bestScore = result

        return bestScore


print("Tic Tac Toe")
printBoard(gameState)
setValues()
currentState = "Not Done"
winner = None
currentPlayer = human

while currentState == "Not Done":
    if currentPlayer == human:
        index = getHumanInput()
    else:
        index = getBestMove(gameState)

    playMove(gameState, currentPlayer, index)

    printBoard(gameState)

    winner, currentState = checkState(gameState)

    if winner != None:
        print(str(winner) + " won!")
    else:
        if currentPlayer == human:
            currentPlayer = algorithm
        elif currentPlayer == algorithm:
            currentPlayer = human

    if currentState == "Draw":
        print("Draw")