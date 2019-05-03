def temperature():
    temp = input('What is the temperature outside?:')
    degr = input('Is that Fahrenheit or Celsius?:')
    while True:
        if degr.lower() == 'celsius':
            fahr = int(temp) * 1.8 + 32
            print('The temperature outside is ' + str(fahr) + ' Fahrenheit.')
            break
        elif degr.lower() == 'fahrenheit':
            cels = int(temp)%1.8 - 32
            print('The temperature outside is ' + str(cels) + ' Celsius.')
            break
        else:
            continue
temperature()

   
