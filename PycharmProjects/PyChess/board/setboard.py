import chess


class Setboard:
    def __init__(self):
        pass

    @staticmethod
    def idToColoredSymbol(_id, faction):
        symbol = chess.Chess.Symbol.relation[_id]

        colorString = chess.Chess.Color.relation[faction]

        if faction == 0:
            return colorString + symbol + chess.Chess.Color.black
        else:
            return colorString + symbol
