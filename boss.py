from asset import InteractableAsset
from spell import spellbook, Spell
from player import Player
class Boss(InteractableAsset):
    def __init__(self,name, skills, hp, atk, speed, strength="None", weakness="None"):
        super().__init__(name, skills, hp, atk, speed, strength, weakness)
        self.hasSummon = False # technically applies for any enemy that can spawn another enemy, in Akari's case this would be the UFO
        self.ICD = 3 # ensures the boss can't spam its most powerful moves
    
    # shadow Akari can randomly attack with any of the moves in her arsenal, but there is a three-turn cooldown for Abduction
    def turn():
        pass
