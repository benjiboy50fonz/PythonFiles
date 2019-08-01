class PlayerMove:
    def __init__(self):
        import chess

        super().__init__()
        self.board = chess.Chess.Board.board

        self.oppColor = chess.Chess.oppColor
        self.playerColor = chess.Chess.playerColor

        self.pieceStartX = 0
        self.pieceStartY = 0

        self.oldX = 0
        self.oldY = 0

    def playerMove(self):
        import chess

        self.getBoard()

        print('\nYour Move!')

        NotInt = True

        while NotInt:
            try:
                self.pieceStartY = int(input('What is the X value of the piece would you like to move?: '))
                self.pieceStartX = int(input('What is the Y value of the piece would you like to move?: '))

            except TypeError:
                print('\nPlease enter a valid integer!\n')
                continue
            if self.pieceStartX <= 0 or self.pieceStartX >= 9 or self.pieceStartY <= 0 or self.pieceStartY >= 9:
                print('\nPlease enter a valid integer!\n')
                continue

            if self.board[self.pieceStartX - 1][self.pieceStartY - 1][1] == self.oppColor:
                print('\nThat\'s not your piece!\n')
                continue

            if self.board[self.pieceStartX - 1][self.pieceStartY - 1][0] == ' ':
                print('\nThere\'s no piece there!\n')
                continue

            NotInt = False

        pieceId = self.board[self.pieceStartX - 1][self.pieceStartY - 1][0]
        pieceName = chess.Chess.Id.reverseRelation[pieceId]

        possibilities = chess.Chess.Piece.findPiece(pieceName, self.pieceStartX, self.pieceStartY)

        print('possibilities ' + str(possibilities))

        self.oldX = self.pieceStartX - 1
        self.oldY = self.pieceStartY - 1

        idiot = True
        while idiot:

            moveX = str(input('\nWhat is the X value of the space you would like to move the ' + \
                              pieceName[0].upper + pieceName[1:].lower() + ' to?: '))

            moveY = str(input('\nWhat is the Y value of the space you would like to move the ' + \
                              pieceName[0].upper + pieceName[1:].lower() + ' to?: '))
            try:
                if [int(moveX), int(moveY)] in possibilities:
                    self.setEmpty()  # sets your previous position as empty.
                    if self.board[moveX][moveY][1] == chess.Ches.oppColor:
                        self.replaceEnemy(moveX, moveY, pieceId)

                    idiot = False

            except TypeError:
                print('\nPlease enter a valid integer!\n')
                continue

    def getBoard(self):
        import chess

        self.board = chess.Chess.Board.board

    def setEmpty(self):
        self.board[self.oldX][self.oldY][0] = ' '
        self.board[self.oldX][self.oldY][1] = ' '

    def replaceEnemy(self, x, y, yourId):
        import chess

        enemyId = self.board[x][y][0]

        self.board[x][y][0] = yourId
        self.board[x][y][1] = chess.Chess.playerColor

        chess.Chess.Piece.removeEnemyPiece(enemyId)
