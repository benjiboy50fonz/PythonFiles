from pieces.piece import Piece

import chess


class King(Piece):
    def __init__(self, faction):

        # Faction should be either 0 or 1!

        self.faction = faction
        self.id = chess.Chess.Id.king
        self.symbol = chess.Chess.Symbol.king

        self.colorString = chess.Chess.Color.relation[self.faction]