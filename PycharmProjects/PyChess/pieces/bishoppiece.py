from pieces.piece import Piece

import chess


class Bishop(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.board = chess.Chess.Board.board

        self.faction = faction
        self.id = chess.Chess.Id.bishop
        self.symbol = chess.Chess.Symbol.bishop

        self.colorString = chess.Chess.Color.relation[self.faction]

        self.possibleUpLeft = []
        self.possibleUpRight = []
        self.possibleDownLeft = []
        self.possibleDownRight = []

        self.total = []

    def getAvailablePos(self, currentX, currentY):
        up = currentX
        down = 8 - currentX

        countX = currentX
        countY = currentY

        self.possibleUpLeft = []
        self.possibleUpRight = []
        self.possibleDownLeft = []
        self.possibleDownRight = []

        # Checks up and left diagonal.

        for pos in range(up):
            countX -= 1
            countY -= 1
            if countX < 0 or countY < 0:
                break
            if self.board[countX][countY][1] == chess.Chess.Game.playerColor:
                break
            elif self.board[countX][countY][1] == chess.Chess.Game.oppColor:
                self.possibleUpLeft.append([countX, countY])
                break
            else:
                self.possibleUpLeft.append([countX, countY])

        countX = currentX
        countY = currentY

        # Checks up and right diagonal.

        for pos in range(up):
            countX -= 1
            countY += 1
            if countX < 0 or countY < 0:
                break
            if self.board[countX][countY][1] == chess.Chess.Game.playerColor:
                break
            elif self.board[countX][countY][1] == chess.Chess.Game.oppColor:
                self.possibleUpRight.append([countX, countY])
                break
            else:
                self.possibleUpRight.append([countX, countY])

        countX = currentX
        countY = currentY

        # Checks down and left diagonal.

        for pos in range(down):
            countX += 1
            countY -= 1
            if countX < 0 or countY < 0:
                break
            if self.board[countX][countY][1] == chess.Chess.Game.playerColor:
                break
            elif self.board[countX][countY][1] == chess.Chess.Game.oppColor:
                self.possibleDownLeft.append([countX, countY])
                break
            else:
                self.possibleDownLeft.append([countX, countY])

        countX = currentX
        countY = currentY

        # Checks down and right diagonal.

        for pos in range(down):
            countX += 1
            countY += 1
            if countX < 0 or countY < 0:
                break
            if self.board[countX][countY][1] == chess.Chess.Game.playerColor:
                break
            elif self.board[countX][countY][1] == chess.Chess.Game.oppColor:
                self.possibleDownRight.append([countX, countY])
                break
            else:
                self.possibleDownRight.append([countX, countY])

        self.total = self.possibleUpLeft + self.possibleUpRight + self.possibleDownLeft + self.possibleDownRight

        if [currentX, currentY] in self.total:
            self.total.remove([currentX, currentY])

        return self.total

    def getBoard(self):
        self.board = chess.Chess.Board.board
