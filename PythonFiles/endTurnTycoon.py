from tycoonchar import Character

class EndTurn(Character):
    
    def getSales(self):
        from random import randint

        import collections
        
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
            large = int(i[3] * 0.45)
            specificBuyers = randint(small, large)
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
            for person in range(peopleAtDealer):
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
