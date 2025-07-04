# interactable asset, applies for both bosses and players.
class InteractableAsset(object):
   def __init__(self, name, skills, hp, atk, dfn, speed, level, strength="None", weakness="None"):
      self.name = name
      self.skills = skills
      self.hp = hp
      self.currenthp = hp
      self.atk = atk
      self.dfn = dfn
      self.speed = speed
      self.level = level
      self.null = strength # immunities/strengths
      self.weakness = weakness # weaknesses
      self.buffs = []
      self.debuffs = []
      # TODO: ADD ITEMS
      
   def turn():
      print("Default code that enables inheritance")
      pass
