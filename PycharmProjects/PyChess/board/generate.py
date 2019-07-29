class ChessBoard:
    def __init__(self):
        from board.setboard import Setboard

        self.SetBoard = Setboard()

        # Look as if it were an actual board, (0 = -id of piece {' ' if vacant}, 0 = faction of piece {' ' if vacant},
        # 0 = color of square {White = 0, Black = 1})

        self.board = [
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)]
        ]

    def startBoard(self):
        self.board = [
            [(4, 0, 0), (2, 0, 1), (3, 0, 0), (0, 0, 1), (1, 0, 0), (3, 0, 1), (2, 0, 0),
             (4, 0, 1)],
            [(5, 0, 1), (5, 0, 0), (5, 0, 1), (5, 0, 0), (5, 0, 1), (5, 0, 0), (5, 0, 1),
             (5, 0, 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(5, 1, 1), (5, 1, 0), (5, 1, 1), (5, 1, 0), (5, 1, 1), (5, 1, 0), (5, 1, 1),
             (5, 1, 0)],
            [(4, 1, 0), (2, 1, 1), (3, 1, 0), (0, 1, 1), (1, 1, 0), (3, 1, 1), (2, 1, 0),
             (4, 1, 1)],
        ]

    def resetBoard(self):
        # Do not touch this reset.

        self.board = [
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
            [(' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0),
             (' ', ' ', 1)],
            [(' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1), (' ', ' ', 0), (' ', ' ', 1),
             (' ', ' ', 0)],
        ]

    def generateTop(self):
        import chess

        color = chess.Chess.Color.black

        values = []

        for val in range(8):
            values.append(str(self.SetBoard.idToColoredSymbol(self.board[0][val][0], self.board[0][val][1])))

        string = color + \
                 '''                -----------------------------------------------------------------------------------------------------------------
                |             |             |             |             |             |             |             |             |
                |             |             |             |             |             |             |             |             |                                                                            
                |      ''' + values[0] + '''      |      ''' + values[1] + '''      |      ''' + values[
                     2] + '''      |      ''' + values[3] + '''      |      ''' + values[4] + '''      |      ''' + \
                 values[5] + '''      |      ''' + values[6] + '''      |      ''' + values[7] + '''      |
                |             |             |             |             |             |             |             |             |
                |             |             |             |             |             |             |             |             |
    '''

        return string

    def generateMiddle(self):
        import chess

        color = chess.Chess.Color.black

        finalString = ''

        for row in range(6):
            row += 1
            values = []
            for val in range(8):
                values.append(str(self.SetBoard.idToColoredSymbol(self.board[row][val][0], self.board[row][val][1])))

            if row == 1:
                string = color + \
                         '''            -----------------------------------------------------------------------------------------------------------------                                                                                                                                                                                  
                |             |             |             |             |             |             |             |             |                            
                |             |             |             |             |             |             |             |             |                                                                                                                                                                
                |      ''' + values[0] + '''      |      ''' + values[1] + '''      |      ''' + values[
                             2] + '''      |      ''' + values[3] + '''      |      ''' + values[
                             4] + '''      |      ''' + \
                         values[5] + '''      |      ''' + values[6] + '''      |      ''' + values[7] + '''      |
                |             |             |             |             |             |             |             |             |                                                                                                                                                                
                |             |             |             |             |             |             |             |             |                                                                                                                                                                                                                                                                    
    '''
            else:
                string = color + \
                         '''            -----------------------------------------------------------------------------------------------------------------                                                                                                                                                                                  
                |             |             |             |             |             |             |             |             |                            
                |             |             |             |             |             |             |             |             |                                                                                                                                                                
                |      ''' + values[0] + '''      |      ''' + values[1] + '''      |      ''' + values[
                             2] + '''      |      ''' + values[3] + '''      |      ''' + values[
                             4] + '''      |      ''' + \
                         values[5] + '''      |      ''' + values[6] + '''      |      ''' + values[7] + '''      |     
                |             |             |             |             |             |             |             |             |                                                                                                                                                                
                |             |             |             |             |             |             |             |             |                                                                                                                                                                                                                                                                         
    '''

            finalString += string

        return finalString

    def generateBottom(self):
        import chess

        color = chess.Chess.Color.black

        values = []

        for val in range(8):
            values.append(str(self.SetBoard.idToColoredSymbol(self.board[7][val][0], self.board[7][val][1])))

        string = color + \
                 '''            -----------------------------------------------------------------------------------------------------------------                
                |             |             |             |             |             |             |             |             |
                |             |             |             |             |             |             |             |             |                                                                            
                |      ''' + values[0] + '''      |      ''' + values[1] + '''      |      ''' + values[
                     2] + '''      |      ''' + values[3] + '''      |      ''' + values[4] + '''      |      ''' + \
                 values[5] + '''      |      ''' + values[6] + '''      |      ''' + values[7] + '''      |
                |             |             |             |             |             |             |             |             |
                |             |             |             |             |             |             |             |             |
                -----------------------------------------------------------------------------------------------------------------
       '''

        return string

    def regenerate(self):
        topString = self.generateTop()
        middleString = self.generateMiddle()
        bottomString = self.generateBottom()

        print(topString + middleString + bottomString)
