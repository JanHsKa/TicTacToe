from Player import*


class AIPlayer(Player):
    def __init__(self, name, figure):
        super(AIPlayer, self).__init__(name, figure)
        print("AIPlayer")
        print(self.figure)

