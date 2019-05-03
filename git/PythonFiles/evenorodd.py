def evenorodd():
    while True:
        number = int(input('What number would you like to test?:'))
        answer = number % 2
        if answer == 0:
            print(str(number) + ' is even.')
        elif answer != 0:
            print(str(number) + ' is odd.')
        again = input('Would you like to enter another number?:')
        if again.lower == 'yes' or again.lower == 'yea':
            continue
        elif again.lower == 'no':
            break
            exit()


        
