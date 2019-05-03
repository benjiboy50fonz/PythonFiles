"""
This file will return basic information when requested. Run it as an option during some inputs.
Extend this list as neccessary.
STATUS: WORKING
"""

def ReturnPlayerStats(score, health, armor):
    player_stat_string = 'Score = ' + str(score) + '\nHealth = ' + str(health) + ' hps \nArmor = ' + str(armor) + ' hps'
    return player_stat_string

class ReturnStats():

    @classmethod
    def ReturnAllStats(self, score, health, armor):
        from Miscellaneous.weaponclasses import Weapons
        weapon_stats_string = Weapons.returnGunStats()
        player_stat_string = ReturnPlayerStats(score, health, armor)
        print(player_stat_string + weapon_stats_string)


#   Used in weaponclasses.py. DO NOT DELETE!

    @classmethod
    def ReturnWeaponStats(self, p_weapon, s_weapon, p_mag_count, s_mag_count, p_start_amount, s_start_amount):

#       Checks Status of the weapons.
        if p_weapon == 0 and s_weapon == 0:
            string_primary = 'None'
            string_secondary = 'None'
        elif p_weapon == 0 and s_weapon == 1:
            string_primary = 'None'
            string_secondary = 'Pistol'
        elif p_weapon == 1 and s_weapon == 0:
            string_primary = 'Assault Rifle'
            string_secondary = 'None'
        else:
            string_primary = 'Assault Rifle'
            string_secondary = 'Pistol'

        weapon_stat_string = '\nPrimary Weapon = ' + string_primary + '\nSecondary Weapon = ' + string_secondary + \
                             '\nPrimary Weapon Magazine Count = ' + str(p_mag_count) + '\nSecond Weapon Magazine Count = ' + \
                             str(s_mag_count) + '\nRemaining Shots in Primary Weapon Magazine = ' + \
                             str(p_start_amount) + '\nRemaining Shots in Secondary Weapon Magazine = ' + str(s_start_amount)

        return weapon_stat_string


