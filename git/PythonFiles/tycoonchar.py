
def propertySelect(properties):
    choice = input("\nPlease enter the number of the property you would like to purchase, or type 'cancel', to leave!: ")
    if str(choice.lower()) == 'cancel':
        return False, 0
    try:
        choice = int(choice) - 1
    except ValueError:
        return 'error', 0
    try:
        # Takes selected info. 
        tp1 = properties[choice]
    except IndexError:
        return 'error', 0
    tp2 = tp1[0]
    # Returns total price.
    return tp2, tp1

def dsSelect(dealerships):
    choice = input('\nPlease enter the number of the dealership you would like to purchase, or type \'cancel\', to leave!: ')
    if str(choice.lower()) == 'cancel':
        return False
    choice = int(choice) - 1
    try:
        # Takes selected info. 
        tp1 = dealerships[choice]
    except IndexError:
        return 'error'
    tp2 = tp1[1]
    # Returns total price.
    return tp2, tp1
    

class Character():
    
    def __init__(self, gender, firstName, lastName, brand, starting_product, age):
        product_types = []
        self.gender = gender

        self.firstName = firstName
        self.lastName = lastName

        self.brand_name = str(brand)
        
        self.starting_product = str(starting_product)
        product_types.append(self.starting_product)
        
        self.age = age
        self.money = 100000

        self.possibleVehicles = []
        self.dealerships = []
        self.properties = []

### ADD VEHICLES

    def buyProperty(self):
        from random import randint
        from price_calcs_tycoon import priceCalcProp
        
        propertiesForSale = []
        propertyCount = randint(1, 3)
        print('\n...Contacting Agent...')
        print('\n----------------------')
        number = 1
        for i in range(propertyCount):
            tp, sf, ppsf, type_ = priceCalcProp()
            # Adds total price first
            propertiesForSale.append((tp, sf, ppsf, type_, number))
            number += 1
        for i in propertiesForSale:
            print('\n' + str(i[4]) + '. Type: ' + str(i[3]))
            print('\nTotal Price: $' + str(i[0]))
            print('\nSquare Footage: ' + str(i[1]))
            print('\nPrice Per Square Foot: $' + str(i[2]))
            print('\n ------------------------------')
        buying = True
        purchasing = True
        while buying:
            buy_ = input('\nWould you like to purchase one of these properties?: ')
            if str(buy_.lower()) == 'no':
                print('\n...Exiting...')
                break
            elif str(buy_.lower()) == 'yes' or str(buy_.lower()) ==' yeah' or str(buy_.lower()) == 'yea':
                
                while purchasing:
                    
                    ret_tp, propertyDetails = propertySelect(propertiesForSale)

                    if ret_tp == 'error':
                        print('\nThere is no property with that number!')
                        continue
            
                    elif not ret_tp:
                        print('\n...Exiting...')
                        break
                        
                    elif ret_tp <= self.money:
                        self.money -= int(ret_tp)
                        print('\nPurchase was successful!\n')
                        print('Remaining cash: ' + str(self.money))
                        self.properties.append(propertyDetails)
                        break
                                            
                    else:
                        print('You do not have enough money to purchase that property!')
                        continue
       
            buying = False

    def displayProperties(self):
        print('\n----------------------')
        print('Dealerships: ' )
        for detail in self.dealerships:
            print('   Max # of Employees: ' + str(detail[0]))
            print('   Value: $' + str(detail[1]))
            print('   Class: ' + str(detail[2]))
            print('   People in area: ' + str(detail[3]) + '\n')
        print('Properties: ')
        for detail in self.properties:
            print('   Value : $' + str(detail[0]))
            print('   Square footage: ' + str(detail[1]) + ' square feet')
            print('   Value per square footage: $' + str(detail[2]))
            print('   Type: ' + str(detail[3]) + '\n')
        

    def buyDealership(self):
        from random import randint
        from price_calcs_tycoon import priceCalcDS
        
        count = randint(1, 3)
        dsForSale = []
        number = 0
        print('\n...Contacting Agent...')
        print('\n----------------------')
        
        for i in range(count):
            maxEmployees, price, class_, people = priceCalcDS()
            dsForSale.append((maxEmployees, price, class_, people))

        for i in dsForSale:
            number += 1
            print('\n' + str(number) + '.' + ' Total Price: $' + str(i[1]))
            print('\nMax Number of Employees: ' + str(i[0]))
            print('\nPopulation of Surrounding Area: ' + str(i[3]))
            print('\nClass: ' + str(i[2]))
            print('\n ------------------------------')
            
        buying = True
        purchasing = True
        while buying:
            buy_ = input('\nWould you like to purchase one of these dealerships?: ')
            if str(buy_.lower()) == 'no':
                print('\n...Exiting...')
                break
            elif str(buy_.lower()) == 'yes' or str(buy_.lower()) ==' yeah' or str(buy_.lower()) == 'yea':
                
                while purchasing:
                    try:
                        ret_tp, dealershipDetails = dsSelect(dsForSale)
                    except TypeError:
                        ret_tp = False                        
                    if ret_tp == 'error':
                        print('\nThere is no property with that number!')
                        continue
   
                    elif not ret_tp:
                        print('\n...Exiting...')
                        break
                    
                    elif ret_tp <= self.money:
                        self.money -= int(ret_tp)
                        self.dealerships.append(dealershipDetails)
                        print('\nPurchase was successful!\n')
                        print('Remaining cash: ' + str(self.money))
                        break
                 
                    else:
                        print('You do not have enough money to purchase that property!')
                        continue

            else:
                print('Please enter \'Yes\' or \'No')
                continue
                
            
            buying = False

smith = Character(0,0,0,0,0,0)
smith.buyDealership()
smith.displayProperties()
            

