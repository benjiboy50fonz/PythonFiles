from config import ColorString, PieceFaction, SquareColor, PieceSymbol

from pieceids import Id

from gameplay.start import Gameplay
from gameplay.playermove import PlayerMove

from board.generate import ChessBoard

from pieces.piece import Piece


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

Chess.Piece = Piece()

from pieces.rookpiece import Rook

rook = Rook(0)
print(str(rook.getAvailablePos(3, 3)))

Chess.Game.turnCycle()
