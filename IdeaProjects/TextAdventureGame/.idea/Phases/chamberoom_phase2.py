class ChamberRoom_Phase2():
    @classmethod
    def BreakGlass(self, hatchetstat, error_count, health):
        self.possible_FAIL_break_phrases = ['break the glass',
                                            'break glass',
                                            'smash the glass',
                                            'smash glass',
                                            'hit the glass',
                                            'hit glass',
                                            'shatter the glass',
                                            'shatter glass',
                                            'destroy the glass',
                                            'destroy glass']

        self.possible_break_phrases = ['break the glass with the hatchet',
                                       'break glass with the hatchet',
                                       'break glass with hatchet',
                                       'smash the glass with the hatchet',
                                       'smash glass with the hatchet',
                                       'smash glass with hatchet',
                                       'destroy the glass with the hatchet',
                                       'destroy glass with the hatchet',
                                       'destroy glass with hatchet',
                                       'shatter the glass with the hatchet',
                                       'shatter glass with the hatchet',
                                       'shatter glass with hatchet',
                                       'hit the glass with the hatchet',
                                       'hit glass with the hatchet',
                                       'hit glass with hatchet',
                                       'use the hatchet to break the glass']
        if hatchetstat == 1:
            pass
        else:
            print('------------------\nError. Restart Game\n------------------')
            exit()
        break_glass = True
        while not break_glass != True:
            break_glass_input = raw_input('\nWhat next?: ')
            if str(break_glass_input.lower()) in self.possible_FAIL_break_phrases:
                print('You punch the glass with all your might but nothing happens. You hand is not strong enough!')
                error_count += 1
                health -= 15

                if error_count > 3:
                    print('\n--------------------------\n\nSadly, you did not escape quickly enough, and suffocated in your chamber.\n ')
                    print('-------------------------- \n\nPlease play again!')
                    exit()
                else:
                    continue

            elif str(break_glass_input.lower()) in self.possible_break_phrases:
                print('The glass shatters when your hatchet makes contact with it. You slowly step out into the cool, dead air. '
                      '\nYou look down to see that you had a thermal suit, on providing zero protection. '
                      '\nYou are in the chamber room. Straight ahead, there is an exit. Everything in the room was savaged.')
            else:
                print('''\nThat didn't work!\n''')
                error_count += 1
                if error_count > 3:
                    print('\n--------------------------\n\nSadly, you did not escape quickly enough, and suffocated in your chamber.\n ')
                    print('-------------------------- \n\nPlease play again!')
                    exit()
                else:
                    continue

            break_glass = False



    @classmethod
    def ExitCapsuleRoom(self):
        self.possible_exit_phrases = ['go forward',
                                      'go straight',
                                      'leave room',
                                      'leave the room',
                                      'go ahead']
        self.possible_FAIL_exit_phrases = ['look around',
                                           'view',
                                           'what now?',
                                           'what now']

        while True:
            chamber_room_direction_input = raw_input('\nWhat next?: ')
            if str(chamber_room_direction_input.lower()) in self.possible_FAIL_exit_phrases:
                print('\nThere is nothing left to do here.')
                continue
            elif str(chamber_room_direction_input.lower()) in self.possible_exit_phrases:
                print('You have left the capsule room. ')
                return '0'
            else:
                print('\nYou can not do that!\n')
                continue
        ### 0 means you left, 1 means returned







