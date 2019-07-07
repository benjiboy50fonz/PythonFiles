def generateGroup(list_, symbol):
        # TODO Figure this out 
        return '''                  _________________________
                  |       |       |       |
                  |       |       |       |
                  |   ''' + str(symbol) + '''   |       |       |
                  |       |       |       |
                  |_______|_______|_______|'''
class Chess():

    import numpy as np
    
    def __init__(self):

        # X is 1, O is 2
        
        print(generateGroup())
        print(generateGroup())
        print(generateGroup())

        self.startGame()

    def startGame(self):
        print('Welcome to the unbeatable game!')

        incorrect = True
        while incorrect: 
            choice = input('\nType \'1\' for X\'s or \'2\' for O\'s: ')
            if str(choice) == '1':
                print('\nYou chose X\'s!')
                self.playerSymbol = 1
                self.aiSymbol = 2
                incorrect = False

            elif str(choice) == '2':
                print('\nYou chose Y\'s!')
                self.playerSymbol = 2
                self.aiSymbol = 1
                incorrect = False

            else:
                print('\nPlease enter \'1\' or \'2\'!')
                continue

        self.generateField()
        self.playerMove()

    def generateField(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', ''],
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
            
            if self.board[int(row) - 1][int(column) - 1] != '':
                print('\nThat Space is Taken! Please choose another!')
                continue

            wrong = False

        self.modifyBoard(int(row) - 1, int(column) - 1)

    def modifyBoard(self, row, column):
        print(generateGroup('X', 1))

            
board = Chess()





































