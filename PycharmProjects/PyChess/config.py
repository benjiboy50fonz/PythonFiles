class ColorString:

    def __init__(self):
        import chess

        # Color of piece occupying a certain space.

        self.white = "\033[1;31;47m"
        # is actually displayed as red lol

        self.black = "\033[1;30;47m"

        factionOne = chess.Chess.Faction.white
        factionTwo = chess.Chess.Faction.black
        emptyFaction = ' '

        self.relation = {
                        factionOne : self.white,
                        factionTwo : self.black,
                        emptyFaction : self.black
                        }


class PieceFaction:
    def __init__(self):
        self.white = 0
        self.black = 1


class SquareColor:
    def __init__(self):
        self.white = 0
        self.black = 1


class PieceSymbol:
    def __init__(self):
        self.king = 'K'
        self.queen = 'Q'
        self.knight = 'H'
        self.bishop = 'B'
        self.rook = 'R'
        self.pawn = 'P'
        self.emptySign = ' '

        self.relation = {
                        0 : self.king,
                        1 : self.queen,
                        2 : self.knight,
                        3 : self.bishop,
                        4 : self.rook,
                        5 : self.pawn,
                        ' ' : self.emptySign
                        }
