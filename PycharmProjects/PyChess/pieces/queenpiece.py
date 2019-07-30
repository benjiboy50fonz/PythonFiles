from pieces.piece import Piece

import chess


class Queen(Piece):
    def __init__(self, faction):

        self.board = chess.Chess.Board.board

        # Faction should be either 0 or 1!

        self.faction = faction
        self.id = chess.Chess.Id.queen
        self.symbol = chess.Chess.Symbol.queen

        self.colorString = chess.Chess.Color.relation[self.faction]

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

        return self.verticalPos + self.horizontalPos + self.total


    def getBoard(self):
        self.board = chess.Chess.Board.board
