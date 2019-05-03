while True:
    prob = input('''Please enter '1', if you're finding an average speed, '2' for a length of time, and '3' for a distance (NOTE: Miles, MPH, and hours and seconds are used.): ''')
    if prob == '1':


        ##Copy below for func.

        
        dist1 = input('What is the distance?:')
        dist1 = int(dist1)
        time11 = input('''How many hours did it take?(NOTE: Please enter data like this: 3)''')
        time12 = input('''How many minutes did it take?(NOTE: Please enter data like this: 3)''')
        time13 = input('''How many seconds did it take?(NOTE: Please enter data like this: 3)''')
        time11 = int(time11)
        time12 = int(time12)
        time13 = int(time13)
        time12 = time12 / 60
        time13 = time13 / 3600
        ftime1 = time12 + time13 + time11
        print(str(ftime1))
        avrgspd = dist1 / int(ftime1)
        print(str(avrgspd))
    
