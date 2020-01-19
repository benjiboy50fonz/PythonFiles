class Calculator:
    def __init__(self):

        self.myWeight = self.getMyWeight()
        self.partnerWeight = self.getPartnerWeightInput()

        self.maxLengthFromCent = 55.625  # 4' 7 5/8"
        self.rungLength = 3  # 3"

        who, distance, otherDistance = self.calculate()

        if who == 0:
            print('\nMake sure you are ' + str(
                round((distance / 12), 3)) + ' ft away from the center! \nMake sure your partner is ' + str(
                round((otherDistance / 12), 3)) + ' ft away from the center!')

        elif who == 1:
            print('\nMake sure your partner is ' + str(
                round((distance / 12), 3)) + ' ft away from the center! \nMake sure you are ' + str(
                round((otherDistance / 12), 3)) + ' ft away from the center!')

    def getMyWeight(self):
        incorrect = True
        while incorrect:
            try:
                weight = float(input('Weight of you? (lb\'s): '))
            except TypeError:
                print('I need a number!')
                continue
            if weight > 155:
                print('TOO HEAVY')
                continue
            else:
                incorrect = False

        return weight

    def getPartnerWeightInput(self):
        incorrect = True  # type: bool
        while incorrect:
            try:
                weight = float(input('Weight of the partner? (lb\'s): '))
            except TypeError:
                print('I need a number!')
                continue
            if weight > 155:
                print('TOO HEAVY')
                continue
            else:
                incorrect = False

        return weight

    def calculate(self):
        # 0 = you, 1 = them

        positionOfWho = int(input('Who has the set position? (0 or anything for you, 1 for partner): '))

        if positionOfWho == 1:
            waiting = True
            while waiting:
                try:
                    self.partnerFeet = int(input('Feet, not including inches, from center?: '))
                    self.partnerInches = int(input('Inches, not including feet, from center?: '))

                    self.partnerDistance = ((12 * self.partnerFeet) + self.partnerInches)

                    if self.partnerDistance >= self.maxLengthFromCent:
                        print('Too far over!')
                        continue

                    break

                except(TypeError, NameError):
                    print('I need a number!')
                    continue

            return 0, ((self.partnerDistance * self.partnerWeight) / self.myWeight), self.partnerDistance  # 0, returning your distance

        else:
            waiting = True
            while waiting:
                try:
                    self.yourFeet = int(input('Feet, not including inches, from center?: '))
                    self.yourInches = int(input('Inches, not including feet, from center?: '))

                    self.yourDistance = ((12 * self.yourFeet) + self.yourInches)

                    if self.yourDistance >= self.maxLengthFromCent:
                        print('Too far over!')
                        continue

                    break

                except(TypeError, NameError):
                    print('I need a number!')
                    continue

            return 1, ((self.yourDistance * self.myWeight) / self.partnerWeight), self.yourDistance  # 1, returning partner's distance


running = True
while running:
    run = Calculator()

    try:
        again = str(input('\nWould you like to do this again? (y/n): ')).lower()

        if again == 'y':
            del run
            continue
        elif again == 'n':
            break
        else:
            print('I\'ll take that as a no!')
            break

        break

    except NameError:
        continue

exit()
