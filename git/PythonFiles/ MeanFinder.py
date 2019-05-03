import random 
print('Mean Calculator:')
totalnum = input('''What are your numbers? Please space them like this: e.g. 1 2 3 / Type 'none' if done:''')
while totalnum != 'none':
    num = totalnum
    num.split(' ')
    print(num)
    print(len(num))
if totalnum.lower() == 'none':
    print('ok')
    print(numlist)


