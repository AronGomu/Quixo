
import view
import model


class Quixo:

    def __init__(self):
        pass

    def getSimplifiedBoard(self):
        boardSimplified = []
        for i in range(0, 5):
            boardSimplified.append(range(0, 5))
        for i in range(0, 5):
            for j in range(0, 5):
                boardSimplified[i][j] = self.matrixOfButton[i][j]["text"]
        return boardSimplified

    def setBoardFromSimplified(self, boardSimplified):
        for i in range(0, 5):
            boardSimplified.append(range(0, 5))
        for i in range(0, 5):
            for j in range(0, 5):
                self.matrixOfButton[i][j]["text"] = boardSimplified[i][j]

    def launchApp(self, playerX_is_ai, playerO_is_ai):

        if (playerX_is_ai == 'ai'):
            self.playerX.is_ai = True
        else:
            playerX_is_ai = False

        if (playerO_is_ai == 'ai'):
            self.playerO.is_ai = True
        else:
            playerO_is_ai = False

        print("playerX.is_ai :", self.playerX.is_ai)
        print("playerO.is_ai :", self.playerO.is_ai)

        view.View()

        for i in range(0, 5):
            self.matrixOfButton.append(range(0, 5))

        for i in range(0, 5):
            for j in range(0, 5):
                self.matrixOfButton[i][j] = self.createButton(i, j)
                if(i != 0 and i != 4 and j != 0 and j != 4):
                    disableButton(self.matrixOfButton[i][j])
                self.matrixOfButton[i][j].grid(row=i, column=j)

        if (self.activePlayer.is_ai == True):
            self.aiPlay()

        self.root.mainloop()


def enableButton(button):
    button.configure(state='normal', bg='grey')


def disableButton(button):
    button.configure(state=Tkinter.DISABLED, bg='black')


def endGame(player):
    tkMessageBox.showinfo("Game Ended", player + " player win !")
    raise SystemExit
