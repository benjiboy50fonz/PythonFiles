class Piece:

    # Parent class, uniting all child classes. Put universal piece methods here.

    @staticmethod
    def removePiece(self, piece):
        import chess

        playerPieces = chess.Chess.totalPlayerPieces
