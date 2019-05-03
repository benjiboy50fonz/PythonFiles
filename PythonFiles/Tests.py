while True:

    print('')

    print('You walk out past the other capsules. You reach a room, where there is an intersection. You can walk straight up the stairs, or go left or right.')

    capsule_hall = input('Which way would you like to go?:')

    if capsule_hall.lower() == 'go left' or capsule_hall.lower() == 'left':

        ammo_room = input('The hallway which goes left comes to a quick end at a door')

        if ammo_room.lower() == 'go back':

            gun = 1
            continue
        elif ammo_room.lower() == 'enter the room':

            print('In the room you find a handgun, with 20 magazines. This may come in handy.')

            gun = 2

            mag = 20

            print('You step back out into the hallway.')

            continue                                                                                                                                                                        
    elif capsule_hall.lower() == 'go right' or capsule_hall.lower() == 'right':

        desk = input('There is a small desk with a lamp, a maintenance chart, and a broom.')

        if desk.lower() == 'take the broom':

            print('Broom taken.')

            broom = 2

        elif desk.lower() == 'go back':

            broom = 1

            continue

    elif capsule_hall.lower() == 'go forward' or capsule_hall.lower() == 'go straight':
        break
print('You walk up the stairs, ready for amything. There is a computer terminal where you can access files, and the capsule releases and awakenings. Probably best not to release the others.')
print(' ')
print(gun)

while True:
    computer_terminal = input('What would you like to do? You can access the terminal or go down from the landing, left or right. They both take you to two double doors: ')
    if computer_terminal.lower() == 'access the terminal':

        print('On the terminal, three options are displayed:')

        print(' - Open recent revivals')

        print(' - Revive soldier')

        print(' - Get starship information')

        terminal_access = input('What would you like to do?:')

        if terminal_access.lower() == 'exit the terminal' or terminal_access.lower() == 'exit terminal':

            continue

        elif terminal_access.lower() == 'open recent revivals':

            print('Charlie Smith / Date: 1/18/2876 / Age Left: 28 / Sex: Male / Deployment reason: War call / Return: False /')

            print('Rodric Cald / Date: 5/23/3012 / Age Left: 30 / Sex: Male / Deployment reason: Unkown / Return: False/')

            print('Sebastian McCloud / Date: 10/17/3062 / Age Left: 34 / Sex: Male / Deployment reason: Unkown / Return: Unknown/')

            print('You will now exit the terminal')

            continue

        elif terminal_access.lower() == 'revive soldier':

            print(' ')

            print('PLEASE ENTER PIN: ____')

            terminal_code = input('What code would you like to guess? You do not know any codes:')

            if terminal_code == '4469':

                print('CORRECT')

                awaken = input('Who would you like to awake? Tristen Cower is the only fit soldier.')

                if awaken.lower() == 'tristen cower':

                    print('UNABLE')

                    print('UNKNOWN REASON')

                    print('You will now exit the terminal')

                    continue

                elif awaken.lower() == 'exit':

                    continue

                else:

                    continue

                    

            else:

                print('INCORRECT')

                print('You will now exit the terminal.')

                continue

        elif terminal_access.lower() == 'get starship information':

            print('STARSHIP 4759489: DEPARTURE DATE 2897 / DEPARTURE LOCATION: RAULLEN / NEAREST GALAXY: DURAN / NEAREST CONTROLLED GALAXY: SEDEFF.DISTANCE.584038ly / CURRENT LOCATION: UNKOWN / CURRENT COURSE: UNKOWN[SET COURSE OR ERROR] / ARRIVAL TIME/ ERROR /')

            print('You will now exit the terminal')

            dest = 1

        elif terminal_access.lower() != 'get starship information':

            dest = 1

    elif computer_terminal.lower() == 'go left' or computer_terminal.lower() == 'go right':

        print('You carry on down through the platform. The doors seemed jammed. You take your hatchet and put it in the door, and creep through. You look left and notice a door at the end. Towards the right, the hall runs down about 30 feet. At the end there is a small storage closet. The door is open with the light off. You look a little closer and notcie that there is something moving around in there. "Hey!" You shout, hoping that it is anthor soldier, and hopefully the one who let you out. It glances over at you, its red eyes illuminating the closet. You realize it is about 8 feet tall, and muscular, with an oddly shaped head. It is not a human.')

        alien1_health = 2
        break
while True:
    if ammo_room.lower() == 'go back':
            gun = 1
            continue
    elif ammo_room.lower() == 'enter the room':
        pass
        print('clear')
