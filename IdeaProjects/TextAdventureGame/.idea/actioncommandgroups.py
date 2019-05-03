"""
This file consists of the general commands and actions for the story.
Import each action separatley through phases like the intro text.
If the command is a general like the score increase, define it here.
IMPORTANT: REMEMBER PHASES AND COMMANDS ARE DIFFERENT!!!
PHASES TELL STORIES, COMMANDS PERFORM ACTIONS!
Please be careful with this file for it is very fragile, and add comments where and when neccessary!
STATUS: UNDER CONSTRUCTION
"""
from Phases.introtext_phase1 import IntroText_Phase1
from Phases.chamberoom_phase2 import ChamberRoom_Phase2
from Phases.largehallway_phase3 import LargeHallway_Phase3
from Phases.commsroom_phase4 import CommsRoom_Phase4

from SeparateCommands.scorecommand import ScoreCommands
from SeparateCommands.returnstatscommand import ReturnStats

from Miscellaneous.weaponclasses import Weapons

class StoryMethods():
    def __init__(self, name, gender):
        self.name = str(name)
        if str(gender.lower()) == 'male':
            self.gender = 0
            self.gender_stat = 'Male'
        elif str(gender.lower()) == 'female':
            self.gender = 1
            self.gender_stat = 'Female'
        else:
            self.gender = 0
            self.gender_stat = 'Male'

        self.health = 100
        self.armor = 0

        self.ammo_storage_stat = 0
        self.armor_storage_stat = 0
        self.broken_console_stat = 0

        self.score = 0

        self.error_count = 0

#       Whether you have the weapons or not (Used in ReturnStats)
#        self.p_weapon = False
#        self.s_weapon = False

        self.default_damage = 25 # (Hands. Should never be used, unless another way out without hatchet is created.)
        self.hatchet_stat = 0

#       Weapon Stats! Look for more in weaponclasses.py!

        self.pistol_stat = 0

        self.ar_stat = 0

        self.critical_hit_chance_stack = 0

        self.block_fail_chance = 2 # One out of two chances of failing your defence
        self.melee_attack_damage = 50 # Default basic hatchet damage

        # Weapon Damages
        self.secondary_distance_attack_damage = 35 # Pistol. Primary at the beginning. Check armory for primary. Until then, call this.
        self.primary_distance_attack_damage = 65 # AR. Earned later in the game. Find at Armory.

        self.critical_hit_chance = 15 # Starting chance, lower is better!

        # Miss Damages
        self.melee_attack_miss_damage = 0
        self.distance_attack_miss_damage = 0

        self.distance_miss_chance = 4 # Starting accuracy. Higher is better. (One out of four chances of missing your shot.)
        self.distance_miss_defence = 2 # ONLY USED WITH ROGUE. IF THEY TAKE COVER, RUN THIS CHANCE OF MISSING AS ARGUEMENT
        self.melee_attack_miss_chance = 8 # Starting accuracy. Higher is better.
        self.melee_attack_miss_defence = 3 # ONLY USED WITH ROGUE. IF THEY DEFEND OR ROLL, RUN THIS CHANCE OF MISSING AS ARGUEMENT

        # Add Phases and Commands Below!

    def BeginStory(self, player):
        pistol = Weapons()
        assault_rifle = Weapons()
        """
        self.hatchet_stat, self.error_count = IntroText_Phase1.Intro_text(self.hatchet_stat) # Could have renamed intro_text -> phase 1, but did not for detail!
        ChamberRoom_Phase2.BreakGlass(self.hatchet_stat, self.error_count, self.health)
        return_v1 = ChamberRoom_Phase2.ExitCapsuleRoom()
        if return_v1 == '0':
            pass
        else:
            print('error')
        while True:
            return_v2 = LargeHallway_Phase3.OpenHallway()
            if return_v2 == '0':
                return_v2b = \
                    LargeHallway_Phase3.MaintenanceDesk(pistol)
                continue

            elif return_v2 == '1':
                return_v2c, self.armor, self.armor_storage_stat, self.ammo_storage_stat, self.score = \
                    LargeHallway_Phase3.StorageCloset(pistol, self.armor, self.ammo_storage_stat, self.armor_storage_stat, self.score)
                if return_v2c == '0':
                    continue

            elif return_v2 == '2':
                return_2vd = ChamberRoom_Phase2.ExitCapsuleRoom()
                if return_2vd == '0':
                    continue

            elif return_v2 == '3':
                return_2ve = LargeHallway_Phase3.LargeDoor(self.broken_console_stat)
                if return_2ve == '0':
                    continue

                elif return_2ve == '1':
                    self.score = ScoreCommands.IncreaseScoreMega(self.score) # Continues on through the door
                    break
            else:
                print('Balls.')
            """
        CommsRoom_Phase4.CommsRoom(pistol, assault_rifle, player)
        print(player.block_fail_chance)
