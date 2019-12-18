import Tkinter
import tkMessageBox
import player
import ai


root = None

playerX = player.Player('X', False)
playerO = player.Player('O', False)
playerX.next = playerO
playerO.next = playerX


activePlayer = playerX
selectingPosition = False
selectingDirection = False
tempBtnClickedInfo = None

matrixOfButton = []


def swapPlayer():
    global activePlayer
    activePlayer = activePlayer.getNext()


def createButton(i, j):
    global root
    return Tkinter.Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(matrixOfButton[i][j], i, j))


def enableButton(button):
    button.configure(state='normal', bg='grey')


def enableAllPossibleButton():
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or i == 4 or j == 0 or j == 4):
                if (writeText() == 'X'):
                    if (matrixOfButton[i][j]["text"] != 'O'):
                        matrixOfButton[i][j].configure(
                            state='normal', bg='grey')
                elif (writeText() == 'O'):
                    if (matrixOfButton[i][j]["text"] != 'X'):
                        matrixOfButton[i][j].configure(
                            state='normal', bg='grey')


def disableButton(button):
    button.configure(state=Tkinter.DISABLED, bg='black')


def disableAllButton():
    for i in range(0, 5):
        for j in range(0, 5):
            disableButton(matrixOfButton[i][j])


def writeText():
    return activePlayer.symbol


def endGame(player):
    tkMessageBox.showinfo("Game Ended", player + " player win !")
    raise SystemExit


def insertAtRow(i, start, end, increment, tempBtnClickedInfo):
    matrixOfButton[tempBtnClickedInfo[1]
                   ][tempBtnClickedInfo[2]]["text"] = 'VOID'
    temp = matrixOfButton[i][start]["text"]
    temp2 = None
    matrixOfButton[i][start]["text"] = writeText()
    for iterator in range(start+increment, end+increment, increment):
        if (temp == 'VOID'):
            break
        temp2 = matrixOfButton[i][iterator]["text"]
        matrixOfButton[i][iterator]["text"] = temp
        temp = temp2


def insertAtColumn(j, start, end, increment, tempBtnClickedInfo):
    matrixOfButton[tempBtnClickedInfo[1]
                   ][tempBtnClickedInfo[2]]["text"] = 'VOID'
    temp = matrixOfButton[start][j]["text"]
    temp2 = None
    matrixOfButton[start][j]["text"] = writeText()
    for iterator in range(start+increment, end+increment, increment):
        if (temp == 'VOID'):
            break
        temp2 = matrixOfButton[iterator][j]["text"]
        matrixOfButton[iterator][j]["text"] = temp
        temp = temp2


def endOfSelection():
    global activePlayer, selectingPosition, selectingDirection
    selectingPosition = False
    selectingDirection = False
    swapPlayer()
    disableAllButton()
    checkForWin()
    if (activePlayer.is_ai == True):
        aiPlay()
    enableAllPossibleButton()


def btnClick(button, i, j):

    global selectingPosition, selectingDirection, tempBtnClickedInfo

    if (selectingPosition == False and selectingDirection == False):
        disableAllButton()
        if (i == 0):
            enableButton(matrixOfButton[4][j])
            if (j != 0):
                enableButton(matrixOfButton[i][0])
            if (j != 4):
                enableButton(matrixOfButton[i][4])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True
        if (i == 4):
            enableButton(matrixOfButton[0][j])
            if (j != 0):
                enableButton(matrixOfButton[i][0])
            if (j != 4):
                enableButton(matrixOfButton[i][4])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True
        if (j == 0):
            enableButton(matrixOfButton[i][4])
            if (i != 0):
                enableButton(matrixOfButton[0][j])
            if (i != 4):
                enableButton(matrixOfButton[4][j])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True
        if (j == 4):
            enableButton(matrixOfButton[i][0])
            if (i != 0):
                enableButton(matrixOfButton[0][j])
            if (i != 4):
                enableButton(matrixOfButton[4][j])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True

    elif (selectingPosition == True and selectingDirection == False):

        if (i == tempBtnClickedInfo[1] and j != tempBtnClickedInfo[2]):
            if (j == 0):
                insertAtRow(i, 0, 4, 1, tempBtnClickedInfo)
                endOfSelection()
            elif (j == 4):
                insertAtRow(i, 4, 0, -1, tempBtnClickedInfo)
                endOfSelection()

        elif (i != tempBtnClickedInfo[1] and j == tempBtnClickedInfo[2]):
            if (i == 0):
                insertAtColumn(j, 0, 4, 1, tempBtnClickedInfo)
                endOfSelection()
            elif (i == 4):
                insertAtColumn(j, 4, 0, -1, tempBtnClickedInfo)
                endOfSelection()


def checkForWin():
    for i in range(0, 5, 1):
        if (matrixOfButton[i][0]['text'] != " "):
            if (matrixOfButton[i][0]["text"] == matrixOfButton[i][1]["text"] == matrixOfButton[i][2]["text"] == matrixOfButton[i][3]["text"] == matrixOfButton[i][4]["text"]):
                endGame(matrixOfButton[i][0]["text"])
    for j in range(0, 5, 1):
        if (matrixOfButton[0][j]['text'] != " "):
            if (matrixOfButton[0][j]["text"] == matrixOfButton[1][j]["text"] == matrixOfButton[2][j]["text"] == matrixOfButton[3][j]["text"] == matrixOfButton[4][j]["text"]):
                endGame(matrixOfButton[0][j]["text"])
    if (matrixOfButton[0][0]['text'] != " "):
        if (matrixOfButton[0][0]["text"] == matrixOfButton[1][1]["text"] == matrixOfButton[2][2]["text"] == matrixOfButton[3][3]["text"] == matrixOfButton[4][4]["text"]):
            endGame(matrixOfButton[0][0]["text"])
    if (matrixOfButton[0][4]['text'] != " "):
        if (matrixOfButton[0][4]["text"] == matrixOfButton[1][3]["text"] == matrixOfButton[2][2]["text"] == matrixOfButton[3][1]["text"] == matrixOfButton[4][0]["text"]):
            endGame(matrixOfButton[0][0]["text"])


def aiPlay():
    setBoardFromSimplified(ai.findBestPlay(getSimplifiedBoard(), activePlayer))
    checkForWin()
    swapPlayer()
    if (activePlayer.is_ai == True):
        aiPlay()
    else:
        return


def getSimplifiedBoard():
    global matrixOfButton
    boardSimplified = []
    for i in range(0, 5):
        boardSimplified.append(range(0, 5))
    for i in range(0, 5):
        for j in range(0, 5):
            boardSimplified[i][j] = matrixOfButton[i][j]["text"]
    return boardSimplified


def setBoardFromSimplified(boardSimplified):
    global matrixOfButton
    for i in range(0, 5):
        boardSimplified.append(range(0, 5))
    for i in range(0, 5):
        for j in range(0, 5):
            matrixOfButton[i][j]["text"] = boardSimplified[i][j]


def launchApp(playerX_is_ai, playerO_is_ai):
    global root, playerX, playerO

    if (playerX_is_ai == 'ai'):
        playerX.is_ai = True
    else:
        playerX_is_ai = False

    if (playerO_is_ai == 'ai'):
        playerO.is_ai = True
    else:
        playerO_is_ai = False

    print("playerX.is_ai :", playerX.is_ai)
    print("playerO.is_ai :", playerO.is_ai)

    root = Tkinter.Tk()
    root.title("Quixo")

    for i in range(0, 5):
        matrixOfButton.append(range(0, 5))

    for i in range(0, 5):
        for j in range(0, 5):
            matrixOfButton[i][j] = createButton(i, j)
            if(i != 0 and i != 4 and j != 0 and j != 4):
                disableButton(matrixOfButton[i][j])
            matrixOfButton[i][j].grid(row=i, column=j)

    if (activePlayer.is_ai == True):
        aiPlay()

    root.mainloop()
