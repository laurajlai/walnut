import math
class Spell(object):
    def __init__(self,name, type, effect, aoe, element="Stella", affected_stat="None"):
        self.name = name
        self.element = element # Zio, Garu, Bufu, Agi, Aqua, Hama, Mudo, None (if non damaging)
        self.affected_stat = affected_stat # could be ATK, DEF, HP, or EVN
        self.type = type # ex. buff, debuff, damage, heal
        self.effect = effect # ex. light, medium, heavy
        self.aoe = aoe # ex. single target or AoE

        # certain types of debuffs and buffs have a countdown, so they will be effective for 3 turns at once
        if self.type == "buff" or self.type == "debuff":
            self.countdown = 3
        else:
            self.countdown = 0

    # prints a quick description of the spell, used when player clicks "help"
    def description(self):
        to_return = "Invalid spell."
        if self.type == "damage":
            to_return = self.name + ": This spell does " + self.effect + " " + self.element + " damage to " + self.aoe + " targets."
        elif self.type == "buff":
            to_return = self.name + ": This spell increases " + self.affected_stat + " by a " + self.effect + " amount."
        elif self.type == "debuff":
            to_return = self.name + ": This spell reduces " + self.affected_stat + " by a " + self.effect + " amount."
        elif self.type == "heal":
            to_return = self.name + ": This spell heals " + self.aoe + " for a " + self.effect + " amount."
        return to_return

    # does the spell chosen by player(s) on the chosen enemy(s)
    # this only applies to players, enemies damage is calculated including the players' defense stat
    def player_spell(self, caster, player_targets, enemy_targets):
        # attack spells: attack is calculated based on light/medium/heavy, player level, player attack, and player element
        if self.type == "attack":
            # decrease enemy HP using the damage formula
            for enemy in enemy_targets:
                pass
            # damage calculation
            num_damage = 3 * math.sqrt((caster.atk*caster.level)/4)
            if self.effect == "light":
                num_damage *= 0.5
            elif self.effect == "medium":
                num_damage *= 0.75
            else:
                num_damage *= 0.9

            # STAB / weakness hitting
            if caster.null == self.element:
                num_damage *= 2
            
            # subtract enemy DEF
            num_damage -= enemy.dfn/100
            
            effect = "Does " + str(num_damage) + " damage."

        # buff spells: the designated stat goes up by a percentage of the player's stat (ex. ATK boost is calculated on the caster's ATK)
        elif self.type == "buff":
            increase = 1.6 * caster.affected_stat
            effect = "New attack stat is " + str(increase) + "."
        # debuff spells: the designated stat goes down by a percentage of the player's stat (ex. DEF debuff is calculated on the caster's DEF)
        elif self.type == "debuff":
            decrease = 0.8 * caster.atk
        # heal spells: heal is calculated based on light/medium/heavy & player level
        elif self.type == "heal":
            pass
        else:
            print("For some reason, this spell didn't work! Terrible vegetables!")
        return effect

# definition of all spells used in the Shadow Akari fight (more can be added later on)
spellbook = {
    "Mazio": Spell(name="Mazio", type="damage", effect="light", aoe="all", element="lightning"),
    "Tarunda": Spell(name="Tarunda", type="debuff", effect="light", aoe="one", affected_stat="ATK"),
    "Bufula": Spell(name="Bufula", type="damage", effect="medium", aoe="one", element="ice"),
    "Kick": Spell(name="Kick", type="damage", effect="light", aoe="all", element="physical"),
    "Aqua": Spell(name="Aqua", type="damage", effect="light", aoe="one", element="water"),
    "Dia": Spell(name="Dia", type="heal", effect="light", aoe="one", affected_stat="HP"),
    "Marakunda": Spell(name="Marakunda", type="debuff", effect="light", aoe="all", affected_stat="def"),
    "Aques": Spell(name="Aques", type="damage", effect="medium", aoe="one", element="water"),
    "Garula": Spell(name="Garula", type="damage", effect="medium", aoe="one", element="wind"),
    "Tarukaja": Spell(name="Tarukaja", type="buff", effect="light", aoe="one", affected_stat="atk"),
    "Magaru": Spell(name="Magaru", type="damage", effect="medium", aoe="one", element="wind"),
    "Punch": Spell(name="Punch", type="damage", effect="light", aoe="one", element="physical"),
    "Sweep": Spell(name="Sweep", type="damage", effect="light", aoe="all", element="physical"),
    "Agilao": Spell(name="Agilao", type="damage", effect="medium", aoe="one", element="fire"),
    "Rakukaja": Spell(name="Rakukaja", type="buff", effect="light", aoe="one", affected_stat="def"),
    "Tetrakarn": Spell(name="Tetrakarn", type="buff", effect="medium", aoe="one", affected_stat="evn"),
    "Maragi": Spell(name="Maragi", type="damage", effect="light", aoe="all", element="fire"),
    "Abduction": Spell(name="Abduction", type="debuff", effect="heavy", aoe="one", affected_stat="evn")
}
