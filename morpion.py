import Tkinter
import tkMessageBox
root = Tkinter.Tk()
root.title("Quixo")


bclick = True


def createButton(i, j):
    return Tkinter.Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(matrixOfButton[i][j]))


def disableButton(button):
    button.configure(state=Tkinter.DISABLED)


def endGame(player):
    tkMessageBox.showinfo("Game Ended", player + " player win !")
    raise SystemExit


def btnClick(buttons):
    global bclick
    if (buttons["text"] != "O" and buttons["text"] != "X" and bclick == True):
        buttons["text"] = "X"
        bclick = False
        disableButton(buttons)
        checkForWin()

    elif (buttons["text"] != "O" and buttons["text"] != "X" and bclick == False):
        buttons["text"] = "O"
        bclick = True
        disableButton(buttons)
        checkForWin()
    else:
        print("ERROR : THIS BUTTON SHOULD NOT BE CLICKABLE")


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


matrixOfButton = []
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
