import chess


class Setboard:
    def __init__(self):
        pass

    @staticmethod
    def idToColoredSymbol(id, faction):
        symbol = chess.Chess.Symbol.relation[id]

        colorString = chess.Chess.Color.relation[faction]

        print(colorString + symbol)


