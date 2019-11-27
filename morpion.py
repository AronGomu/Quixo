import Tkinter
import tkMessageBox
root = Tkinter.Tk()
root.title("Quixo")


turnOfPlayerO = True


def changePlayer():
    global turnOfPlayerO
    if turnOfPlayerO == True:
        turnOfPlayerO = False
    else:
        turnOfPlayerO = True


selectingPosition = False
selectingDirection = False
tempBtnClickedInfo = None

matrixOfButton = []


def createButton(i, j):
    return Tkinter.Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(matrixOfButton[i][j], i, j))


def enableButton(button):
    button.configure(state='normal', bg='grey')


def enableAllPossibleButton():
    for i in range(0, 5):
        for j in range(0, 5):
            if (i == 0 or i == 4 or j == 0 or j == 4):
                if (matrixOfButton[i][j]["text"] != 'O' and matrixOfButton[i][j]["text"] != 'X'):
                    matrixOfButton[i][j].configure(state='normal', bg='grey')


def disableButton(button):
    button.configure(state=Tkinter.DISABLED, bg='black')


def disableAllButton():
    for i in range(0, 5):
        for j in range(0, 5):
            disableButton(matrixOfButton[i][j])


def writeText(turnOfPlayerO):
    if (turnOfPlayerO == True):
        return 'O'
    elif (turnOfPlayerO == False):
        return 'X'
    else:
        print ("ERROR in writeText. turnOfPlayer is :", turnOfPlayer)
        return None


def endGame(player):
    tkMessageBox.showinfo("Game Ended", player + " player win !")
    raise SystemExit


def insertAtRow(i, start, end, increment):
    temp = matrixOfButton[i][start]["text"]
    temp2 = None
    matrixOfButton[i][start]["text"] = writeText(turnOfPlayerO)
    for iterator in range(start+increment, end+increment, increment):
        temp2 = matrixOfButton[i][iterator]["text"]
        matrixOfButton[i][iterator]["text"] = temp
        temp = temp2


def insertAtColumn(j, start, end, increment):
    temp = matrixOfButton[start][j]["text"]
    temp2 = None
    matrixOfButton[start][j]["text"] = writeText(turnOfPlayerO)
    for iterator in range(start+increment, end+increment, increment):
        temp2 = matrixOfButton[iterator][j]["text"]
        matrixOfButton[iterator][j]["text"] = temp
        temp = temp2


def endOfSelection():
    global selectingPosition, selectingDirection
    selectingPosition = False
    selectingDirection = False
    changePlayer()
    disableAllButton()
    enableAllPossibleButton()


def btnClick(button, i, j):
    global turnOfPlayerO, selectingPosition, selectingDirection, tempBtnClickedInfo

    if (selectingPosition == False and selectingDirection == False):
        disableAllButton()
        if (i == 0 or i == 4):
            enableButton(matrixOfButton[0][j])
            enableButton(matrixOfButton[4][j])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True
        if (j == 0 or j == 4):
            enableButton(matrixOfButton[i][0])
            enableButton(matrixOfButton[i][4])
            tempBtnClickedInfo = [button, i, j]
            selectingPosition = True

    elif (selectingPosition == True and selectingDirection == False):
        if (i == tempBtnClickedInfo[1] and j == tempBtnClickedInfo[2]):
            if (j == 0):
                if (i == 0):
                    disableAllButton()
                    enableButton(matrixOfButton[i+1][j])
                    enableButton(matrixOfButton[i][j+1])
                    selectingPosition = False
                    selectingDirection = True
                    return
                if (i == 1 or i == 2 or i == 3):
                    insertAtRow(i, 0, 4, 1)
                    endOfSelection()
                    return
                if (i == 4):
                    disableAllButton()
                    enableButton(matrixOfButton[i-1][j])
                    enableButton(matrixOfButton[i][j+1])
                    selectingPosition = False
                    selectingDirection = True
                    return

            elif (j == 1 or j == 2 or j == 3):
                if (i == 0):
                    insertAtColumn(j, 0, 4, 1)
                    endOfSelection()
                elif (i == 4):
                    insertAtColumn(j, 4, 0, -1)
                    endOfSelection()

            if (j == 4):
                if (i == 0):
                    disableAllButton()
                    enableButton(matrixOfButton[i+1][j])
                    enableButton(matrixOfButton[i][j-1])
                    selectingPosition = False
                    selectingDirection = True
                    return
                if (i == 1 or i == 2 or i == 3):
                    insertAtRow(i, 4, 0, -1)
                    endOfSelection()
                    return
                if (i == 4):
                    disableAllButton()
                    enableButton(matrixOfButton[i-1][j])
                    enableButton(matrixOfButton[i][j-1])
                    selectingPosition = False
                    selectingDirection = True
                    return

    elif (selectingPosition == False and selectingDirection == True):
        # When choosing top right
        if (i == 0 and j == 1):
            insertAtRow(i, 0, 4, 1)
            endOfSelection()
            return

        elif (i == 1 and j == 0):
            insertAtColumn(j, 0, 4, 1)
            endOfSelection()
            return

        # When choosing top left
        elif (i == 0 and j == 3):
            insertAtRow(i, 4, 0, -1)
            endOfSelection()
            return
        elif (i == 1 and j == 4):
            insertAtColumn(j, 0, 4, 1)
            endOfSelection()
            return

        # When choosing bottom right
        elif (i == 4 and j == 1):
            insertAtRow(i, 0, 4, 1)
            endOfSelection()
            return
        elif (i == 3 and j == 0):
            insertAtColumn(j, 4, 0, -1)
            endOfSelection()
            return

        # When choosing bottom left
        elif (i == 4 and j == 3):
            insertAtRow(i, 4, 0, -1)
            endOfSelection()
            return
        elif (i == 3 and j == 4):
            insertAtColumn(j, 4, 0, -1)
            endOfSelection()
            return

        else:
            print("ERROR : Wrong case selected")
            return


def checkForWin():
    for i in range(0, 5):
        for j in range(0, 5):
            if (i != 0 and i != 4):
                if (matrixOfButton[i][j]['text'] != " "):
                    if (matrixOfButton[i][j]['text'] == matrixOfButton[i+1][j]['text'] and matrixOfButton[i][j]['text'] == matrixOfButton[i-1][j]['text']):
                        endGame(matrixOfButton[i][j]['text'])
            if (j != 0 and j != 4):
                if (matrixOfButton[i][j]['text'] != " "):
                    if (matrixOfButton[i][j]['text'] == matrixOfButton[i][j+1]['text'] and matrixOfButton[i][j]['text'] == matrixOfButton[i][j-1]['text']):
                        endGame(matrixOfButton[i][j]['text'])
            if (i != 0 and i != 4 and j != 0 and j != 4):
                if (matrixOfButton[i][j]['text'] != " "):
                    if (matrixOfButton[i][j]['text'] == matrixOfButton[i+1][j+1]['text'] and matrixOfButton[i][j]['text'] == matrixOfButton[i-1][j-1]['text']):
                        endGame(matrixOfButton[i][j]['text'])
                    if (matrixOfButton[i][j]['text'] == matrixOfButton[i+1][j-1]['text'] and matrixOfButton[i][j]['text'] == matrixOfButton[i-1][j+1]['text']):
                        endGame(matrixOfButton[i][j]['text'])


for i in range(0, 5):
    matrixOfButton.append(range(0, 5))
print(matrixOfButton[0][0])


for i in range(0, 5):
    for j in range(0, 5):
        matrixOfButton[i][j] = createButton(i, j)
        if(i != 0 and i != 4 and j != 0 and j != 4):
            disableButton(matrixOfButton[i][j])
        matrixOfButton[i][j].grid(row=i, column=j)


root.mainloop()
