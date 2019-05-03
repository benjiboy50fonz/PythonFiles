class IntroText_Phase1():
    @classmethod
    def Intro_text(self, hatchetstat):
        error_count = 0
        print('\nYou awaken in a small capsule. You are a member of the Katarsis Military group, which serves under the nation of Andeya. You were put into hyper sleep about 2539 years ago. You have no idea who reactivated you.')
        print('You look through the glass and see that all the other capsules are fogged and not active. You are the only one. Then, a blibking red light catches your eye.')
        print('The blibnking light is next to a text which says \'AIR\'. Frightned, you realize your almost out of air. You must act quickly. ')
        while True:
            input_1cap = raw_input('You notice a hatchet on the side of your armor: ')
            if str(input_1cap.lower()) == 'take the hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'grab the hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'hold the hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'take hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'grab hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'hold hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'pick up the hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'pick up hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'use hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            elif str(input_1cap.lower()) == 'use the hatchet':
                print('Hatchet taken!')
                hatchetstat = 1
            else:
                print('That didn\'t work!')
                error_count += 1

                if error_count > 3:
                    print('\n--------------------------\n\nSadly, you did not escape quickly enough, and suffocated in your chamber.\n ')
                    print('-------------------------- \n\nPlease play again!')
                    exit()
                else:
                    continue
            return hatchetstat, error_count


