import ai


class AiFactory:

    def __init__(self):
        pass

    def createAi(self, type):
        if (type == "default"):
            return ai.Ai()
        else:
            return ai.Ai()
