from spell import Spell
import random

# interactable asset, applies for both bosses and players.
class InteractableAsset(object):
   def __init__(self,name, skills, hp, atk, speed, strength="None", weakness="None"):
      self.name = name
      self.skills = skills
      self.hp = hp
      self.atk = atk
      self.speed = speed
      self.null = strength # immunities
      self.weakness = weakness # weaknesses
      self.buffs = []
      self.debuffs = []
      # TODO: ADD ITEMS
      
   def turn():
      print("Default code that enables inheritance")
      pass
