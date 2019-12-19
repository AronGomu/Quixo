import player
import ai_factory
import random


class Model:

    def __init__(self):
        # creating an ai
        self.aiFactory = ai_factory.AiFactory()
        self.ai = self.aiFactory.createAi("default")

        # creating the players
        self.playerX = player.Player('X', False)
        self.playerO = player.Player('O', False)
        self.playerX.next = self.playerO
        self.playerO.next = self.playerX

        # generate randomly the first player
        if random.randrange(0, 2, 1) == 0:
            self.activePlayer = self.playerX
        else:
            self.activePlayer = self.playerO

        # create the board
        self.board = []
        for i in range(0, 5):
            self.board.append(range(0, 5))

        for i in range(0, 5):
            for j in range(0, 5):
                self.board[i][j] = " "

    def swapPlayer(self):
        self.activePlayer = self.activePlayer.getNext()

    def getPlayerSymbol(self):
        return self.activePlayer.symbol

    def insertAtRow(self, i, start, end, increment, tempBtnClickedInfo):
        self.board[tempBtnClickedInfo[1]
                   ][tempBtnClickedInfo[2]] = 'VOID'
        temp = self.board[i][start]
        temp2 = None
        self.board[i][start] = self.getPlayerSymbol()
        for iterator in range(start+increment, end+increment, increment):
            if (temp == 'VOID'):
                break
            temp2 = self.board[i][iterator]
            self.board[i][iterator] = temp
            temp = temp2

    def insertAtColumn(self, j, start, end, increment, tempBtnClickedInfo):
        self.board[tempBtnClickedInfo[1]
                   ][tempBtnClickedInfo[2]] = 'VOID'
        temp = self.board[start][j]
        temp2 = None
        self.board[start][j] = self.getPlayerSymbol()
        for iterator in range(start+increment, end+increment, increment):
            if (temp == 'VOID'):
                break
            temp2 = self.board[iterator][j]
            self.board[iterator][j] = temp
            temp = temp2

    def checkForWin(self):
        for i in range(0, 5, 1):
            if (self.board[i][0] != " "):
                if (self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] == self.board[i][4]):
                    return self.board[i][0]
        for j in range(0, 5, 1):
            if (self.board[0][j] != " "):
                if (self.board[0][j] == self.board[1][j] == self.board[2][j] == self.board[3][j] == self.board[4][j]):
                    return self.board[0][j]
        if (self.board[0][0] != " "):
            if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == self.board[4][4]):
                return self.board[0][0]
        if (self.board[0][4] != " "):
            if (self.board[0][4] == self.board[1][3] == self.board[2][2] == self.board[3][1] == self.board[4][0]):
                return self.board[0][4]
        return None

    def endOfTurn(self):
        winner = self.checkForWin()
        if (self.checkForWin() is not None):
            return winner
        self.swapPlayer()
        if (self.activePlayer.is_ai == True):
            self.aiPlay()

    def aiPlay(self):
        self.board = self.ai.findBestPlay(self.board, self.activePlayer)
        self.checkForWin()
        self.swapPlayer()
        if (self.activePlayer.is_ai == True):
            self.aiPlay()
        else:
            return
