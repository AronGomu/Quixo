import Tkinter
import tkMessageBox


class View:

    def __init__(self, title):
        self.root = Tkinter.Tk()
        self.root.title(title)

        self.selectingPosition = False
        self.selectingDirection = False
        self.tempBtnClickedInfo = None

        self.matrixOfButton = []

        for i in range(0, 5):
            self.matrixOfButton.append(range(0, 5))

    def enableAllPossibleButton(self, activePlayerSymbol):
        for i in range(0, 5):
            for j in range(0, 5):
                if (i == 0 or i == 4 or j == 0 or j == 4):
                    if (activePlayerSymbol == 'X'):
                        if (self.matrixOfButton[i][j]["text"] != 'O'):
                            self.matrixOfButton[i][j].configure(
                                state='normal', bg='grey')
                    elif (activePlayerSymbol == 'O'):
                        if (self.matrixOfButton[i][j]["text"] != 'X'):
                            self.matrixOfButton[i][j].configure(
                                state='normal', bg='grey')

    def disableAllButton(self):
        for i in range(0, 5):
            for j in range(0, 5):
                disableButton(self.matrixOfButton[i][j])

    def createButton(self):
        return Tkinter.Button(self.root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8)


def enableButton(button):
    button.configure(state='normal', bg='grey')


def disableButton(button):
    button.configure(state=Tkinter.DISABLED, bg='black')


def endGame(player):
    tkMessageBox.showinfo("Game Ended", player + " player win !")
    raise SystemExit
