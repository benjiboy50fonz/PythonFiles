class Piece:
    def __init__(self):
        import chess

        self.playerPieces = chess.Chess.totalPlayerPieces
        self.playerColor = chess.Chess.playerColor

    # Parent class, uniting all child classes. Put universal piece methods here.

    @staticmethod
    def removeEnemyPiece(self, enemyId):
        import chess

        self.oppPieces = chess.Chess.totalOppPieces

        found = False

        for obj in self.oppPieces:
            if obj[1] == enemyId:
                found = True

        if found:
            self.oppPieces.remove(obj)

        chess.Chess.totalOppPieces = self.oppPieces
        return self.oppPieces

    def findPiece(self, piece, x, y):
        possible = []

        print(self.playerPieces)
        print(x)
        print(y)

        if piece == 'king':
            for obj in self.playerPieces:
                if obj[1] == 0:
                    possible = obj[0].getAvailablePos(x, y)
                    print('king')

        elif piece == 'queen':
            for obj in self.playerPieces:
                if obj[1] == 1:
                    possible = obj[0].getAvailablePos(x, y)
                    print('queen')

        elif piece == 'knight':
            for obj in self.playerPieces:
                if obj[1] == 2:
                    possible = obj[0].getAvailablePos(x, y)
                    print('knight')

        elif piece == 'bishop':
            for obj in self.playerPieces:
                if obj[1] == 3:
                    possible = obj[0].getAvailablePos(x, y)
                    print('bishop')

        elif piece == 'rook':
            for obj in self.playerPieces:
                if obj[1] == 4:
                    possible = obj[0].getAvailablePos(x, y)
                    print('rook')

        elif piece == 'pawn':
            for obj in self.playerPieces:
                if obj[1] == 5:
                    possible = obj[0].getAvailablePos(x, y)
                    print('ran')

        return possible
