class EnemyAttacksFirstGunClass:

    @classmethod
    def enemyAttacksFirstGun(self, enemy_list, pistol_obj, ar_object, player_obj):
        from deathcommand import PlayerDeath
        from fightcommand import Fight


        self.take_cover_phrases = ['hide',
                                   'take cover',
                                   'cover',
                                   'take hide',
                                   'get down',
                                   'run for cover',
                                   'hide in cover',
                                   'hide at cover'
                                   ]

        self.counter_phrases = []

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

        self.hatchet_phrases = ['melee him',
                                'melee it',
                                'melee her',
                                'melee them',
                                'melee',
                                'hand to hand',
                                'punch him',
                                'punch her',
                                'punch them',
                                'punch it'
                                'use my hatchet',
                                'use the hatchet',
                                'swing hatchet',
                                'swing the hatchet',
                                'attack with hatchet',
                                'attack them with the hatchet',
                                'attack them with hatchet',
                                'attack it with the hatchet',
                                'attack it with hatchet',
                                'attack with the hatchet',
                                'fight with the hatchet',
                                'fight with hatchet',
                                'hatchet',
                                'use the hatchet',
                                'use hatchet',
                                'fight the hatchet']

        enemy_count = len(enemy_list)

        if enemy_count <= 0:
            print('ERROR here?')
        while enemy_count > 0:
            if enemy_count > 0:
                pass
            else:
                print('The fight is now over. ')
                print(enemy_list)
                break

            for i in enemy_list:
                damage, chance, defence = Fight.minAndMaxHostileRangedDamage(i)

                defence_or_no = raw_input('\nWhat do you do?: ')
                if str(defence_or_no.lower()) in self.take_cover_phrases:
                    print('You take nearby cover!')

                    if chance == 1:
                        print('\nThe enemy missed it\'s shot, and it\'s shot wizzed far from you. ' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')
                        damage = 0


                    else:
                        if defence == 1:
                            if reason == 1:
                                print('\nYou did not reach your cover quick enough, and the enemy hit you, dealing ' + str(damage) + '!' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')
                            else:
                                print('\nYour cover did not prevent the enemies attack, and you were hit, taking ' + str(damage) + ' damage!' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')

                            if player_obj.health > damage:
                                player_obj.health -= damage

                            else:
                                death = PlayerDeath('mob', str(i.name))
                                exit()

                        else:
                            print('\nYou took cover successfully, surviving the enemy attack!' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')
                            damage = 0

                else:
                    print('\nYou did not act well enough, and the enemy attacked')
                    if chance == 1:
                        print('The enemy landed a good shot on you, dealing ' + str(damage) + ' damage!' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')

                        if player_obj.health > damage:
                            player_obj.health -= damage

                        else:
                            death = PlayerDeath('mob', str(i.name))
                            exit()

                    else:
                        print('\nThankfully, the enemy missed it\'s shot!' + ' (CURRENT HEALTH = ' + str(player_obj.health) + ')')
                        damage = 0


            if enemy_count == 1:
                print('\nYou prepare to attack after the ' + enemy_list[0].name + ' finishes it\'s attack!')

            else:
                print('\nThe enemies finish their attacks and await yours!')


### BELOW IS FOR THE PLAYER'S ATTACK!!!

            attack_method = raw_input('\nHow would you like to attack?: ')
            print('here1')
            if str(attack_method.lower()) in self.hatchet_phrases:
                print('here')
                attack_use_object = player_obj
                attack_choice = 'hatchet'
                chosen_enemy = enemy_list[0]
                damage_dealt = Fight.playerDamageCalc('hatchet', player_obj, pistol_obj,
                                                  ar_object, player_obj.melee_attack_miss_chance, chosen_enemy)

                if damage_dealt == 0:
                    pass
                else:
                    if enemy_count >= 1:
                        if chosen_enemy.health > damage_dealt:
                            chosen_enemy.health = chosen_enemy.health - damage_dealt
                        elif chosen_enemy.health <= damage_dealt:
                            enemy_list.pop(0)
                            enemy_count -= 1
                            print('You kill the ' + chosen_enemy.name + ' with your hatchet!')

                    else:
                        print('ERROR 2')

                    continue

                return attack_choice, attack_use_object

            elif str(attack_method.lower()) in self.shoot_phrases:
                pass
