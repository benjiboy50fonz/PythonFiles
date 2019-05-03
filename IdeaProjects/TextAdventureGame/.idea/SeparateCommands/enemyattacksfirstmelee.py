class EnemyAttacksFirstMeleeClass:

    @classmethod
    def enemyAttacksFirstMelee(self, enemy_list, pistol_obj, ar_object, player_obj):
        from deathcommand import PlayerDeath
        from fightcommand import Fight



        self.hatchet_phrases = ['melee him',
                            'melee it',
                            'melee her',
                            'melee them',
                            'melee',
                            'hand to hand',
                            'punch him',
                            'punch her',
                            'punch them',
                            'punch it',
                            'hit it',
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

        enemy_count = len(enemy_list)
        end_count = len(enemy_list)

        if enemy_count <= 0:
            print('ERROR')
            exit()
        while enemy_count > 0:
            if enemy_count == 0:
                print('The fight is now over. ')
                print(enemy_list)

            for i in enemy_list:
                damage, result, text = Fight.minAndMaxHostileDamage(i.melee_attack_fail,
                                                               i.melee_attack, i.melee_attack_success, player_obj.block_fail_chance)

                if player_obj.health <= int(damage):
                    death = PlayerDeath('mob', str(i.name))
                    exit()
                else:
                    player_obj.health -= int(damage)

                if result == True and damage != 0:
                    print('The ' + i.name + ' attacked you and dealt ' + str(damage) + ' damage! (CURRENT HEALTH = ' + str(player_obj.health) + ')\n')

                elif result == False and text == 2:
                    print('The ' + i.name + ' missed it\'s attack!\n')

                elif result == False and text == 1:
                    print('You block the ' + i.name + '\'s attack, taking no damage!\n')

            if enemy_count == 1:
                print('You prepare to attack after the ' + enemy_list[0].name + ' finishes it\'s attack!\n')

            elif enemy_count > 1:
                print('The enemies finish their attacks and await yours!\n')

            attack_method = raw_input('How would you like to attack?: ')
            if str(attack_method.lower()) in self.hatchet_phrases:
                attack_choice = 'hatchet'
                chosen_enemy = enemy_list[0]
                damage_dealt = Fight.playerDamageCalc('hatchet', player_obj, pistol_obj,
                                             ar_object, player_obj.melee_attack_miss_chance, chosen_enemy)

                if damage_dealt == 0:
                    pass

                else:
                    if enemy_count >= 1:
                        if chosen_enemy.health > damage_dealt:
                            chosen_enemy.health -= damage_dealt
                        elif chosen_enemy.health <= damage_dealt:
                            enemy_list.pop(0)
                            enemy_count -= 1
                            print('You kill the ' + chosen_enemy.name + ' with your hatchet!')

                    else:
                        print('ERROR')

                if enemy_count > 0:
                    continue

                return end_count, attack_choice, player_obj

            elif str(attack_method.lower()) in self.shoot_phrases:
                attack_choice = 'pistol'
                chosen_enemy = enemy_list[0]
                damage_dealt = Fight.playerDamageCalc('pistol', player_obj, pistol_obj,
                                                      ar_object, player_obj.melee_attack_miss_chance, chosen_enemy)
                if damage_dealt == 'no':
                    continue






            else:
                print('You did not attack quick enough, and the enemy readied themselves for another attack!\n')
                continue

