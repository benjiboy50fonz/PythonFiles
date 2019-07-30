from pieces.piece import Piece

import chess


class King(Piece):
    def __init__(self, faction):
        # Faction should be either 0 or 1!

        self.board = chess.Chess.Board.board

        self.faction = faction
        self.id = chess.Chess.Id.king
        self.symbol = chess.Chess.Symbol.king

        self.colorString = chess.Chess.Color.relation[self.faction]

        self.possiblePos = []

    def getAvailablePos(self, currentX, currentY):
        self.getBoard()

        # Checks left and right.
        if currentY - 1 >= 0 and currentY + 1 <= 7:
            try:
                if not self.board[currentX][currentY - 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX, currentY - 1])
                    print('left')
            except IndexError:
                pass

            try:
                if not self.board[currentX][currentY + 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX, currentY + 1])
                    print('right')
            except IndexError:
                pass

        # Checks up and down.

        if currentX - 1 >= 0 and currentX + 1 <= 7:
            try:
                if not self.board[currentX - 1][currentY][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX - 1, currentY])
                    print('up')
            except IndexError:
                pass

            try:
                if not self.board[currentX + 1][currentY][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX + 1, currentY])
                    print('down')
            except IndexError:
                pass

        # Checks diagonals.

        if currentX - 1 >= 0 and currentX + 1 <= 7 and currentY - 1 >= 0 and currentY + 1 <= 7:
            try:
                if not self.board[currentX - 1][currentY - 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX - 1, currentY - 1])
                    print('1')
            except IndexError:
                pass

            try:
                if not self.board[currentX - 1][currentY + 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX - 1, currentY + 1])
                    print('2')
            except IndexError:
                pass

            try:
                if not self.board[currentX + 1][currentY - 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX + 1, currentY - 1])
                    print('3')
            except IndexError:
                pass

            try:
                if not self.board[currentX + 1][currentY + 1][1] == chess.Chess.Game.playerColor:
                    self.possiblePos.append([currentX + 1, currentY + 1])
                    print('4')
            except IndexError:
                pass

        return self.possiblePos

    def getBoard(self):
        self.board = chess.Chess.Board.board
