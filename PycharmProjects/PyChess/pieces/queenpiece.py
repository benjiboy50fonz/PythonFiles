from pieces.piece import Piece

import chess


class Queen(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.faction = faction
        self.id = chess.Chess.Id.queen
        self.symbol = chess.Chess.Symbol.queen

        self.colorString = chess.Chess.Color.relation[self.faction]