"""
This file creates and preforms the weapon functions, ranging from picking them up, all the way to firing them.
STATUS: WORKING
"""
# Tip!: Return the damage value for the shoot method!

class Weapons():

    #@classmethod
    def __init__(self):
        self.ar_stat = 0
        self.ar_mag_size = 20
        self.ar_mag_count = 0
        self.ar_mag_start_count = 0
        self.pistol_stat = 0
        self.pistol_mag_size = 8
        self.pistol_mag_count = 0
        self.pistol_mag_current_count = 0

    #@classmethod
    def equipAR(self):
        self.ar_stat = 1
        self.ar_mag_size = 20
#       Describe one spare mag in text (Belowi)
        self.ar_mag_count = 1
        self.ar_mag_start_count = 20

    #@classmethod
    def equipPistol(self):
        self.pistol_stat = 1
        self.pistol_mag_size = 8
#       Describe two spare mag in text (Below)
        self.pistol_mag_count = 2
        self.pistol_mag_current_count = 8
        self

    #@classmethod
    def increasePistolMags(self, val):
        self.pistol_mag_count += val
        print('Ammo Taken! ')

    #@classmethod
    def returnGunStats(self):
        from SeparateCommands.returnstatscommand import ReturnStats
        self.weapon_stat_string = ReturnStats.ReturnWeaponStats(self.ar_stat, self.pistol_stat, self.ar_mag_count,
                                              self.pistol_mag_count, self.ar_mag_start_count,
                                              self.pistol_mag_start_count)

        return self.weapon_stat_string
