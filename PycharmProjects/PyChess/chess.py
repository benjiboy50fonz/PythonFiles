from config import ColorString, PieceFaction, SquareColor, PieceSymbol

from pieceids import Id

from gameplay.start import Gameplay
from gameplay.playermove import PlayerMove

from board.generate import ChessBoard


class Chess:
    pass


# Dummy class to store objects.

Chess = Chess()

Chess.Faction = PieceFaction()
Chess.Square = SquareColor()
Chess.Symbol = PieceSymbol()
Chess.Color = ColorString()

Chess.Board = ChessBoard()
Chess.Id = Id()

Chess.Game = Gameplay()

Chess.playerColor = Chess.Game.playerColor
Chess.oppColor = Chess.Game.oppColor

Chess.Player = PlayerMove()

Chess.totalPlayerPieces = Chess.Game.totalPlayerPieces
Chess.totalOppPieces = Chess.Game.totalOppPieces

Chess.Game.turnCycle()
