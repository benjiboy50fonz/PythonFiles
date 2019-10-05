from fractions import Fraction

import math


def getInput():

    # ax^2 + bx + c

    values = []
    order = ['a', 'b', 'c']

    for val in range(3):
        incorrect = True
        while incorrect:
            num = input(order[val] + ': ')
            try:
                # Checks to see if the input is an integer.
                num = float(num)
                
            except ValueError:
                # Checks to see if fraction. Does more fancy
                # stuff to check to see if it really is a fraction. 
                if '/' in str(num).strip():
                    newNum = str(num.replace('/', ''))
                    try:
                        numWithSpace = str(num.replace('/', ' '))
                        separateNums = numWithSpace.split()
                        if not len(separateNums) == 2:
                            print('What was that?')
                            continue
                        finalDec = float(separateNums[0]) / float(separateNums[1])
                        num = finalDec
                    except ValueError:
                        print('What was that?')
                        continue
                else:
                    print('What was that?')
                    continue
            incorrect = False
            values.append(num)

    return values

def factorFunc(number):
    factors = []
    number = int(number)
    for i in range(1, abs(number)+1):
        if number % i == 0:
            factors.append(i)

    return factors

def completeCalculations(values):
    # Three Groups: The -b +/-, the radical, and the denominator. Starts with the radical.

    a = values[0]
    b = values[1]
    c = values[2]

    integer = True
    needI = False

    try:
        radical = math.sqrt((b * b) - (4 * a * c))
    except ValueError:
        radical = math.sqrt(abs((b * b) - (4 * a * c)))
        needI = True

    cont = False
    print(radical)
    if '.' in str(radical):
        radicalTwo = str(radical).replace('.', ' ')
        if not radical / int(radicalTwo[0])== 1:
            cont= True
    # The indexed one is the permanent 'integer'. This should allow us to accuratley test for decimals. 
    print(str(radical) + str(cont))
    if cont:
        # Takes positive radical.

        radical = (b * b) - (4 * a * c)
        # reverts the radical back to what it was under the sign.
        
        radicalFactors = factorFunc(radical)

        finalOut = '1'
        finalIn = radical
        print(finalIn)
        print(radicalFactors)
        # Removes sketchy and messed up values.
        radicalFactors.remove(1)
        radicalFactors.remove(int(abs(radical)))
        
        for factor in radicalFactors:
            bringFactorOut = False
            bringPartnerOut = False
            
            partner = radical / factor
            factor = int(factor)

            # Uses above decimal test method to check for whole nums. 

            factorRoot = math.sqrt(abs(factor))
            partnerRoot = math.sqrt(abs(partner))

            pseudoFRoot = int(math.sqrt(abs(factor)))
            pseudoPRoot = int(math.sqrt(abs(partner)))
            
            if pseudoFRoot / factorRoot == 1:
                bringFactorOut = True
            if pseudoPRoot / partnerRoot == 1:
                bringPartnerOut = True

            # Checks to see if they both can be brought out of the radical, then checks individually. 

            print(bringPartnerOut)
            print(bringFactorOut)

            if bringFactorOut and bringPartnerOut:
                finalOut = factorRoot * partnerRoot
                finalIn = '1'

            if bringFactorOut:
                finalOut = factorRoot
                finalIn = partnerRoot
            
            if bringPartnerOut:
                finalOut = partnerRoot
                finalIn = factorRoot

        print('final ' + str(finalIn))
        print('final ' + str(finalOut))
                
            
        integer = False
        if needI:
            radString = str(finalOut) + 'sqrt(' + str(round(finalIn, 4)) + ')i'
        else:
            radString = str(finalOut) + '*sqrt(' + str(round(finalIn, 4)) + ')'
    else:
        print('here')
        if needI:
            radString = ' ' + str(round(radical, 4)) + 'i'
        else:
            radString = ' ' + str(round(radical, 4))

    # TODO: Test the above radical code more and finish writing down below. 
            
    finalRad = radString.strip()

    print(radString)

    # Done with radical part. Begins -b +/-.

    finalB = b * -1

    # Done with -b lol. Begin denominator.

    finalDen = 2 * a

    # Done with denominator lol. Add it all together and check for simplification.
    
    one, two = returnFinal(integer, needI, finalRad, finalB, finalDen)
    print('one ' + one)
    print('two ' + two)

    
def returnFinal(integer, needI, finalRad, finalB, finalDen):
    if not needI:
        if integer:
            firstPass = False
            secondPass = False
            # checks to see if top divisible by the bottom.
            testOne = int(int(finalB) / int(finalDen))
            if not '.' in str(testOne):
                firstPass = True
            print(finalRad)
            print(finalDen)
            testTwo = float(finalRad) / int(finalDen)
            if not '.' in str(testTwo):
                secondPass = True

            # If they are divisible, divide and combine the two numbers.
            # Otherwise, do nothing to either and return the final. 

            if firstPass and secondPass:
                partOne = finalB / finalDen
                partTwo = finalRad / finalDen

                finalOne = (partOne + partTwo)
                finalTwo = (partOne - partTwo)
                
            else:
                # In theory the final rad part should never be negative . . .
                finalTopOne = float(finalB) + float(finalRad)
                finalTopTwo = float(finalB) - float(finalRad)

                finalValOne = finalTopOne / finalDen
                finalValTwo = finalTopTwo / finalDen

                # Final vals should be working. TESTED.

                finalValOne = Fraction(float(finalValOne))
                finalValTwo = Fraction(float(finalValTwo))
                print(finalValOne)
                
                finalOne = str(finalValOne)
                finalTwo = str(finalValTwo)

        else:
            finalOne = str(finalB) + ' + ' + str(abs(finalRad)) + ' / ' + str(finalDen)
            finalTwo = str(finalB) + ' - ' + str(abs(finalRad)) + ' / ' + str(finalDen)

    else:
        if integer:
            firstPass = False
            secondPass = False

            testOne = int(int(finalB) / int(finalDen))
            if not '.' in str(testOne):
                firstPass = True

            neutralRad = float(finalRad.replace('i', ''))

            
            testTwo = float(neutralRad) / int(finalDen)

            print(testTwo)
            
            if not '.' in str(testTwo):
                secondPass = True
# TODO: TRACE 2,4,9 RESPECTIVLEY, ITS NOT SIMPLIFYING. 
            print(testOne)
            if not firstPass:
                testOne = testOne.as_integer_ratio()
                testOne = list(testOne)

            if not secondPass:
                testTwo = testTwo.as_integer_ratio()
                testTwo = list(testTwo)

            neutralRad = int(neutralRad)

            print(str(firstPass) + str(secondPass))
            if firstPass and secondPass:
                partOne = finalB / finalDen
                partTwo = neutralRad / finalDen

                finalOne = str(partOne) + ' + ' + str(abs(partTwo)) + 'i'
                finalTwo = str(partOne) + ' - ' + str(abs(partTwo)) + 'i'
            elif firstPass:
                partOne = finalB / finalDen
                
                finalOne = str(partOne) + ' + ' + str(testTwo[0]) + 'i / ' + str(testTwo[1]) 
                finalTwo = str(partOne) + ' - ' + str(testTwo[0]) + 'i / ' + str(testTwo[1])

            elif secondPass:
                partTwo = finalB / finalDen
                
                finalOne = str(testOne[0]) + ' + ' + str(partTwo) + 'i / ' + str(testOne[1]) 
                finalTwo = str(testOne[0]) + ' - ' + str(partTwo) + 'i / ' + str(testOne[1])

            else:
                finalOne = str(testOne[0]) + ' + ' + str(testTwo[0]) + 'i / ' + str(testOne[1]) 
                finalTwo = str(testOne[0]) + ' - ' + str(testTwo[0]) + 'i / ' + str(testOne[1])
        else:
            finalOne = str(finalB) + ' + ' + str(finalRad) + ' / ' + str(finalDen)
            finalTwo = str(finalB) + ' - ' + str(finalRad) + ' / ' + str(finalDen)
            
    return finalOne, finalTwo
    


values = getInput()
completeCalculations(values)

