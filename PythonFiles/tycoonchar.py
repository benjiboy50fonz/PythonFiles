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
        import collections
        
        product_types = []
        self.gender = gender

        self.totalVehicles = {'coupe':10}

        self.companySize = 0 # The score
        
        self.tierOneVehicles = [('sedan', 55, 1, 100),
                                ('SUV', 80, 1, 100),
                                ('minivan', 70, 1, 100),
                                ('crossover', 75, 1, 100),
                                ('coupe',65, 1, 100),
                                ('van', 75, 1, 100),
                                ('pickup truck', 80, 1, 100),
                                ('simple motorcycle', 80, 1, 100),
                                ('electric scooter', 50, 1, 100),
                                ('segway personal transporter', 60, 1, 100),
                                ('canoe', 55, 1, 100),
                                ('kayak', 55, 1, 100),
                                ('hang glider', 60, 1, 100),
                                ('minibus', 75, 1, 100)
                                ]                                

        self.firstName = firstName
        self.lastName = lastName

        self.brand_name = str(brand)
        
        self.starting_product = str(starting_product)
        product_types.append(self.starting_product)
        
        self.age = age
        self.money = 1000000

        self.possibleVehicles = []
        self.dealerships = []
        self.properties = []

### ADD VEHICLES

    def endTurn(self):
        from random import randint

        import collections
        
        print('ds ' + str(self.dealerships))
        print('p ' + str(self.properties))

        totalSurroundingBuyers = 0
        locationPurchases = {}


        # REMOVE
        self.dealerships = [(33, 356838, 'A', 252, 1045, 'Ben\'s Cars')]

        totalEarnings = 0

        totalVehicles = 0
        for i in self.totalVehicles.values():
            totalVehicles += i
        
        for i in self.dealerships:
            small = int(i[3] * 0.15) # Takes a minimum number of people based off of the total number of surrounding people. 
            large = int(i[3] * 0.85)
            specificBuyers = randint(small, large)
            locationPurchases[i[5]] = specificBuyers
            totalSurroundingBuyers += specificBuyers

        locationPurchases = collections.OrderedDict(locationPurchases)
        self.totalVehicles = collections.OrderedDict(self.totalVehicles)
        locationEarnings = {}

        count = 0
        # This only runs once because there is only one dealership, which creates an issue in the zip for loop.
        for person, dealership in zip(locationPurchases.values(), locationPurchases.keys()):
            print('LEN1 =' + str(locationPurchases.values()) + ' uh =' +str(len(locationPurchases.keys())))
            # gets the dealership name and the total people buying from that location.
            possibleBuys = len(self.totalVehicles.keys()) - 1
            print('PB ' + str(len(self.totalVehicles.keys())))
            
            totalVehicles = 0
            for i in self.totalVehicles.values():
                totalVehicles += i
            
            if possibleBuys == 0:
                print('uh oh')
                # add fixer here
            if totalVehicles > 0:
                buyType = randint(0, possibleBuys)
                vehicleNames = list(self.totalVehicles.keys())
                typeName = vehicleNames[buyType]           
                numberOfType = self.totalVehicles[typeName]
                print('NOT ' + str(numberOfType))
                if numberOfType > 0:
                    vehiclesLeft = False
                else:
                    continue
                print('len3 ' +str(len(locationPurchases.keys())))
                for i in self.tierOneVehicles:
                    if i[0] == typeName:
                        priceForSelected = i[3]
                # add other tiers here.
                # Adds credits to earnings
                totalEarnings += priceForSelected
                print('here')
                
                # Removes car from availability
                self.totalVehicles[typeName] -= 1

                #Removes the person from buyers list
                totalSurroundingBuyers -= 1
                if totalSurroundingBuyers <= 0:
                    done = True

                locationPurchases[dealership] -= 1
                print('len3 ' +str(len(locationPurchases.keys())))

                # Adds earnings to specific dealer.
                if dealership in locationEarnings:
                    locationEarnings[dealership] += priceForSelected
                else:
                    locationEarnings[dealership] = priceForSelected

                print(str(count) + '. locationEarnings: ' + str(locationEarnings) + ', locationPurchases: ' + str(locationPurchases) + \
                      ' totalEarnings: ' + str(totalEarnings) + ' totalVehicles: ' + str(self.totalVehicles))

                count += 1
                print('len3 ' +str(len(locationPurchases.keys())))
                print('LEN1 =' + str(len(locationPurchases.values())))
            if totalVehicles <= 0:
                print('Dunzzies')

    def increaseScore(self, val=100):
        self.companySize += val

    def produceVehicle(self, exit_=True):
        if not exit_:
            return
        print('\n--- Entering Online Production Server ---\n')
        if self.companySize >= 3000:
            self.availableTiers = 3

        elif self.companySize >= 1000:
            self.availableTiers = 2
        
        else:
            self.availableTiers = 1
        
        # Above chooses which vehicle libraries to display
        count = 1
        if self.availableTiers == 1:
            for i in self.tierOneVehicles:
                words = i[0].split()
                for word in words:
                    totalWords = str(word[0].upper() + word[1:] + ' ')
                totalWords = totalWords.strip()
                print(str(count) + '. ' + str(totalWords) + ' Cost: ' + str(i[1]) + ' credits\n')
                count += 1
        playerIsAnIdiot = True
        while playerIsAnIdiot:
            selectedVehicle = input('Please enter the number of the vehicle you would like to produce, or type \'cancel\' to leave: ' )
            try:
                selectedVehicle = int(selectedVehicle)
            except(ValueError):
                if str(selectedVehicle.lower()) == 'cancel':
                    print('--- Exiting ---')
                    return
                print('Please enter a number!\n')
                continue
            selectedVehicle -= 1
            try:
                proceed = input('You selected the ' + str(self.tierOneVehicles[selectedVehicle][0]) + '. Proceed?: ')
            except(IndexError):
                print('\nPlease enter a listed values.\n')
                continue
            
            if str(proceed.lower()) == 'yes':
                pass
            else:
                print('\nReturning.\n')
                continue

            # Continues to the exact number.
            vehicleName = self.tierOneVehicles[selectedVehicle][0]
            vehicleCost = self.tierOneVehicles[selectedVehicle][1]
            playerIsAnIdiot = False
            tooMany = True
            
            while tooMany:
                number = input('How many ' + vehicleName + 's would you like to produce?: ')
                try:
                    number = int(number)
                except(ValueError):
                    print('Please enter a number!')
                    continue

                if number * vehicleCost > self.money:
                    print('\nYou do not have enough money to produce ' + str(number) + ' ' + vehicleName + 's!\n')
                    continue

                else:
                    remainingMoney = str(self.money - (number * vehicleCost))
                    confirmation = input('Are you sure you want to produce ' + str(number) + ' ' + vehicleName + 's? The total cost is $' + \
                                         str(number * vehicleCost) + ' and you will have $' + remainingMoney + ' remaining: ')
                    if str(confirmation.lower()) == 'yes':
                        if vehicleName in self.totalVehicles.keys():
                            self.totalVehicles[vehicleName] += number
                        else:
                            self.totalVehicles[vehicleName] = number

                        print('\nYour purchase was successful! You gained an additional ' + str(number) + ' ' + vehicleName + 's!\n')

                        unclear = True                        
                        while unclear:
                            again = input('\nWould you like to exit or produce more?: ')
                            if str(again.lower()) == 'exit':
                                print('--- Exiting ---')
                                return
                            elif str(again.lower().strip()) == 'produce more' or str(again.lower().strip()) == 'again':
                                self.produceVehicle()
                            else:
                                print('Please enter\'again\' or \'exit\'!')
                                                    
                    elif str(confirmation.lower()) == 'cancel':
                        print('--- Exiting ---')
                        return
                    else:
                        continue
                
                                               
                                    
                    

    def buyProperty(self):
        from random import randint
        from price_calcs_tycoon import priceCalcProp
        
        propertiesForSale = []
        propertyCount = randint(1, 3)
        print('\n...Contacting Agent...')
        print('\n----------------------\nMoney: ' + str(self.money))
        number = 1
        for i in range(propertyCount):
            tp, sf, ppsf, type_, tax = priceCalcProp()
            # Adds total price first
            propertiesForSale.append((tp, sf, ppsf, type_, number))
            number += 1
        for i in propertiesForSale:
            print('\n' + str(i[4]) + '. Type: ' + str(i[3]))
            print('\nTotal Price: $' + str(i[0]))
            print('\nSquare Footage: ' + str(i[1]))
            print('\nPrice Per Square Foot: $' + str(i[2]))
            print('\nTax: $' + str(i[4]) + ' per turn')          
            print('\n ------------------------------')
        buying = True
        purchasing = True
        while buying:
            buy_ = input('\nWould you like to purchase one of these properties?: ')
            if str(buy_.lower()) == 'no':
                print('\n...Exiting...')
                return
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
                        self.increaseScore()
                        

                        name = str(input('What would you like to name your property?: '))
                        name.strip()
                        wordsInName = name.split()
                        finalString = '' 
                        for word in wordsInName:
                            finalString = finalString + word[0].upper() + word[1:].lower() + ' '
                        propertyDetails = propertyDetails + (str(finalString.strip()),)
                        
                        self.properties.append(propertyDetails)
                        break
                                            
                    else:
                        print('You do not have enough money to purchase that property!')
                        continue
       
            buying = False

    def displayLand(self):
        print('\n----------------------')
        print('Dealerships: ' )
        if len(self.dealerships) == 0:
            print('   No Dealerships.')
        else:
            for detail in self.dealerships:
                print('  ' + str(detail[4]) + ': ')
                print('   Max # of Employees: ' + str(detail[0]))
                print('   Value: $' + str(detail[1]))
                print('   Class: ' + str(detail[2]))
                print('   People in area: ' + str(detail[3]) + '\n')
        print('Properties: ')
        if len(self.properties) == 0:
            print('   No Properties.')
        else:
            for detail in self.properties:
                print('  ' + str(detail[4]) + ': ')
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
        print('\n----------------------\nMoney: ' + str(self.money))
        
        for i in range(count):
            maxEmployees, price, class_, people, tax = priceCalcDS()
            dsForSale.append((maxEmployees, price, class_, people, tax))

        for i in dsForSale:
            number += 1
            print('\n' + str(number) + '.' + ' Total Price: $' + str(i[1]))
            print('\nMax Number of Employees: ' + str(i[0]))
            print('\nPopulation of Surrounding Area: ' + str(i[3]))
            print('\nClass: ' + str(i[2]))
            print('\nTax: $' + str(i[4]) + ' per turn')
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
                        return
                    
                    elif ret_tp <= self.money:
                        self.money -= int(ret_tp)
                        print('\nPurchase was successful!\n')
                        # Adds names to the dealerships.
                        self.increaseScore()
                        name = str(input('What would you like to name your dealership?: '))
                        name.strip()
                        wordsInName = name.split()
                        finalString = '' 
                        for word in wordsInName:
                            finalString = finalString + word[0].upper() + word[1:].lower() + ' '
                        dealershipDetails = dealershipDetails + (str(finalString.strip()),)
                        
                        self.dealerships.append(dealershipDetails)
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
smith.endTurn()
            

