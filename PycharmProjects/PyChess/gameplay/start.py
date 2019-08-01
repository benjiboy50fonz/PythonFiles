class Gameplay():
    def __init__(self):
        from chess import Chess

        self.totalPlayerPieces = []
        self.totalOppPieces = []

        self.oppColor = ''
        self.playerColor = ''

        self.playerStart = True
        self.gameOn = True

        self.startGame()
        Chess.Board.startBoard()
        self.generatePieces()

    def generatePieces(self):
        from pieces.kingpiece import King
        from pieces.queenpiece import Queen
        from pieces.knightpiece import Knight
        from pieces.bishoppiece import Bishop
        from pieces.rookpiece import Rook
        from pieces.pawnpiece import Pawn

        for king in range(1):
            self.totalPlayerPieces.append([King(0), 0])
            self.totalOppPieces.append([King(1), 0])

        for queen in range(1):
            self.totalPlayerPieces.append([Queen(0), 1])
            self.totalOppPieces.append([Queen(1), 1])

        for knight in range(2):
            self.totalPlayerPieces.append([Knight(0), 2])
            self.totalOppPieces.append([Knight(1), 2])

        for bishop in range(2):
            self.totalPlayerPieces.append([Bishop(0), 3])
            self.totalOppPieces.append([Bishop(1), 3])

        for rook in range(2):
            self.totalPlayerPieces.append([Rook(0), 4])
            self.totalOppPieces.append([Rook(1), 4])

        for pawn in range(8):
            self.totalPlayerPieces.append([Pawn(0), 5])
            self.totalOppPieces.append([Pawn(1), 5])

    def startGame(self):
        import chess

        nullSpace = chess.Chess.Color.black

        print('\n' + nullSpace + 'Welcome to PyChess!\n')

        wrong = True
        self.playerStart = True

        while wrong:
            first = input(nullSpace + 'Would you like to start? (\'Yes\' or \'No\'): ')
            if str(first.lower()) == 'no':
                self.playerStart = False
            elif str(first.lower()) == 'yes':
                pass
            else:
                print('\nPlease enter \'Yes\' or \'No\'!')
                continue

            wrong = False

        dumb = True
        while dumb:
            color = input('Would you like to be red or black?: ')
            if str(color.lower()) == 'red':
                self.playerColor = chess.Chess.Faction.white
                self.oppColor = chess.Chess.Faction.black
            elif str(color.lower()) == 'black':
                self.playerColor = chess.Chess.Faction.black
                self.oppColor = chess.Chess.Faction.white
            else:
                print('\nPlease enter \'Red\' or \'Black\'!\n')
                continue
            dumb = False

    def turnCycle(self):
        import chess

        chess.Chess.Board.regenerate()

        if not self.playerStart:
            pass

        while self.gameOn:
            playerResult = chess.Chess.Player.playerMove()
            if playerResult == 'error':
                continue

