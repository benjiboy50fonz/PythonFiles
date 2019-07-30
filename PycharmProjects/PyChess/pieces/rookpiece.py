from pieces.piece import Piece

import chess


class Rook(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.board = chess.Chess.Board.board
        self.faction = faction
        self.id = chess.Chess.Id.rook
        self.symbol = chess.Chess.Symbol.rook

        self.colorString = chess.Chess.Color.relation[self.faction]

        self.possibleUp = []
        self.possibleDown = []

        self.possibleLeft = []
        self.possibleRight = []

        self.verticalPos = []
        self.horizontalPos = []

    def getAvailablePos(self, currentX, currentY):
        self.getBoard()
        # Check possible movements based off of current position.

        self.possibleUp = []
        self.possibleDown = []

        self.possibleLeft = []
        self.possibleRight = []

        # NOTE: The following part is different for each individual pieces's move set.

        up = currentX
        down = 8 - currentX

        for row in range(up):

            if row == currentX:
                continue
                # THIS ACTUALLY SHOULD NOT BE USED. INVESTIGATE.
                # This is the selected piece; you cannot move to yourself.
            elif self.board[row][currentY][1] == chess.Chess.Game.playerColor:
                self.possibleUp = []
                # Checks to see if an allied piece
            elif self.board[row][currentY][1] == chess.Chess.Game.oppColor:
                self.possibleUp = []
                self.possibleUp.append([row, currentY])
            else:
                self.possibleUp.append([row, currentY])

        for row in range(down):
            if row + currentX == currentX:
                continue
            elif self.board[row + currentX][currentY][1] == chess.Chess.Game.playerColor:
                break
                # Checks to see of an allied piece is blocking further progress.
            elif self.board[row + currentX][currentY][1] == chess.Chess.Game.oppColor:
                self.possibleDown.append([row + currentX, currentY])
                break
            else:
                self.possibleDown.append([row + currentX, currentY])

        self.verticalPos = self.possibleUp + self.possibleDown

        # NOTE: Above is currently working. Provides possible vertical movements based off of standard chess rules.
        # The following will check horizontal movements.

        left = currentY
        right = 8 - currentY

        for column in range(left):
            if column == currentY:
                continue
            elif self.board[currentX][column][1] == chess.Chess.Game.playerColor:
                self.possibleLeft = []
            elif self.board[currentX][column][1] == chess.Chess.Game.oppColor:
                self.possibleLeft = []
                self.possibleLeft.append([currentX, column])
            else:
                self.possibleLeft.append([currentX, column])

        for column in range(right):
            if column + currentY == currentY:
                continue
            elif self.board[currentX][column + currentY][1] == chess.Chess.Game.playerColor:
                break
            elif self.board[currentX][column + currentY][1] == chess.Chess.Game.oppColor:
                self.possibleRight.append([currentX, column + currentY])
                break
            else:
                self.possibleRight.append([currentX, column + currentY])

        self.horizontalPos = self.possibleLeft + self.possibleRight

        return self.verticalPos + self.horizontalPos

        # This code appears to be 100% correct and functional.

    def getBoard(self):
        self.board = chess.Chess.Board.board
