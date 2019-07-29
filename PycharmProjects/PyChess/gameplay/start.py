class Gameplay:
    def __init__(self):
        self.totalPlayerPieces = []
        self.totalOppPieces = []

        self.generatePieces()

    def generatePieces(self):
        from pieces.kingpiece import King

        for king in range(2):
            self.totalPlayerPieces.append(King(0))
            self.totalOppPieces.append(King(1))
