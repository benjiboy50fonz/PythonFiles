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

        self.numberSold = {}

        self.employeeWage = 75
        self.employeeAnger = 0

        self.totalVehicles = {'coupe':1000,
                              'SUV':200} 

        self.companySize = 0 # The score
        
        self.tierOneVehicles = [['sedan', 55, 1, 100],
                                ['SUV', 80, 1, 100],
                                ['minivan', 70, 1, 100],
                                ['crossover', 75, 1, 100],
                                ['coupe',65, 1, 100],
                                ['van', 75, 1, 100],
                                ['pickup truck', 80, 1, 100],
                                ['simple motorcycle', 80, 1, 100],
                                ['electric scooter', 50, 1, 100],
                                ['segway personal transporter', 60, 1, 100],
                                ['canoe', 55, 1, 100],
                                ['kayak', 55, 1, 100],
                                ['hang glider', 60, 1, 100],
                                ['minibus', 75, 1, 100]
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
    def resetSold(self):
        self.numberSold = {}
        # Should never need
        
    def checkLevelUps(self):
        for vehicle in self.tierOnevehicles:
            if vehicle in self.numbersold.keys():
                vehicleReqLevel = vehicle[2] * vehicle[2]
                if self.numberSold[vehicle] > vehicleReqLevel:
                    levelUp = True
                else:
                    levelUp = False

            if levelUp and vehicle[1] > 20:
                self.tierOneVehicles[vehicle][1] -= 5
                self.tierOneVehicles[vehicle][2] += 1
                
            
    def changeEmployeeWage(self, val=75):
        self.employeeWage = val
        if val > self.employeeWage:
            self.employeeAnger = 1
        self.employeeAnger = (75 - self.employeeWage) * 1.3
        # Put this out of 100


    def changeVehicleCost(self, repeat=False):
        if repeat:
            pass
        else:
            print('\n--- Logging Onto Server --- \n')
        if len(self.totalVehicles) == 0:
            print('You have no vehicles!')
            print('\n--- Logging Off server ---\n')
            return
        else:
            count = 1
            print('\nVehicles in Stock: \n')        
            for i in list(self.totalVehicles.keys()):
                for x in self.tierOneVehicles:
                    if x[0] == i:
                        price = x[3]
            
                print(str(count) + '. ' + i + '  :  $' + str(price) + '\n')
                count += 1
                if len(list(self.totalVehicles.keys())) == 0:
                    print('You have no vehicles in stock!')
                    print('\n--- Logging Off Server ---\n')
                    return

            notInt = True
            while notInt:
                try:
                    choice = int(input('Please enter the number next to the desired vehicle, or type \'cancel\' to exit: '))
                except(ValueError):
                    if str(choice.lower()) == 'cancel':
                        print('\n--- Logging Off Server ---\n')
                        return
                    print('\nPlease enter a number!\n')
                    continue
                try:
                    
                    vehicleNames = list(self.totalVehicles.keys())
                    print(str(vehicleNames))
                    vehicleName = vehicleNames[choice - 1]
                except(IndexError):
                    print('\nPlease enter a number within the range!\n')
                    continue
                notInt = True
                while notInt:
                    index = 0
                    newPrice = input('What would you like to change the price of the ' + str(vehicleName) + ' to?: ')    
                    for set_ in self.tierOneVehicles:
                        if vehicleName in set_[0]:
                            original = set_[3]
                            
                            try:
                                newPrice = int(newPrice)
                            except(ValueError):
                                print('\nPlease enter a number!\n')
                                continue

                            self.tierOneVehicles[index][3] = int(newPrice)
                            
                            notInt = False
                            print('\nThe price for the ' + str(set_[0]) + ' was successfully changed to $' + str(set_[3]) + \
                                  ' from $' + str(original) + '!\n')
                            unclear = True
                            while unclear:
                                again = input('Change another value?: ')
                                if str(again.lower()) == 'yes':
                                    self.changeVehicleCost(True)
                                elif str(again.lower()) == 'no':
                                    print('\n--- Logging Off Server --- \n')
                                    break
                                    return
                                else:
                                    print('\nPlease enter \'yes\' or \'no\'!\n')
                                    continue
                        else:
                            index += 1
                            continue

                
                
    def calcLosses(self):
        from random import randint

        # Runs employee payments
        totalEmployees = 0
        for i in self.dealerships:
            totalEmployees += i[0]

        totalEmployeeExpenses = self.employeeWage * totalEmployees

        totalEmployeeLosses = 0
        
        # Calculates people who quit. 
        for i in self.dealerships:
            chance = randint(self.employeeAnger, 100)
            if chance == 99:
                i[0] -= 1
                totalEmployeeLosses += 1
                # Employee quits

        # Calculates robbery.
        robbed = False
        losses = 0
        robbedChek = False
        robbedLocations = []
        for i in self.dealerships:
            if i[2] == 'C':
                robbery = 10
            elif i[2] == 'B':
                robbery = 6
            else:
                robbery = 2

            chance = randint(robbery, 100)
            if chance == 99:
                robbed = True
                robbedChek = True
                robbedLocations.append(str(i[5]))
                losses += i[3] * 0.5
            else:
                if robbedChek:
                    pass
                else:
                    robbed = False

        # Does the same for the properties
        robbedP = False
        lossesP = 0
        robbedLocationsP = []
        robbedCheck = False
        for i in self.properties:
            robbery = i[1]
            chance = randint(robbery, robbery * i[1])
            if chance == robbery + 1:
                robbedP = True
                robbedCheck = True
                robbedPLocationsP.append(str(i[5]))
                lossesP += i[1] * 0.05
            else:
                if robbedCheck:
                    pass
                else:
                    robbedP = False

        # Combines the two.
        if robbedP or robbed:
            finalRob = True
            totalRobberyLosses = lossesP + losses
            robbedFinalLocations = list(robbedLocations + robbedLocationsP)
        else:
            totalRobberyLosses = 0
            robbedFinalLocations = []
            finalRob = False
            

        # Calculates taxes.
        dealershipTotalTax = 0
        for i in self.dealerships:
            dealershipTotalTax += int(i[4])

        propertyTotalTax = 0
        for i in self.properties:
            propertyTotalTax += int(i[4])

        totalTax = propertyTotalTax + dealershipTotalTax

        #Sums it all up
        totalLosses = totalEmployeeExpenses + totalRobberyLosses + totalTax
        robberyStats = [totalRobberyLosses, robbedFinalLocations]

        self.money -= totalLosses
        return totalLosses, totalTax, totalEmployeeExpenses, robberyStats, totalEmployeeLosses

    def calcSaleLosses(self):
        from random import randint

        import math

        #TODO Add necessary limits on car pricing (< 0 = !) and work out mathematics


        #Have starting prices for each tier 1:100 2:500 3:1500 4:2500+
        for i[0] in self.tierOneVehicles:
            if i[0] in self.totalVehicles:
                yourVehicleType = i[0]
                yourVehicleLevel = i[2]
                yourVehicleCost = i[3]

                range_ = int(yourVehicleCost * 0.25)
                if yourVehicleCost > 100:
                    difference = yourVehicleCost - 100
                    multiplier = math.sqrt(difference * 0.25)
                elif yourVehicleCost == 100:
                    multiplier = 0
                else:
                    difference = 100 - yourVehicleCost
                    multiplier = -1 * math.sqrt(difference * 0.25)
                    
                    
                qualityComparison = randint(0, 3)
                if qualityComparison == 0:
                    # Higher compared to you
                    opposingQuality = randint(1, 3) + yourVehicleLevel
                elif qualityComparison == 1:
                    # Lower compared to you
                    var = randint(1, 3)
                    if yourVehicleLevel <= var:
                        opposingQuality = 1
                    else:
                        opposingQuality = yourVehicleLevel - var
                else:
                    opposingQuality = yourVehicleLevel

                if opposingQuality != yourVehicleLevel:
                    _multiplier = math.sqrt(opposingQuality - yourVehicleLevel)

                else:
                    _multiplier = 0

                final = _multiplier + multiplier

                # Add multipliers together for final
        
    def getSales(self, saleLosses):
        from random import randint

        import collections
        import math
        
        totalSurroundingBuyers = 0
        locationPurchases = {}

        totalEarnings = 0

        totalVehicles = 0
        lossesPerDS = []
        for i in self.totalVehicles.values():
            totalVehicles += i
        print('og sl ' + str(saleLosses))
        print('og ds len ' + str(len(self.dealerships)))
        

        # Funky and jank distribution of sale losses for each ds. #WORKEDFIRSTTIME
        #TODO: Confirm this is actually working or just not crashing.
        if len(self.dealerships) == 0:
            print('WARNING YOU OWN NO DEALERSHIPS. THEREFORE, YOU CANNOT EARN MONEY VIA SALES.')
            return
            
        elif saleLosses >= len(self.dealerships):
            print(str(math.floor(saleLosses / len(self.dealerships))))
            print(str(saleLosses / len(self.dealerships)))
            if math.floor(saleLosses / len(self.dealerships)) == saleLosses / len(self.dealerships):
                for i in range(len(self.dealerships)):
                    lossesPerDS.append(int(saleLosses / len(self.dealerships)))
            else:
                whole = math.floor(saleLosses / len(self.dealerships))
                var = len(self.dealerships) * whole
                remainder = saleLosses - var
                for ds in self.dealerships:
                    lossesPerDS.append(whole)
                    
                # Evenly distributes the remaining sale losses 6/25/2019
                index = 0
                for loss in range(remainder):
                    try:
                        lossesPerDS[index] = lossesPerDS[index] + 1
                        index += 1
                    except (IndexError):
                        index = 0
                        continue
                        
                        
                print('remainder ' + str(remainder))
        else:
            index = 0
            empty = False
            if len(lossesPerDS) == 0:
                empty = True
            for loss in range(saleLosses):
                try:
                    lossesPerDS[index] = lossesPerDS[index] + 1
                    index += 1
                except (IndexError):
                    if empty:
                        lossesPerDS.append(1)
                        index += 1

            # fills in zeros for the dealerships with no losses.
            while len(lossesPerDS) != len(self.dealerships):
                lossesPerDS.append(0)
                
            print('hmm')

        print('lossesPerDS ' + str(lossesPerDS))
            
        for i, x in zip(self.dealerships, lossesPerDS):
            small = int(i[3] * 0.15) # Takes a minimum number of people based off of the total number of surrounding people. 
            large = int(i[3] * 0.45)
            specificBuyers = randint(small, large)
            if specificBuyers - x >= 0:
                specificBuyers -= x
            elif specificBuyers < x:
                specificBuyers = 0
            
            locationPurchases[i[5]] = specificBuyers
            totalSurroundingBuyers += specificBuyers

        ogLocationPurchases = locationPurchases
        locationPurchases = collections.OrderedDict(locationPurchases)
        self.totalVehicles = collections.OrderedDict(self.totalVehicles)
        locationEarnings = {}

        count = 0
        # This only runs once because there is only one dealership, which creates an issue in the zip for loop.
        for dealership in locationPurchases.keys():
            peopleAtDealer = locationPurchases[dealership]
            for person in range(int(peopleAtDealer)):
                # gets the dealership name and the total people buying from that location.
                possibleBuys = len(self.totalVehicles.keys()) - 1
                
                totalVehicles = 0
                for i in self.totalVehicles.values():
                    totalVehicles += i
                    
                    # add fixer here
                if totalVehicles > 0:
                    buyType = randint(0, possibleBuys)
                    vehicleNames = list(self.totalVehicles.keys())
                    typeName = vehicleNames[buyType]           
                    numberOfType = self.totalVehicles[typeName]
                    if numberOfType > 0:
                        vehiclesLeft = False
                    else:
                        continue
                    for i in self.tierOneVehicles:
                        if i[0] == typeName:
                            priceForSelected = i[3]
                    # add other tiers here.
                    # Adds credits to earnings
                    totalEarnings += priceForSelected
                    
                    # Removes car from availability
                    self.totalVehicles[typeName] -= 1

                    # Adds car to sold dictionary
                    if str(typeName) in self.numberSold.keys():
                        self.numberSold[typeName] += 1
                    else:
                        self.numberSold[typeName] = 1

                    #Removes the person from buyers list
                    totalSurroundingBuyers -= 1
                    if totalSurroundingBuyers <= 0:
                        done = True

                    locationPurchases[dealership] -= 1

                    # Adds earnings to specific dealer.
                    if dealership in locationEarnings:
                        locationEarnings[dealership] += priceForSelected
                    else:
                        locationEarnings[dealership] = priceForSelected

                    count += 1

                else:
                    ranOutOfVehicles = True

        try:
            if ranOutOfVehicles:
                pass
        except(UnboundLocalError):
            ranOutOfVehicles = False
            
        return totalEarnings, ogLocationPurchases, locationEarnings, self.totalVehicles, ranOutOfVehicles
        
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
                        print('Remaining cash: $' + str(self.money))
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
smith.changeVehicleCost()
print(str(smith.getSales(1)))

#totalEarnings, ogLocationPurchases, locationEarnings, self.totalVehicles, ranOutOfVehicles

