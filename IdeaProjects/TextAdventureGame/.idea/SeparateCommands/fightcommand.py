class Fight():

    def __init__(self):
        self.melee_phrases = ['melee him',
                          'melee it',
                          'melee her',
                          'melee them',
                          'melee',
                          'hand to hand',
                          'punch him',
                          'punch her',
                          'punch them',
                          'punch it']

        self.shoot_phrases = ['shoot him',
                               'fire at him',
                               'shoot at him',
                               'shoot',
                               'fire',
                               'shoot at them',
                               'shoot at her',
                               'shoot at it',
                               'fire at her',
                               'fire at them',
                               'fire at it']

        self.nevermind_phrases = ['nevermind',
                                  'go back',
                                  'return',
                                  'forget it',
                                  'i do not want to do this',
                                  'go backwards']

    @classmethod
    def rand_two(self):
        from random import randint
        return randint(0, 2)

    @classmethod
    def spawnMobsFight(self, number_of_crawlers, number_of_gollums, number_of_skullers,
                   number_of_oridds, number_of_demmalodes, number_of_rogues):

        import Miscellaneous.mobclasses

        def createobjects(spawn_number, type): # Use the Create_____ Command for type arguement
            from Miscellaneous.mobclasses import CreateCrawler, CreateGollum, CreateSkuller, \
                CreateOridd, CreateDemmalode, CreateRogue

            if str(type.lower()) == 'crawler':
                classtype = CreateCrawler()
                sort_class = 'C'

            elif str(type.lower()) == 'gollum':
                classtype = CreateGollum()
                sort_class = 'G'

            elif str(type.lower()) == 'skuller':
                classtype = CreateSkuller()
                sort_class = 'S'

            elif str(type.lower()) == 'oridd':
                classtype = CreateOridd()
                sort_class = 'O'

            elif str(type.lower()) == 'demmalode':
                classtype = CreateDemmalode()
                sort_class = 'D'

            elif str(type.lower()) == 'rogue':
                classtype = CreateRogue()
                sort_class = 'R'

            else:
                print('Error: Fight Command; problem assigning classes to variables???')

            current_mobs = []

            if spawn_number == 1:
                object1 = classtype
                current_mobs.append(object1)

            elif spawn_number == 2:
                object1 = classtype
                object2 = classtype
                current_mobs.append(object1)
                current_mobs.append(object2)

            elif spawn_number == 3:
                object1 = classtype
                object2 = classtype
                object3 = classtype
                current_mobs.append(object1)
                current_mobs.append(object2)
                current_mobs.append(object3)

            elif spawn_number == 4:
                object1 = classtype
                object2 = classtype
                object3 = classtype
                object4 = classtype
                current_mobs.append(object1)
                current_mobs.append(object2)
                current_mobs.append(object3)
                current_mobs.append(object4)

            elif spawn_number == 5:
                object1 = classtype
                object2 = classtype
                object3 = classtype
                object4 = classtype
                object5 = classtype
                current_mobs.append(object1)
                current_mobs.append(object2)
                current_mobs.append(object3)
                current_mobs.append(object4)
                current_mobs.append(object5)

            elif spawn_number == 0:
                pass

            else:
                print('Error creating mobs!')

            return current_mobs

# Add func here
#number_of_crawlers, number_of_gollums, number_of_skullers,
#                number_of_oridds, number_of_demmalodes, number_of_rogues):

        crawler_object_list = createobjects(number_of_crawlers, 'crawler')
        gollum_object_list = createobjects(number_of_gollums, 'gollum')
        skuller_object_list = createobjects(number_of_skullers, 'skuller')
        oridd_object_list = createobjects(number_of_oridds, 'oridd')
        demmalode_object_list = createobjects(number_of_demmalodes, 'demmalode')
        rogue_object_list = createobjects(number_of_rogues, 'rogue')

        total_mob_list = crawler_object_list + gollum_object_list + skuller_object_list + \
                         oridd_object_list + demmalode_object_list + rogue_object_list

        try:
            self.total_mob_count = int(number_of_crawlers) + int(number_of_gollums) + int(number_of_skullers) + \
                                   int(number_of_oridds) + int(number_of_demmalodes) + int(number_of_rogues)
        except:
            pass # Add errors and solutions

        if self.total_mob_count > 25:
            print('You can not have that many mobs! (Change if you REALLLY want to!)')
            exit()

        return total_mob_list

        """
        return crawler_object_list, gollum_object_list, \
               skuller_object_list, oridd_object_list, \
               demmalode_object_list, rogue_object_list
        """

    @classmethod
    def minAndMaxHostileDamage(self, min_damage, max_damage, chance_of_hit, defence_chance):
        from random import randint
        num = randint(min_damage, max_damage)
        chance = randint(1, chance_of_hit)
        defence = randint(1, defence_chance)
        if chance == 1:
            if defence == 1:
                text = 0
                result = True
            else:
                text = 1
                num = 0
                result = False
        else:
            result = False
            num = 0
            text = 2

        return num, result, text

# For ranged defence (Below)
    @classmethod
    def minAndMaxHostileRangedDamage(self, enemy):
        from random import randint

        num = enemy.distant_attack_success #min_damage
        chance = randint(1, enemy.distance_hit_chance)
        defence = randint(1, enemy.distance_hit_defend)
        if str(enemy.ranged_name.lower()) == 'prepares to pounce on you':
            print('The Crawler ' + str(enemy.ranged_name) + '!')

        elif str(enemy.ranged_name.lower()) == 'machete':
            print('The Skuller pulls their arm back, ready to throw their ' + str(enemy.ranged_name) + '!')

        else:
            print('The ' + enemy.name + ' lines you up with their ' + str(enemy.ranged_name) + '!')


        return num, chance, defence

    @classmethod
    def playerDamageCalc(self, weapon, player_object, pistol_object, ar_object, miss_chance, chosen_enemy):
        from random import randint
        if str(weapon.lower()) == 'hatchet':
            attack_hit = randint(0, miss_chance) # For miss chance, higher is better... see ACG!
            if attack_hit == 0:
                print('\nYou swing your hatchet and miss your target, dealing no damage!')
                total_damage = 0
            elif attack_hit > 0:
                critical_chance = randint(0, player_object.critical_hit_chance)
                if critical_chance == 0:
                    total_damage = player_object.melee_attack_damage * 1.5
                    total_damage = int(total_damage)

                else:
                    total_damage = player_object.melee_attack_damage

                if player_object.melee_attack_damage == total_damage:
                    print('\nYou swing your hatchet and deal ' + str(total_damage) + ' damage to the ' + str(chosen_enemy.name) + '!')

                elif player_object.melee_attack_damage < total_damage:
                    print('\nYou swing your hatchet and deal ' + str(total_damage) + ' damage, landing a critical hit on the ' + str(chosen_enemy.name) + '!')

                else:
                    print('ERROR line 205 ')


            return int(total_damage)


        elif str(weapon.lower()) == 'pistol':
            # Checks pistol to make sure everything is a-ok!
            if pistol_object.pistol_mag_current_count <= 0 and pistol_object.pistol_mag_count <= 0:
                print('You are out of pistol ammunition!')
                return 'no'

            if player_object.pistol_stat == 0:
                print('That is not available!')
                return 'no'



        elif str(weapon.lower()) == 'ar':
            pass


    @classmethod
    def fightStart(self, number_of_crawlers, number_of_gollums, number_of_skullers,
                   number_of_oridds, number_of_demmalodes, number_of_rogues,
                   player_attacks_first_check, pistol_object, ar_object, player):
        from SeparateCommands.enemyattacksfirstmelee import EnemyAttacksFirstMeleeClass
        from SeparateCommands.enemyattacksfirstgun import EnemyAttacksFirstGunClass
        import SeparateCommands.enemyattacksfirstmelee
        import SeparateCommands

        self.melee_phrases = ['melee him',
                              'melee it',
                              'melee her',
                              'melee them',
                              'melee',
                              'hand to hand',
                              'punch him',
                              'punch her',
                              'punch them',
                              'punch it']

        if player_attacks_first_check == True:
            while True:
                total_mobs_list = self.spawnMobsFight(number_of_crawlers, number_of_gollums, number_of_skullers,
                                                      number_of_oridds, number_of_demmalodes, number_of_rogues)
                melee_or_attack_input = raw_input('Melee or shoot?: ')
                if str(melee_or_attack_input.lower()) in self.melee_phrases:
                    pass

                elif str(melee_or_attack_input.lower()) in self.shoot_phrases:
                    pass
            # Add shoot command here

                else:
                    print('Please specify how you would like to engage!')
                    continue

        elif player_attacks_first_check == False:
            total_mobs_list = self.spawnMobsFight(number_of_crawlers, number_of_gollums, number_of_skullers,
                                                  number_of_oridds, number_of_demmalodes, number_of_rogues)
            print('\n')

            combat_type = 0 #Fight.rand_two()
            if combat_type == 0:
                if len(total_mobs_list) > 1:
                    print('The enemies attack you first!')
                else:
                    print('The ' + total_mobs_list[0].name + ' attacks first!')

                end_count, attack_used, attack_used_object = SeparateCommands.enemyattacksfirstmelee.EnemyAttacksFirstMeleeClass.enemyAttacksFirstMelee(total_mobs_list, pistol_object, ar_object, player)
                return end_count, attack_used, attack_used_object

            else:
                if len(total_mobs_list) > 1:
                    print('The enemies attack you first!')
                else:
                    print('The ' + total_mobs_list[0].name + ' attacks first!')

                attack_used, attack_used_object = EnemyAttacksFirstGunClass.enemyAttacksFirstGun(total_mobs_list, pistol_object, ar_object, player)

                return end_count, attack_used, attack_used_object

    @classmethod
    def fightEnd(self, player, enemy_start_count, attack_used, attack_used_object): # Attack used might be pistol
        from SeparateCommands.scorecommand import ScoreCommands

        for i in range(enemy_start_count):
            player.score = ScoreCommands.IncreaseScoreStandard(player.score)

        if player.critical_hit_chance_stack == 5:
            player.critical_hit_chance -= 1
            player.critical_hit_chance = 0

        else:
            player.critical_hit_chance_stack += 1

        if str(attack_used.lower()) == 'hatchet':
            player.block_fail_chance += 1

        elif str(attack_used.lower) == 'pistol':
            pass
        elif str(attack_used.lower()) == 'ar':
            pass
        else:
            print('\nError')

    #TODO Finish rewards from fights, check to make sure melee works!