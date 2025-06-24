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

    # does the spell chosen by player on the chosen enemy
    def spell(self, player, enemy):
        pass


# definition of all spells used in the Shadow Akari fight (more can be added later on)
spellbook = {
    "Mazio": Spell(name="Mazio", type="damage", effect="light", aoe="all", element="lightning"),
    "Tarunda": Spell(name="Tarunda", type="debuff", effect="light", aoe="one", affected_stat="ATK"),
    "Bufu": Spell(name="Bufu", type="damage", effect="light", aoe="one", element="ice"),
    "Kick": Spell(name="Kick", type="damage", effect="light", aoe="all", element="physical"),
    "Aqua": Spell(name="Aqua", type="damage", effect="light", aoe="one", element="water"),
    "Dia": Spell(name="Dia", type="heal", effect="light", aoe="one", affected_stat="HP"),
    "Marakunda": Spell(name="Marakunda", type="debuff", effect="light", aoe="all", affected_stat="DEF"),
    "Aques": Spell(name="Aques", type="damage", effect="medium", aoe="one", element="water"),
    "Garu": Spell(name="Garu", type="damage", effect="light", aoe="one", element="wind"),
    "Tarukaja": Spell(name="Tarukaja", type="buff", effect="light", aoe="one", affected_stat="ATK"),
    "Magaru": Spell(name="Magaru", type="damage", effect="medium", aoe="one", element="wind"),
    "Punch": Spell(name="Punch", type="damage", effect="light", aoe="one", element="physical"),
    "Sweep": Spell(name="Sweep", type="damage", effect="light", aoe="all", element="physical"),
    "Agi": Spell(name="Agi", type="damage", effect="light", aoe="one", element="fire"),
    "Rakukaja": Spell(name="Rakukaja", type="buff", effect="light", aoe="one", affected_stat="DEF"),
    "Tetrakarn": Spell(name="Tetrakarn", type="buff", effect="medium", aoe="one", affected_stat="EVN"),
    "Maragi": Spell(name="Maragi", type="damage", effect="light", aoe="all", element="fire"),
    "Abduction": Spell(name="Abduction", type="debuff", effect="heavy", aoe="one", affected_stat="EVN")
}
