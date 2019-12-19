
import view
import model


class Controller:

    __instance = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
            return cls.__instance


    def __init__(self, playerX_is_ai, playerO_is_ai):
        if not Controller.__instance:
            self.model = model.Model()
            self.view = view.View("Quixo")

            if (playerX_is_ai == 'ai'):
                self.model.playerX.is_ai = True
            else:
                playerX_is_ai = False

            if (playerO_is_ai == 'ai'):
                self.model.playerO.is_ai = True
            else:
                playerO_is_ai = False

            for i in range(0, 5):
                for j in range(0, 5):
                    self.view.matrixOfButton[i][j] = self.createButton(i, j)
                    if(i != 0 and i != 4 and j != 0 and j != 4):
                        view.disableButton(self.view.matrixOfButton[i][j])
                    self.view.matrixOfButton[i][j].grid(row=i, column=j)

            if (self.model.activePlayer.is_ai == True):
                self.model.aiPlay()
                self.setBoardFromSimplified(self.model.board)

            self.view.root.mainloop()
        else:
            self.getInstance()


    def createButton(self, i, j):
        button = self.view.createButton()
        button["command"] = command = lambda: self.btnClick(
            self.view.matrixOfButton[i][j], i, j)
        return button

    def btnClick(self, button, i, j):
        if (self.view.selectingPosition == False and self.view.selectingDirection == False):
            self.view.disableAllButton()
            if (i == 0):
                view.enableButton(self.view.matrixOfButton[4][j])
                if (j != 0):
                    view.enableButton(self.view.matrixOfButton[i][0])
                if (j != 4):
                    view.enableButton(self.view.matrixOfButton[i][4])
                self.view.tempBtnClickedInfo = [button, i, j]
                self.view.selectingPosition = True
            if (i == 4):
                view.enableButton(self.view.matrixOfButton[0][j])
                if (j != 0):
                    view.enableButton(self.view.matrixOfButton[i][0])
                if (j != 4):
                    view.enableButton(self.view.matrixOfButton[i][4])
                self.view.tempBtnClickedInfo = [button, i, j]
                self.view.selectingPosition = True
            if (j == 0):
                view.enableButton(self.view.matrixOfButton[i][4])
                if (i != 0):
                    view.enableButton(self.view.matrixOfButton[0][j])
                if (i != 4):
                    view.enableButton(self.view.matrixOfButton[4][j])
                self.view.tempBtnClickedInfo = [button, i, j]
                self.view.selectingPosition = True
            if (j == 4):
                view.enableButton(self.view.matrixOfButton[i][0])
                if (i != 0):
                    view.enableButton(self.view.matrixOfButton[0][j])
                if (i != 4):
                    view.enableButton(self.view.matrixOfButton[4][j])
                self.view.tempBtnClickedInfo = [button, i, j]
                self.view.selectingPosition = True

        elif (self.view.selectingPosition == True and self.view.selectingDirection == False):
            if (i == self.view.tempBtnClickedInfo[1] and j != self.view.tempBtnClickedInfo[2]):
                if (j == 0):
                    self.model.insertAtRow(
                        i, 0, 4, 1, self.view.tempBtnClickedInfo)
                    self.endOfSelection()
                elif (j == 4):
                    self.model.insertAtRow(
                        i, 4, 0, -1, self.view.tempBtnClickedInfo)
                    self.endOfSelection()

            elif (i != self.view.tempBtnClickedInfo[1] and j == self.view.tempBtnClickedInfo[2]):
                if (i == 0):
                    self.model.insertAtColumn(
                        j, 4, 0, 1, self.view.tempBtnClickedInfo)
                    self.endOfSelection()
                elif (i == 4):
                    self.model.insertAtColumn(
                        j, 4, 0, -1, self.view.tempBtnClickedInfo)
                    self.endOfSelection()

    def endOfSelection(self):
        self.setBoardFromSimplified(self.model.board)
        self.view.selectingPosition = False
        self.view.selectingDirection = False
        self.view.disableAllButton()
        winner = self.model.endOfTurn()
        if (winner is not None):
            view.endGame(winner)
        self.setBoardFromSimplified(self.model.board)
        self.view.enableAllPossibleButton(self.model.getPlayerSymbol())

    def getSimplifiedBoard(self):
        boardSimplified = []
        for i in range(0, 5):
            boardSimplified.append(range(0, 5))
        for i in range(0, 5):
            for j in range(0, 5):
                boardSimplified[i][j] = self.view.matrixOfButton[i][j]["text"]
        return boardSimplified

    def setBoardFromSimplified(self, boardSimplified):
        for i in range(0, 5):
            for j in range(0, 5):
                self.view.matrixOfButton[i][j]["text"] = boardSimplified[i][j]

        def aiPlay(self):
            self.model.aiPlay()
            self.setBoardFromSimplified(self.model.board)
