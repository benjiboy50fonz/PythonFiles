class PlayerMove:
    def __init__(self):
        import chess

        super().__init__()
        self.board = chess.Chess.Board.board

        self.oppColor = chess.Chess.oppColor
        self.playerColor = chess.Chess.playerColor

        self.pieceStartX = 0
        self.pieceStartY = 0

    def playerMove(self):
        self.getBoard()

        print('\nYour Move!')

        NotInt = True

        while NotInt:
            try:
                self.pieceStartX = int(input('What is the X value of the piece would you like to move?: '))
                self.pieceStartY = int(input('What is the Y value of the piece would you like to move?: '))

            except TypeError:
                print('\nPlease enter a valid integer!\n')
                continue
            if self.pieceStartX <= 0 or self.pieceStartX >= 9 or self.pieceStartY <= 0 or self.pieceStartY >= 9:
                print('\nPlease enter a valid integer!\n')
                continue

            if self.board[self.pieceStartX - 1][self.pieceStartY - 1][1] == self.oppColor:
                print('\nThat\'s not your piece!\n')
                continue

            NotInt = False

        print('you can move there')

    def getBoard(self):
        import chess

        self.board = chess.Chess.Board.board
