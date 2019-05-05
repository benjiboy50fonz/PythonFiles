def priceCalcProp():
        from random import randint, choice
        
        chances = randint(1, 4)
        if chances == 4:
            square_footage = randint(20000, 300000)
        else:
            square_footage = randint(20000, 100000)
        
        if square_footage > 250000:
            ppsf = randint(28, 56)
            tax = randint(150, 250)
            
        elif square_footage <= 250000 and square_footage > 250000:
            ppsf = randint(21, 34)
            tax = randint(250, 375)

        elif square_footage <= 250000 and square_footage > 200000:
            ppsf = randint(19, 33)
            tax = randint(375, 450)
        elif square_footage <= 200000 and square_footage > 100000:
            ppsf = randint(17, 28)
            tax = randint(450, 600)

        elif square_footage <= 100000 and square_footage > 50000:
            ppsf = randint(16, 26)
            tax = randint(600, 800)

        elif square_footage <= 50000 and square_footage > 35000:
            ppsf = randint(15, 19)
            tax = randint(800, 1000)

        elif square_footage <= 35000:
            ppsf = randint(10, 16)
            tax = randint(1000, 1200)

        else:
            print('error line 53, priceCalcProp')

        total_price = square_footage * ppsf

        typesOfProperties = ['Warehouse', 'Storeroom', 'Factory', 'Basic Commercial', 'Warehouse', 'Factory', 'Newly Constructed']
        type_ = choice(typesOfProperties)
        
        return total_price, square_footage, ppsf, type_, tax

def priceCalcDS():
        from random import randint, choice

        scale = randint(1, 3)
        if scale == 1:
                maxEmployees = randint(8, 16)
                price = randint(100000, 200000)
                class_ = 'C'
                tax = randint(250, 375)
                
        elif scale == 2:
                maxEmployees = randint(16, 27)
                price = randint(200000, 300000)
                class_ = 'B'
                tax = randint(575, 700)
        else:
                maxEmployees = randint(27, 40)
                price = randint(300000, 450000)
                class_ = 'A'
                tax = randint(800, 1100)
                
        people = randint(1, 345)

        return maxEmployees, price, class_, people, tax

