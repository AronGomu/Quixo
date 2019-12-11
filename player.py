class Player:

    def __init__(self, symbol, is_ai):
        self.symbol = symbol
        self.is_ai = is_ai
        self.next = None

    def getNext(self):
        return self.next
