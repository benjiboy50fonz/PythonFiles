from config import ColorString, PieceFaction, SquareColor, PieceSymbol

from pieceids import Id
from gameplay.start import Gameplay

class Chess:
    pass

# Dummy class to store objects.

Chess = Chess()

Chess.Faction = PieceFaction()
Chess.Square = SquareColor()
Chess.Symbol = PieceSymbol()
Chess.Color = ColorString()

Chess.Id = Id()

Chess.Game = Gameplay()
Chess.totalPlayerPieces = Chess.Game.totalPlayerPieces
Chess.totalOppPieces = Chess.Game.totalOppPieces