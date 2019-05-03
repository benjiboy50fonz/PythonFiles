class CommsRoom_Phase4():

    @classmethod
    def CommsRoom(self, pistol_object, ar_object, player):
        from Miscellaneous.weaponclasses import Weapons
        from Miscellaneous.mobclasses import CreateGollum
        from SeparateCommands.fightcommand import Fight

        self.look_around_phrases = ['look around',
                                    'view',
                                    'look around the room',
                                    'look',
                                    'what\'s here',
                                    'where am i']
        self.call_out_phrases = ['shout to the figure',
                                 'shout to him',
                                 'shout to her ',
                                 'shout to it',
                                 'shout to them',
                                 'call to the figure',
                                 'call to him',
                                 'call to her',
                                 'call to it',
                                 'call to them',
                                 'holler to the figure',
                                 'holler to him',
                                 'holler to her',
                                 'holler to it',
                                 'holler to them',
                                 'yell to the figure',
                                 'yell to him',
                                 'yell to her',
                                 'yell to it',
                                 'yell to them']

        self.sneak_up_phrases = ['approach it',
                                 'approach him',
                                 'approach them',
                                 'approach her',
                                 'go towards it',
                                 'go towards him',
                                 'go towards them',
                                 'go towards her',
                                 'walk towards it',
                                 'walk towards him',
                                 'walk towards them',
                                 'walk towards her',
                                 'creep towards it',
                                 'creep towards him',
                                 'creep towards them',
                                 'creep towards her',
                                 'sneak towards it',
                                 'sneak towards him',
                                 'sneak towards them',
                                 'sneak towards her',
                                 'go at it',
                                 'go at him',
                                 'go at her',
                                 'go at them']

        self.what_is_it_phrases = ['what is the figure',
                                   'what is it',
                                   'who is it',
                                   'who is the figure',
                                   'who is that']

        self.attack_phrases = ['attack it',
                               'attack',
                               'attack him',
                               'attack her',
                               'attack them',
                               'fight it',
                               'fight him',
                               'fight her',
                               'fight them']

        self.attack_shoot_phrases = ['shoot him',
                                     'shoot her',
                                     'shoot it'
                                     'shoot them',
                                     'shoot',
                                     'fire at him',
                                     'fire at it',
                                     'fire at her',
                                     'fire at them',
                                     'fire']

        self.attack_melee_phrases = ['hit him',
                                     'hit her',
                                     'hit it',
                                     'hit them',
                                     'punch him',
                                     'punch her',
                                     'punch it',
                                     'punch them',
                                     'slug him',
                                     'slug her',
                                     'slug it',
                                     'slug them',
                                     'kick him',
                                     'kick him',
                                     'kick her',
                                     'kick it',
                                     'kick them']

        self.run_away_phrases = ['run away',
                                 'flee',
                                 'get away',
                                 'leave the area']

        self.melee_phrases = ['hit',
                              'melee',
                              'punch',
                              'attack with hatchet'
                                ]

        self.go_left_phrases = ['go left',
                                'turn left',
                                'go to the left',
                                'go to left',
                                'head left',
                                'head to the left',
                                'head to left',
                                'turn towards the left',
                                ]
        
        self.go_right_phrases = ['go right',
                                 'turn right',
                                 'go to the right',
                                 'go to right',
                                 'head right',
                                 'head to the right',
                                 'head to right',
                                 'turn towards the right',
                                 ]

        self.go_forward_phrases = ['head forward',
                                   'go straight',
                                   'walk straight',
                                   'run straight',
                                   'head straight',
                                   'go forward',
                                   'head forward']
        # Enter the room (Below)

        while True:
            comms_room_first_option_input = raw_input('\n: ')
            if str(comms_room_first_option_input.lower()) in self.look_around_phrases:
                print('You see a small ramp on your left, leading up to a long viewing platform. It overlooks a comm room, sloping downward, left to right.'
                  '\nStraight ahead, there is a row of computers in the comms room. On your right, there is a slope heading down, with more computer rows along the left side.'
                  '\nYou look up to the viewing platform and see a figure standing there.')
                continue

            elif str(comms_room_first_option_input.lower()) in self.call_out_phrases:
                print('The figure turns to face you. But it is not a soldier. It is not even a human. '
                      '\nIt slowly walks out from the tinted glass window, and reaches the top of the ramp on your left.'
                      '\nThe figure stares down at you, and you realize it is an alien of the Zortec military group! It is a  They have been destorying the '
                      '\nKatarsis military! Stunned and frightened, you forget all of your training. ')
                self.player_attacks_first = False
                break

            elif str(comms_room_first_option_input.lower()) in self.sneak_up_phrases:
                print('You approach the figure, creeping up behind it silently. You realize it is not a soldier or a human.'
                      '\nIt is a Gollum, an alien which serves in the Zortec military group. The Katarsis military has been fighting the Zortecs '
                      '\never since you were put into hyper sleep. It is most certainly your enemy.')
                self.player_attacks_first = True
                break

            elif str(comms_room_first_option_input.lower()) in self.go_left_phrases:
                print('You head up the ramp on your left, paying close attention to the creature. You eventually realize that it is not'
                      '\na human. It is a gollum; an alien breed that allies itself with the Zortec military. The Zortecs are'
                      '\nyour greatest enemy!')
                self.player_attacks_first = True
                break

            elif str(comms_room_first_option_input.lower()) in self.go_right_phrases:
                print('You head down the ramp, ignoring the figure. Suddenly, you hear a screech and realize that the figure was the one who made'
                      '\nthat sound. You whirl around and see a Gollum, an member of the Zortec military group staring down at you!')
                self.player_attacks_first = False
                break

            elif str(comms_room_first_option_input.lower()) in self.go_forward_phrases:
                print('You walk through the row of computers ahead of you. You suddenly, you hear a screech and realize that the figure was the one who made'
                      '\nthat sound. You whirl around and see a Gollum, an member of the Zortec military group staring down at you!')
                self.player_attacks_first = False
                break

            elif str(comms_room_first_option_input.lower()) in self.what_is_it_phrases:
                print('We can not tell you that!')
                continue

            else:
                print('\nYou can not do that at this moment!\n')
                continue

        while True:
            comms_room_second_input = raw_input('\nWhat now?: ')

            if str(comms_room_second_input.lower()) in self.attack_phrases:
                fight = Fight()

                enemy_list, attack_used, attack_used_object = fight.fightStart(0, 1, 0, 0, 0, 0, self.player_attacks_first, pistol_object, ar_object, player)

                fight.fightEnd(player, enemy_list, attack_used, attack_used_object)

            elif str(comms_room_second_input.lower()) in self.run_away_phrases:
                print('Frightened you turn back and run to the door! The door is shut however, and the creature is heading towards you!')
                self.player_attacks_first = False
                fight = Fight()

                enemy_list, attack_used, attack_used_object = fight.fightStart(0, 1, 0, 0, 0, 0, self.player_attacks_first, pistol_object, ar_object, player)

                fight.fightEnd(player, enemy_list, attack_used, attack_used_object)

            else:
                continue