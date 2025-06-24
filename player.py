from asset import InteractableAsset
from spell import spellbook, Spell
from boss import Boss
class Player(InteractableAsset):
    def __init__(self,name, skills, hp, atk, speed, strength="None", weakness="None"):
        super().__init__(name, skills, hp, atk, speed, strength, weakness)
        self.defend = False

    # during each player turn, you can either attack, defend, use a consumable (BETA), or check enemy info 
    def turn(self):
        self.defend = False
        print(self.name + "'s turn: \n1: Attack\n2: Use Item\n3: Defend\n")
        choice = int(input())
        
        while (choice != 1 or choice != 2 or  choice != 3 or choice != 4):
            print(choice)
            if choice == 1:
                self.attack()
            elif choice == 2:
                self.defend()
            elif choice == 3:
                self.useitem()
            elif choice == 4:
                self.checkinfo() # returns info about all players and all enemies
            else:
                print("Invalid choice\n")
                print("Your turn: \n1: Attack\n2: Use Item\n3: Defend\n")
                choice = input()

    # when attacking, you can choose any of the attacks you know, and it will be used against the enemy you chose    
    def attack(self):
        print("ATTACK")
        print("Which attack shall you use? Please indicate with a number.")
        index = 1
        for skill in self.skills:
            print(str(index) + ". " + skill.description())
            index = index + 1
        print(str(index) + ". Cancel")
        choice = int(input())

        while choice < 1 or choice > len(self.skills):
            print(choice)
            if choice == 1:
                self.attack()
            elif choice == 2:
                self.defend()
            elif choice == 3:
                self.defend()
            elif choice == 4:
                self.defend()
            else:
                print("Invalid choice\n")
                print("What shall you do?\n1: Attack\n2: Defend\n")
                choice = input()
    
    # (BETA) use a consumable item. 
    def useitem(self):
        pass

    # check what your party HP and what your enemies' HP is.
    def checkinfo(self):
        pass

    # skips turn to block a portion of incoming damage.
    def defend(self):
        print(self.name + " is guarding")
        self.defend = True