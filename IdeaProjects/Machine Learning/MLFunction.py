import random
import collections
import time


def wearOrNot(response):
    if str(response) == 'optional':
        while True:
            choice = raw_input('Caught in the middle . . . would you like to wear a jacket?(\'yes\' or \'no\'!): ')
            if choice == 'yes':
                return 'j'
            elif choice == 'no':
                return 'nj'
            else:
                print('Please enter \'yes\' or \'no\'!')
                continue
    elif response:
        print('--- JACKET ---')
        return True
    else:
        print('--- NO-JACKET ---')
        return True


class TemperatureMeasure:
    def __init__(self):
        self.data = {}
        self.count = 1

        while True:
            options = raw_input('Press \'1\' to expand the database, press \'2\' to be amazed!(Or \'exit\' to exit): ')

            if int(options) == 1:
                if self.applyRandom():
                    continue
            elif int(options) == 2:
                if len(self.data) < 3:
                    print('You need to enter values first!')
                    self.applyRandom()
                if self.getRunner:
                    continue
            elif str(options.lower()) == 'exit':
                print('\nBye!\n')
                time.sleep(2.0)
                exit()

    def applyRandom(self):
        global final, randTemp
        currentlyExisting = True
        for i in range(3):
            while currentlyExisting:
                randTemp = random.randint(0, 101)
                if randTemp in self.data.keys():
                    continue
                break
            decision = raw_input(str(self.count) + '. The temperatureerature is ' + str(randTemp)
                                 + ' degrees fahrenheit. Should you wear a jacket?(\'yes\' or \'no\'): ')
            if str(decision) == 'yes':
                final = 'j'
            elif str(decision) == 'no':
                final = 'nj'
            else:
                print('error')
            self.data[randTemp] = final

            self.data = collections.OrderedDict(sorted(self.data.items()))
            self.count += 1

        self.count = 1
        return True

    def giveResponse(self, temperature):
        self.data[temperature] = 'unknown'
        self.data = collections.OrderedDict(sorted(self.data.items()))
        if 'unknown' in self.data.values():
            unknownPos = self.data.values().index('unknown')
            print(str(self.data))

            prevPos = self.data.keys().index(self.data.keys()[unknownPos - 1])
            postPos = self.data.keys().index(self.data.keys()[unknownPos + 1])

            postDiff = abs(self.data.keys()[postPos] - temperature)
            prevDiff = abs(self.data.keys()[prevPos] - temperature)

            print('post ' + str(postDiff))
            print('pre ' + str(prevDiff))

            if postDiff > prevDiff:
                result = self.data.values()[prevPos]
                self.data[temperature] = self.data.values()[prevPos]
                if result == 'j':
                    return True
                else:
                    return False

            elif postDiff == prevDiff:
                result = 'optional'
                return result

            else:
                result = self.data.values()[postPos]
                self.data[temperature] = self.data.values()[postPos]
                if result == 'j':
                    return True
                else:
                    return False

    @property
    def getRunner(self):
        userIsIdiot = True
        while userIsIdiot:
            try:
                temperature = int(input('What temperatureerature would you like to give?: '))  # type: int
                temperature += 0
            except TypeError:
                print('Enter an integer!')
                continue
            break
        output = self.giveResponse(int(temperature))
        decision = wearOrNot(output)
        if decision == 'j' or decision == 'nj':
            self.data = {k: v for k, v in self.data.items() if v}
            self.data[int(temperature)] = decision
            self.data = collections.OrderedDict(sorted(self.data.items()))
            print(str(self.data))
        return True


if __name__ == '__main__':
    begin = TemperatureMeasure()  # type: TemperatureMeasure
