"""
This file is for the intersection outside the chamber room. Very complex, if it works do not touch it!
STATUS: UNDER CONSTRUCTION
"""
from Miscellaneous.weaponclasses import Weapons

class LargeHallway_Phase3():
    @classmethod
    def __init__(self):
        pistol = Weapons()

    @classmethod
    def OpenHallway(self):
        self.possible_left_phrases = ['go left',
                                      'turn left',
                                      'head left',
                                      'circle left',
                                      'walk left',
                                      'run left',
                                      'creep left']

        self.possible_right_phrases = ['go right',
                                   'turn right',
                                   'head right',
                                   'circle right',
                                   'walk right',
                                   'run right',
                                   'creep right']

        self.possible_straight_phrases = ['go forward',
                                      'go straight',
                                      'head forward',
                                      'head straight',
                                      'walk forward',
                                      'walk straight',
                                      'run forward',
                                      'run straight',
                                      'creep forward',
                                      'creep straight']

        self.possible_backwards_phrases = ['go back',
                                           'return',
                                           'head back',
                                           'head backwards',
                                           'go backwards',
                                           'go to the chamber room',
                                           'go to chamber room']

        self.possible_forward_phrases = ['go straight',
                                         'go forward',
                                         'go ahead',
                                         'walk forward',
                                         'walk straight',
                                         'head forward',
                                         'go to the large sliding door',
                                         'run forward']

        print('\nYou arrive in a large hallway. The hallway is dark, with just one flickering light. There are sleek black walls with tinted sliding glass doors.'
          '''\nOn your left, there is a hallway, and and at the end there is a sliding door that has the word 'STORAGE' above it. On your right, there is a small desk with a handgun on top of it.
          \nStraight ahead, there is a large sliding door.''')
        while True:
            large_hallway_input = raw_input('What would you like to do?: ')
            if str(large_hallway_input.lower()) in self.possible_right_phrases:
                return '0'

            elif str(large_hallway_input.lower()) in self.possible_left_phrases:
                return '1'

            elif str(large_hallway_input.lower()) in self.possible_backwards_phrases:
                return '2'

            elif str(large_hallway_input.lower()) in self.possible_forward_phrases:
                return '3'

            else:
                print('Error')
                return '8'

# , handgunstat, mag_count, mag_size, mag_starting_amount)

    @classmethod
    def MaintenanceDesk(self, object):
        print('\nYou head right and find a fully loaded handgun sitting on a desk, next to two full handgun magazines. '
              'There is nothing else here except for this maintenance desk.')
        self.possible_take_handgun_phrases = ['grab handgun', 'grab the handgun',
                                              'take handgun', 'take the handgun',
                                              'hold handgun', 'hold the handgun',
                                              'pick up handgun', 'pick up the handgun']
        maintenance_desk_input = raw_input('What would you like to do now?: ')
        if str(maintenance_desk_input.lower()) in self.possible_take_handgun_phrases and object.pistol_stat == 0:
            print('\nYou lift up the handgun, examining it slowly. It is an old SIG Sauer M17 handgun. You grab the other two magazines next')
            object.equipPistol()
        elif object.pistol_stat == 1:
            print('You already have the pistol!')
            pass
        else:
            print('Error: largehallway.py line 40ish!')

        print('''That's all that is over here. You walk back towards the hallway. ''')
        return 'hallway'

    @classmethod
    def StorageCloset(self, object, armor, ammo_storage_stat, armor_storage_stat, score):
        from SeparateCommands.scorecommand import ScoreCommands
        print('\nYou walk down the hall and reach the sliding door. You walk up to the door, but instead of the door opening as it should,'
              '\nit creaks. The door seems to be stuck.')

        self.possible_return_phrases = ['go back',
                                        'go back into the large hallway',
                                        'go into the large hallway',
                                        'go into the hallway',
                                        'return',
                                        'go to hallway',
                                        'go to large hallway',
                                        'head back',
                                        'go backwards',
                                        'return to hallway',
                                        'return to the hallway',
                                        'head back',
                                        'head backwards',
                                        'head behind']

        self.possible_pry_door_phrases = ['use the hatchet to pry the door open',
                                          'pry the door open with hatchet',
                                          'pry the door open with the hatchet',
                                          'pry door open with hatchet',
                                          'open the door with hatchet',
                                          'open door with the hatchet',
                                          'open the door with the hatchet',
                                          'open door with hatchet',
                                          'use hatchet to pry door']

        self.possible_FAIL_pry_door_phrases = ['open the door',
                                               'pry the door open',
                                               'pry door open',
                                               'open door',
                                               'open the door with hands',
                                               'pry the door open with hands']

        while True:
            storage_door_input = raw_input('\nWhat now?: ')
#           Tests to see if the player wants to go back. Look at ACG!
            if str(storage_door_input.lower()) in self.possible_return_phrases:
                print('\nYou walk back to the hallway.\n')
                armor_r = armor
                break

            elif str(storage_door_input.lower()) in self.possible_pry_door_phrases:
                self.possible_take_two_handgun_mags = ['take the mags',
                                                        'take ammo',
                                                        'take the ammo',
                                                        'take the mags',
                                                        'take the two handgun mags',
                                                        'take the two hangun magazines',
                                                        'grab the two handgun magazines',
                                                        'grab the mags',
                                                        'grab the magazines',
                                                        'grab the handgun magazines']
                self.possible_take_armor = ['take the armor',
                                            'take armor',
                                            'take the helmet',
                                            'grab armor',
                                            'tahke helmet']

                self.possible_return_in_phrases = ['go back',
                                                   'go back into the large hallway',
                                                   'go into the large hallway',
                                                   'go into the hallway',
                                                   'return',
                                                   'go to hallway',
                                                   'go to large hallway',
                                                   'head back',
                                                   'go backwards',
                                                   'return to hallway',
                                                   'return to the hallway',
                                                   'head back',
                                                   'head backwards',
                                                   'head behind']

                print('You insert the blade of your hatchet into the crack and pull with all your might. '
                  '\nSlowly, the door opens up. Suddenly, the door jerks open, knocking you over. '
                  '\nYou get up and dust yourself off, and proceed into the room.')
                print('\nOn the ground, there is a old combat helmet, and two handgun magazines on a rusty metal shelf.')
                inside = True
                while inside == True:
                    inside_storage_closet_input = raw_input('What would you like to do?: ')
                    armor_r = 0

                    if str(inside_storage_closet_input.lower()) in self.possible_take_two_handgun_mags and ammo_storage_stat == 0:
                        object.increasePistolMags(2)
                        #Ammo was taken!
                        score = ScoreCommands.IncreaseScoreSmall(score)
                        ammo_storage_stat = 1
                        continue
                    elif str(inside_storage_closet_input.lower()) in self.possible_take_armor and armor_storage_stat == 0:
                        print('Armor Taken!')
                        armor_r = armor + 15
                        score = ScoreCommands.IncreaseScoreSmall(score)
                        armor_storage_stat = 1
                        print('Total Armor = ' + str(armor_r) + ' hps')
                        continue
                    elif str(inside_storage_closet_input.lower()) in self.possible_return_in_phrases:
                        print('You walk out of the closet, and the door slams shut behind you.')
                        armor_r = armor
                        inside = False
                    else:
                        print('You can\'t do that!')
                        continue

                continue
                        #return_to_hall = '0'
                        #return return_to_hall

            else:
                print('You can\'t do that!')
                continue
        return ['0', armor_r, armor_storage_stat, ammo_storage_stat, score]

    @classmethod
    def LargeDoor(self, console_broken_stat):
        self.possible_pull_door_open_phrases = ['pull door',
                                                'pull the door open',
                                                'pull the doors open',
                                                'pull the door apart',
                                                'pull the doors apart',
                                                'pull door open',
                                                'use the hatchet to open the door',
                                                'pry the door open with the hatchet']

        self.possible_manual_door_phrases = ['use the manual open',
                                             'use the manual',
                                             'open manually',
                                             'open it manually',
                                             'open the door manually',
                                             'use the manual door open',
                                             'pull the manual',
                                             'pull the manual lever',
                                             'pull the manual switch',
                                             'pull the manual release',
                                             'pull the manual open']

        self.possible_go_back_phrases = ['go back',
                                         'go back into the large hallway',
                                         'go into the large hallway',
                                         'go into the hallway',
                                         'return',
                                         'go to hallway',
                                         'go to large hallway',
                                         'head back',
                                         'go backwards',
                                         'return to hallway',
                                         'return to the hallway',
                                         'head back',
                                         'head backwards',
                                         'head behind']

        print('\nYou walk up to the door and wait for it to slide open. After about three seconds of waiting, you realize the sensor is broken.'
              '\nThe door has a small manual open.')
        while True:
            large_door_input = raw_input('\n: ')
            if str(large_door_input.lower()) in self.possible_manual_door_phrases:
                print('You walk over to the console, and pull the lever on it. '
                    '\nSuddenly, sparks hop off the console, and smoke rises above it.'
                    '\nThe console is rendered useless. You must find another way.')
                console_broken_stat_r = 1
                continue

            elif str(large_door_input.lower()) in self.possible_pull_door_open_phrases:
                print('You grab the edges of the sliding steel doors, and pull with all your strength, slowly the doors open just enough so you can fit through.'
                      '\nYou squeeze through, right as the door slams behind you. No going back now!')
                return '1'

            elif str(large_door_input.lower()) in self.possible_go_back_phrases:
                print('\nYou turn and wak back to the hallway.\n')
                return '0'

            else:
                print('You can\'t do that!')
                continue






