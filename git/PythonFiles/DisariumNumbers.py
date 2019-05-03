from math import pow
while True:
    num = input('What number would you like to test?: ')
    numl = len(num)
    numst = 0
    numen = 1
    finalnumber = 0

    while numen <= numl:
        numen = float(numen)
        num = str(num)
        numst = int(numst)
        numx = num[numst]
        numx = float(numx)
        fnum = pow(numx, numen)
        numst += 1
        numen += 1
        num = str(num)
        numst = str(numst)
        numen = int(numen)
        finalnumber = finalnumber + fnum

    finalnumber = int(finalnumber)
    finalnumber = str(finalnumber)
    num = str(num)

    if num == finalnumber:
        print(num + ' is a Disarium number!')
    else:
        print(num + ' is NOT a Disarium number!')
    
    continue
