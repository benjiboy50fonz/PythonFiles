class CreateCrawler():
    def __init__(self):
        # Third Strongest
        """
        Similar to the Crawlers or whatever they're called in GOW. They pounce and knock you down. They do not have sharp or dangerous teeth.
        However, they do have extremely sharp and lethal claws.
        """
        self.name = 'Crawler'
        self.ranged_name = 'prepares to pounce on you'
        self.health = 135
        self.melee_attack = 30
        # Tail attack (Above)
        self.distant_attack_success = 20
        self.distant_attack_fail = 0
        self.melee_attack_fail = 0
        # Pounce attack (Above)
        self.distance_hit_chance = 3
        self.distance_hc_defend = 6
        self.melee_attack_chance = 2

class CreateGollum():
    # Weakest
    """
    Small white creature. Similar to the character Gollum from LOTR. Equipped with small vest, knife, and small standard blaster.
    Probably will be the most common in the game. Make changes as necessary.
    """
    def __init__(self):
        self.name = 'Gollum'
        self.ranged_name = 'blaster'
        self.health = 50
        self.melee_attack = 15
        # Small knife slash (Above)
        self.distant_attack_success = 30
        self.distant_attack_fail = 0
        self.melee_attack_fail = 0
        # Small standard blaster shot (Above)
        self.distance_hit_chance = 3
        self.distance_hit_defend = 8 # one out of 8 chances of hitting you in cover!
        self.melee_attack_success = 3 # chance of hitting target


class CreateSkuller():
    # Second Strongest
    """
    Bigger creature, about seven feet tall, has four arms, two of them are holding machete like swords. Kinda looks like a
    drugged up elite from Halo. Very lethal close combat
    """
    def __init__(self):
        self.name = 'Skuller'
        self.ranged_name = 'machete'
        self.health = 150
        self.melee_attack = 40
        # Machete attack (Above)
        self.distant_attack_success = 30
        self.distant_attack_fail = 0
        self.melee_attack_fail = 0
        # Machete throw (Above)
        self.distance_hit_chance = 4
        self.distance_hit_defend = 8
        self.melee_attack_success = 1 # (Guaranteed hit, change if needed!)

class CreateOridd():
    # Default, similar to character, second weakest
    """
    Basic human like creature, elite like mouth, big feet, muscular, and black armor. Can only view the mouth.
    """
    def __init__(self):
        self.name = 'Oridd'
        self.ranged_name = 'plasma shotgun'
        self.health = 95
        self.melee_attack = 40
        # Brutal jagged sword (Above)
        self.distant_attack_success = 45
        self.distant_attack_fail = 0
        self.melee_attack_fail = 0
        # Large plasma shutgun (Above)
        self.distance_hit_chance = 5
        self.distance_hit_defend = 8
        self.melee_attack_success = 3

class CreateDemmalode():
    # Brutal creature, hardest mob in the game, strongest
    def __init__(self):
        self.name = 'Demmalode'
        self.ranged_name = 'RPG weapon'
        self.health = 200
        self.melee_attack = 50
        # Sharp, double-ended spear-like weapon, with electricity flowing through each end (Above)
        self.distant_attack_success = 75
        self.distant_attack_fail = 15 # ONLY RUN THIS IF THE CHANCE MISSES, NOT THE DEFEND!!!
        self.melee_attack_fail = 0
        # RPG-Like weapon, fires fast moving shells, with electric shock in them (Above)
        self.distance_hit_chance = 4
        self.distanct_hit_defend = 7
        self.melee_attack_success = 2 # Tries to get a one out of two hit

class CreateRogue():
    # Rogue Soldier who now serves under the rule of the Forvesaa
    """
    Not really a mob, but it fits here. Pretty much the same characteristics as the char. High skills, not stats though.
    """
    def __init__(self):
        self.name = 'Rogue'
        self.ranged_name = 'AR'
        self.health = 110
        self.melee_attack = 50
        # Long dagger (Above)
        self.distant_attack_success = 65

        # Miss Damages
        self.distant_attack_fail = 0
        self.melee_attack_fail = 0

        # Strong and powerful AR. Same one you gain at the Armory (Above)
        # BELOW DIFFERS FROM MOBS: SHOULD BE CHAR.
        self.distance_hit_chance = 2 # Same start as char. This is the chance of the guy hitting you. The lower the number, the higher the chance of him hitting.
        self.distance_hit_defend = 4 # If you defend the rogue's attack, he has a one out of four chance of shooting you!
        self.melee_attack_success = 2 # Same start as char. If char. doesn't defend, the rogue has a one out of seven chances of missing!
