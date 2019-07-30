from pieces.piece import Piece

import chess


class Rook(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.faction = faction
        self.id = chess.Chess.Id.rook
        self.symbol = chess.Chess.Symbol.rook

        self.colorString = chess.Chess.Color.relation[self.faction]

    def move(self, currentX, currentY, moveToX, moveToY):
        self.getBoard()
        # Check possible movements based off of current position.

        self.possiblePositions = []
        self.possibleUp = []
        self.possibleDown = []

        # NOTE: The following part is different for each individual pieces's move set.

        up = currentX
        down = 8 - currentX

        for row in range(up):
            if row == currentX:
                continue
                # THIS ACTUALLY SHOULD NOT BE USED. INVESTIGATE.
                # This is the selected piece; you cannot moveto yourself.
            elif self.board[row][currentY][1] == chess.Chess.Game.playerColor:
                self.possibleUp = []
                # Checks to see if an allied piece
            else:
                self.possibleUp.append([row, currentY])

        for row in range(down):
            if row + currentX == currentX:
                continue
            elif self.board[row + currentX][currentY][1] == chess.Chess.Game.playerColor:
                break
                # Checks to see of an allied piece is blocking further progress.
            else:
                self.possibleUp.append([row + currentX, currentY])
    def getBoard(self):
        self.board = chess.Chess.Board.chess