class PlayerDeath():

    def __init__(self, cause_of_death, mob_type=0):
        if str(cause_of_death.lower()) == 'mob':
            print('-------------------------- \n\nThe ' + str(mob_type) + ' killed you. You gave it your best effort, however it was not good enough. '
                                                                          '\nWe hope to see you again in Iosis soldier!\n\n' + '-------------------------- ')
