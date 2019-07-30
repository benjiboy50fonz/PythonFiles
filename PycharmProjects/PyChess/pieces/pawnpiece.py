from pieces.piece import Piece

import chess


class Pawn(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.board = chess.Chess.Board.board

        self.faction = faction
        self.id = chess.Chess.Id.pawn
        self.symbol = chess.Chess.Symbol.pawn

        self.colorString = chess.Chess.Color.relation[self.faction]

        self.possiblePos = []

    def getAvailablePos(self, currentX, currentY):
        self.getBoard()
        if chess.Chess.playerColor == chess.Chess.Faction.white:
            possibleX = currentX + 1
            if possibleX > 7:
                return []

            try:
                if self.board[possibleX][currentY + 1][1] == chess.Chess.Game.playerColor:
                    pass
                else:
                    self.possiblePos.append([possibleX, currentY + 1])

            except IndexError:
                pass

            try:
                if self.board[possibleX][currentY - 1][1] == chess.Chess.Game.playerColor:
                    pass
                else:
                    self.possiblePos.append([possibleX, currentY - 1])

            except IndexError:
                pass

        # Checks from the black point of view.

        else:
            possibleX = currentX - 1
            if possibleX < 0:
                return []

            try:
                if self.board[possibleX][currentY + 1][1] == chess.Chess.Game.playerColor:
                    pass
                else:
                    self.possiblePos.append([possibleX, currentY + 1])

            except IndexError:
                pass

            try:
                if self.board[possibleX][currentY - 1][1] == chess.Chess.Game.playerColor:
                    pass
                else:
                    self.possiblePos.append([possibleX, currentY - 1])

            except IndexError:
                pass

        return self.possiblePos

    def getBoard(self):
        self.board = chess.Chess.Board.board
