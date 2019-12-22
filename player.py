class Player:

    def __init__(self, symbol, is_ai):
        self.symbol = symbol
        self.is_ai = is_ai
        self.next = None

    # Funcstion to pass the turn
    def getNext(self):
        return self.next
