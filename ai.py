import threading
import copy

listOfPlayToReturn = list()
playToReturn = None

# board must be a matrix of string representing the symbol of the pawn


def findBestPlay(board, activePlayer):
    threads = list()
    for i in range(0, len(board), 1):
        for j in range(0, len(board), 1):
            if (i == 4 or i == 0 or j == 0 or j == 4):
                if (board[i][j] == activePlayer or board[i][j] == ' '):
                    x = threading.Thread(target=makeAllPlay,
                                         args=(copy.deepcopy(i), copy.deepcopy(j), copy.deepcopy(board), copy.deepcopy(activePlayer), copy.deepcopy(activePlayer), 0))
                    threads.append(x)
                    x.start()

    for index, thread in enumerate(threads):
        thread.join()

    global playToReturn
    for index, tempBoard in enumerate(listOfPlayToReturn):
        if (len(tempBoard) > 0):
            if (getBoardValue(tempBoard, activePlayer) > getBoardValue(playToReturn, activePlayer)):
                playToReturn = tempBoard
    return playToReturn


def makeAllPlay(i, j, board, activePlayer, originalActivePlayer, depth):

    if (depth > 1):
        return board

    matrixOfPossiblePlay = []
    for k in range(0, 5, 1):
        matrixOfPossiblePlay.append(range(0, 5, 1))

    for k in range(0, 5, 1):
        for l in range(0, 5, 1):
            matrixOfPossiblePlay[k][l] = False

    # Checking all possible play
    if (i == 0):
        matrixOfPossiblePlay[4][j] = True
        if (j != 0):
            matrixOfPossiblePlay[i][0] = True
        if (j != 4):
            matrixOfPossiblePlay[i][4] = True
    if (i == 4):
        matrixOfPossiblePlay[0][j] = True
        if (j != 0):
            matrixOfPossiblePlay[i][0] = True
        if (j != 4):
            matrixOfPossiblePlay[i][4] = True
    if (j == 0):
        matrixOfPossiblePlay[i][4] = True
        if (i != 0):
            matrixOfPossiblePlay[0][j] = True
        if (i != 4):
            matrixOfPossiblePlay[4][j] = True
    if (j == 4):
        matrixOfPossiblePlay[i][0] = True
        if (i != 0):
            matrixOfPossiblePlay[0][j] = True
        if (i != 4):
            matrixOfPossiblePlay[4][j] = True

    listAllPlayPossible = list()

    # Make all the play
    for k in range(0, 5, 1):
        for l in range(0, 5, 1):
            if (matrixOfPossiblePlay[k][l] == True):
                tempBoard = []
                if (k == i and l != j):
                    if (l == 0):
                        tempBoard = insertAtRow(copy.deepcopy(k), 0, 4, 1, copy.deepcopy(i), copy.deepcopy(j),
                                                copy.deepcopy(board), copy.deepcopy(activePlayer))
                    elif (l == 4):
                        tempBoard = insertAtRow(copy.deepcopy(k), 4, 0, -1, copy.deepcopy(i), copy.deepcopy(j),
                                                copy.deepcopy(board), activePlayer)

                elif (k != i and l == j):
                    if (k == 0):
                        tempBoard = insertAtColumn(copy.deepcopy(l), 0, 4, 1, copy.deepcopy(i), copy.deepcopy(j),
                                                   copy.deepcopy(board), activePlayer)
                    elif (k == 4):
                        tempBoard = insertAtColumn(copy.deepcopy(l), 4, 0, -1, copy.deepcopy(i), copy.deepcopy(j),
                                                   copy.deepcopy(board), activePlayer)

                for k in range(0, len(tempBoard), 1):
                    for l in range(0, len(tempBoard), 1):
                        if (k == 4 or k == 0 or l == 0 or l == 4):
                            if (tempBoard[k][l] == swapPlayer(activePlayer) or tempBoard[k][l] == ' '):
                                listAllPlayPossible.append(makeAllPlay(copy.deepcopy(k), copy.deepcopy(l), copy.deepcopy(tempBoard),
                                                                       copy.deepcopy(swapPlayer(activePlayer)), originalActivePlayer, copy.deepcopy(depth+1)))

    bestValue = 0
    boardToReturn = []
    if (len(listAllPlayPossible) > 0):
        for k in range(0, len(listAllPlayPossible), 1):
            if (len(listAllPlayPossible[k]) > 0):
                tempValue = getBoardValue(listAllPlayPossible[k], activePlayer)
                if (bestValue < tempValue):
                    bestValue = tempValue
                    boardToReturn = listAllPlayPossible[k]
                if (bestValue == 5):
                    break
    else:
        return None

    if (depth == 0):
        global listOfPlayToReturn
        listOfPlayToReturn.append(boardToReturn)

    return boardToReturn


def printBoard(board):
    if len(board) > 0:
        print board[0]
        print board[1]
        print board[2]
        print board[3]
        print board[4]


def insertAtRow(k, start, end, increment, i, j, board, activePlayer):
    board[i][j] = 'VOID'
    temp = board[k][start]
    temp2 = None
    board[k][start] = activePlayer.symbol
    for iterator in range(start+increment, end+increment, increment):
        if (temp == 'VOID'):
            break
        temp2 = board[k][iterator]
        board[k][iterator] = temp
        temp = temp2
    return board


def insertAtColumn(l, start, end, increment, i, j, board, activePlayer):
    board[i][j] = 'VOID'
    temp = board[start][l]
    temp2 = None
    board[start][l] = activePlayer.symbol
    for iterator in range(start+increment, end+increment, increment):
        if (temp == 'VOID'):
            break
        temp2 = board[iterator][l]
        board[iterator][l] = temp
        temp = temp2
    return board


def swapPlayer(activePlayer):
    return activePlayer.getNext()


def getBoardValue(board, activePlayer):

    if (board == None):
        return 0

    # Check if there is a win
    for i in range(0, 5, 1):
        if (board[i][0] == activePlayer.symbol):
            if (board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4]):
                return 5
    for j in range(0, 5, 1):
        if (board[0][j] == activePlayer.symbol):
            if (board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j]):
                return 5
    if (board[0][0] == activePlayer.symbol):
        if (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]):
            return 5
    if (board[0][4] == activePlayer.symbol):
        if (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]):
            return 5

    # Check if there is a lose
    for i in range(0, 5, 1):
        if (board[i][0] == swapPlayer(activePlayer).symbol):
            if (board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4]):
                return 0
    for j in range(0, 5, 1):
        if (board[0][j] == swapPlayer(activePlayer).symbol):
            if (board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j]):
                return 0
    if (board[0][0] == swapPlayer(activePlayer).symbol):
        if (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]):
            return 0
    if (board[0][4] == swapPlayer(activePlayer).symbol):
        if (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]):
            return 0

    # Check the longuest line
    bestValue = 0
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            tempValue = verticalChecking(board, activePlayer, i, j)
            if (bestValue < tempValue):
                bestValue = tempValue
            tempValue = horizontalChecking(board, activePlayer, i, j)
            if (bestValue < tempValue):
                bestValue = tempValue
            tempValue = diagonaleChecking(board, activePlayer, i, j)
            if (bestValue < tempValue):
                bestValue = tempValue
    return bestValue


def verticalChecking(board, activePlayer, i, j):
    value = 1
    if (board[i][j] == activePlayer.symbol and i < 4 and i > 0):
        I = i+1
        while (board[I][j] == activePlayer.symbol):
            value += 1
            I += 1
            if (I > 4):
                break

        I = i-1
        while (board[I][j] == activePlayer.symbol):
            value += 1
            I -= 1
            if (I < 0):
                break

        return value

    else:
        return 0


def horizontalChecking(board, activePlayer, i, j):
    value = 1
    if (board[i][j] == activePlayer.symbol and j < 4 and j > 0):
        J = j+1
        while (board[i][J] == activePlayer.symbol):
            value += 1
            J += 1
            if (J > 4):
                break

        J = j-1
        while (board[i][J] == activePlayer.symbol):
            value += 1
            J -= 1
            if (J < 0):
                break

        return value

    else:
        return 0


def diagonaleChecking(board, activePlayer, i, j):
    value = 1
    if (board[i][j] == activePlayer.symbol and i < 4 and i > 0 and j < 4 and j > 0):
        if (i == j):
            I = i+1
            J = j+1
            while (board[I][J] == activePlayer.symbol):
                value += 1
                I += 1
                J += 1
                if ((I > 4) or (J > 4)):
                    break

            I = i-1
            J = j-1
            while (board[I][J] == activePlayer.symbol):
                value += 1
                I -= 1
                J -= 1
                if ((I < 0) or (J < 0)):
                    break

            return value

        elif (j == 4-i):
            I = i+1
            J = j-1
            while (board[I][J] == activePlayer.symbol):
                value += 1
                I += 1
                J -= 1
                if ((I > 4) or (J < 0) or (I < 0) or (J > 4)):
                    break

            I = i+1
            J = j-1
            while (board[I][J] == activePlayer.symbol):
                value += 1
                I += 1
                J -= 1
                if ((I < 0) or (J > 4) or (I > 4) or (J < 0)):
                    break

            return value

    return 0
