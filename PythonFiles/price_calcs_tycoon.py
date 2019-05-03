def priceCalcProp():
        from random import randint, choice
        
        chances = randint(1, 4)
        if chances == 4:
            square_footage = randint(20000, 300000)
        else:
            square_footage = randint(20000, 100000)
        
        if square_footage > 250000:
            ppsf = randint(28, 56)

        elif square_footage <= 250000 and square_footage > 250000:
            ppsf = randint(21, 34)

        elif square_footage <= 250000 and square_footage > 200000:
            ppsf = randint(19, 33)

        elif square_footage <= 200000 and square_footage > 100000:
            ppsf = randint(17, 28)

        elif square_footage <= 100000 and square_footage > 50000:
            ppsf = randint(16, 26)

        elif square_footage <= 50000 and square_footage > 35000:
            ppsf = randint(15, 19)

        elif square_footage <= 35000:
            ppsf = randint(10, 16)

        else:
            print('error line 53, priceCalcProp')

        total_price = square_footage * ppsf

        typesOfProperties = ['Warehouse', 'Storeroom', 'Factory', 'Basic Commercial', 'Warehouse', 'Factory', 'Newly Constructed']
        type_ = choice(typesOfProperties)
        
        return total_price, square_footage, ppsf, type_

def priceCalcDS():
        from random import randint, choice

        scale = randint(1, 3)
        if scale == 1:
                maxEmployees = randint(8, 16)
                price = randint(100000, 200000)
                class_ = 'C'
                
        elif scale == 2:
                maxEmployees = randint(16, 27)
                price = randint(200000, 300000)
                class_ = 'B'
        else:
                maxEmployees = randint(27, 40)
                price = randint(300000, 450000)
                class_ = 'A'

        people = randint(1, 345)

        return maxEmployees, price, class_, people

