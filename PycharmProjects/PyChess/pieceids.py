class Id:
    def __init__(self):
        self.king = 0
        self.queen = 1
        self.knight = 2
        self.bishop = 3
        self.rook = 4
        self.pawn = 5

        self.relation = {
            'king': 0,
            'queen': 1,
            'knight': 2,
            'bishop': 3,
            'rook': 4,
            'pawn': 5
        }

        self.reverseRelation = {
            0 : 'king',
            1 : 'queen',
            2 : 'knight',
            3 : 'bishop',
            4 : 'rook',
            5 : 'pawn'
        }

        # Dummy class to store values.
