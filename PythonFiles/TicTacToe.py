def generateGroup(list_, num=0):
        # TODO Figure this out 
        return '''                  _________________________
                  |       |       |       |
                  |       |       |       |
                  |   ''' + str(list_[num][0]) + '''   |   ''' + str(list_[num][1]) + '''   |   ''' + str(list_[num][2]) + '''   |
                  |       |       |       |
                  |_______|_______|_______|'''
class Chess():

    import numpy as np
    
    def __init__(self):

        # X is 1, O is 2

        self.nullList = [[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']
                         ]
        
        print(generateGroup(self.nullList))
        print(generateGroup(self.nullList))
        print(generateGroup(self.nullList))

        self.startGame()

    def startGame(self):
        print('Welcome to the unbeatable game!')

        self.aiMiddle = False
        self.corners = [[0,0], [0,2], [2,0], [2,2]]
        self.sides = [[0,1], [1,0], [1,2], [2,1]]

        
        incorrect = True
        while incorrect: 
            choice = input('\nType \'1\' for X\'s or \'2\' for O\'s: ')
            if str(choice) == '1':
                print('\nYou chose X\'s!')
                self.playerSymbol = 'X'
                self.aiSymbol = 'O'
                incorrect = False

            elif str(choice) == '2':
                print('\nYou chose Y\'s!')
                self.playerSymbol = 'O'
                self.aiSymbol = 'X'
                incorrect = False

            else:
                print('\nPlease enter \'1\' or \'2\'!')
                continue

        self.gameOn = True

        self.generateField()

        while self.gameOn:
            self.playerMove()
            self.aiMove()


        # Add the game moves here

    def generateField(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' '],
                     ]

    def playerMove(self):
        wrong = True
        print('\nYour move!')
        while wrong:
            row = input('\nEnter a Row Number (1, 2, 3): ')
            if ('.' not in str(row)) and (int(row) <= 3 and int(row) >= 1):
                pass
            else:
                print('\nPlease enter 1, 2, or 3!')
                continue

            column = input('\nEnter a Column Number (1, 2, 3): ')
            if ('.' not in str(column)) and (int(column) <= 3 and int(column) >= 1):
                pass
            else:
                print('\nPlease enter 1, 2, or 3!')
                continue
            
            if self.board[int(row) - 1][int(column) - 1] != ' ':
                print('\nThat Space is Taken! Please choose another!')
                continue

            wrong = False

        self.board[int(row) - 1][int(column) - 1] = self.playerSymbol
        self.updateBoard()


    def aiMove(self):
        print('\nOpponent\'s Turn!\n')

        if self.checkHorizontal():
            if self.board[self.placeRow][self.placeColumn] != ' ':
                pass
            else:
                self.board[self.placeRow][self.placeColumn] = self.aiSymbol
                self.updateBoard()
                return True

        if self.checkVertical():
            if self.board[self.placeRow][self.placeColumn] != ' ':
                pass
            else:
                self.board[self.placeRow][self.placeColumn] = self.aiSymbol
                self.updateBoard()
                return True
        
        if self.checkDiagonal():
            if self.board[self.placeRow][self.placeColumn] != ' ':
                pass
            else:
                self.board[self.placeRow][self.placeColumn] = self.aiSymbol
                self.updateBoard()
                return True

        else:
            self.aiScore()

            # Add scoring intelligence here
            
    def checkHorizontal(self):
        row = -1
        none = 0
        for i in self.board:
            row += 1
            count = 0
            for x in i:
                if x == self.playerSymbol:
                    count += 1

            if count == 2:

                # Finds the empty spot in row, and takes it. 

                for x in i:
                    if x == ' ':
                        self.placeColumn = i.index(x)
                        self.placeRow = row

            else:
                none += 1
                continue 
        if none == 3:
            return False

        else:
            return True


    def checkVertical(self):
        # Oof.

        self.left = []
        self.middle = []
        self.right = []
        
        for i in self.board:
            for x in i:
                pos = i.index(x)
                if x == self.playerSymbol:
                    if pos == 0:
                        self.left.append(self.playerSymbol)
                    elif pos == 1:
                        self.middle.append(self.playerSymbol)
                    else:
                        self.right.append(self.playerSymbol)
                else:
                    if pos == 0:
                        self.left.append('0')
                    elif pos == 1:
                        self.middle.append('0')
                    else:
                        self.right.append('0')
        
        clearOne = False
        clearTwo = False
        clearThree = False
                     
        count = 0
        for i in self.left:
            if i == self.playerSymbol:
                count += 1
        if count == 2:
            self.placeRow = self.left.index('0')
            self.placeColumn = 0

        else:
            clearOne = True

        count = 0
        for i in self.middle:
            if i == self.playerSymbol:
                count += 1
        if count == 2:
            self.placeRow = self.left.index('0')
            self.placeColumn = 1
        
        else:
            clearTwo = True
            
        count = 0
        for i in self.right:
            if i == self.playerSymbol:
                count += 1
        if count == 2:
            self.placeRow = self.left.index('0')
            self.placeColumn = 2

        else:
            clearThree = True

        if clearThree and clearTwo and clearOne:
            return False
        else:
            return True

    def checkDiagonal(self):
        # Mega-Oof

        #Only Two diagonals. check each individually.

        LeftRightCount = 0
        RightLeftCount = 0
    
        if self.board[0][0] == self.playerSymbol:
            LeftRightCount += 1

        if self.board[1][1] == self.playerSymbol:
            LeftRightCount += 1
                        
        if self.board[2][2] == self.playerSymbol:
            LeftRightCount += 1

        if LeftRightCount == 2:
            num = -1
            for i in range(3):
                num += 1
                if not self.board[num][num] == self.playerSymbol:
                    self.placeRow = num
                    self.placeColumn = num

            return True
                    
                    
        if self.board[0][2] == self.playerSymbol:
            RightLeftCount += 1

        if self.board[1][1] == self.playerSymbol:
            RightLeftCount += 1
                        
        if self.board[2][0] == self.playerSymbol:
            RightLeftCount += 1

        if RightLeftCount == 2:
            num = -1
            for i in range(3):
                num += 1
                if not self.board[0][2] == self.playerSymbol:
                    self.placeRow = 0
                    self.placeColumn = 2           

                if not self.board[1][1] == self.playerSymbol:
                    self.placeRow = 1
                    self.placeColumn = 1

                if not self.board[2][0] == self.playerSymbol:
                    self.placeRow = 2
                    self.placeColumn = 0
            return True

        else:
            return False

    def aiScore(self):
        cornerCheck, posRow, posColumn = self.checkCorners()
        dualCorners, posRowTwo, posColumnTwo = self.checkDualCorners()
        sideCheck, posRowThree, posColumnThree = self.checkSides()
        dualSides, PosRowFour, posColumnFour = self.checkDualSides()
        
        # Insert check win here.
        
        if self.board[1][1] == ' ':
            self.board[1][1] = self.aiSymbol
            self.updateBoard()
            return True
        elif self.aiMiddle and dualCorners:
            self.board[posRowTwo][posRowColumn] = self.aiSymbol
            self.updateBoard()
            return True
        elif self.aiMiddle and cornerCheck:
            self.board[posRow][posColumn] = self.aiSymbol
            self.updateBoard()
            return True
        elif self.aiMiddle and dualSides:
            self.board[posRowFour][posColumnFour] = self.aiSymbol
            self.updateBoard()
            return True
        elif self.aiMiddle and sideCheck:
            self.board[posRowThree][posColumnThree] = self.aiSymbol
            self.updateBoard()
            return True
        elif dualCorners:
            self.board[posRowTwo][posRowColumn] = self.aiSymbol
            self.updateBoard()
            return True
        elif cornerCheck:
            self.board[posRow][posColumn] = self.aiSymbol
            self.updateBoard()
            return True
        elif dualSides:
            self.board[posRowFour][posColumnFour] = self.aiSymbol
            self.updateBoard()
            return True
        elif sideCheck:
            self.board[posRowThree][posColumnThree] = self.aiSymbol
            self.updateBoard()
            return True

    def checkCorners(self):
        for i in self.corners:
            if self.board[i[0]][i[1]] == self.playerSymbol:
                pass
            else:
                return True, i[0], i[1]

        return False, -1, -1

    def checkDualCorners(self):
        for i in self.corners:
            lower = self.corners.index(i) - 1
            higher = self.corners.index(i) + 1
            if self.board[i[0]][i[1]] == self.aiSymbol and self.board[(self.corners[lower])[0]][(self.corners[lower])[1]] == ' ':
                return True, (i - 1)[0], (i - 1)[1]
            if self.board[i[0]][i[1]] == self.aiSymbol and self.board[(self.corners[higher])[0]][(self.corners[higher])[1]] == ' ':
                return True, (self.corners[lower])[0], (self.corners[higher])[1]
        return False, -1, -1
            

    def checkSides(self):
        for i in self.sides:
            if self.board[i[0]][i[1]] == self.playerSymbol:
                pass
            else:
                return True, i[0], i[1]

        return False, -1, -1

    def checkDualSides(self):
        for i in self.sides:
            if self.board[i[0]][i[1]] == self.aiSymbol and self.board[(i - 1)[0]][(i - 1)[1]] == ' ':
                return True, (i - 1)[0], (i - 1)[1]
            if self.board[i[0]][i[1]] == self.aiSymbol and self.board[(i + 1)[0]][(i + 1)[1]] == ' ':
                return True, (i + 1)[0], (i + 1)[1]
        return False, -1, -1

    def checkForTwo(self):
        pass

    def checkPlayerWin(self):
        pass

    def updateBoard(self):
        rowOne = generateGroup(self.board, 0)
        rowTwo = generateGroup(self.board, 1)
        rowThree = generateGroup(self.board, 2)

        print('\n' + rowOne + '\n' + rowTwo + '\n' + rowThree)

            
board = Chess()




































