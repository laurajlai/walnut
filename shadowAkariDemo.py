# Shadow Akari from personAFTB. Fighting her with a full party of Xuanqiang (MC), Yixue, Shengyong, and Luna, with Azu serving as Teddie/navigator/emergency food.  
# Akari deals Fire damage and has no weaknesses, but is strong against Fire (Agi) moves and physical moves are less effective against her.
# The main mechanic of this boss is Abduction - the ability to insta-kill a player character marked with the UFO. She can Abduct characters multiple times, but only one UFO can be on field at any moment.
# If Xuanqiang is downed, the game ends.
from player import Player
from boss import Boss
from spell import spellbook, Spell

# Players
player1 = Player("Xuanqiang", [spellbook['Mazio'], spellbook['Tarunda'], spellbook['Bufula'], spellbook['Kick']], 344, 45, 234, 100, 45, "lightning", "ice")
player2 = Player("Cai Jin", [spellbook['Aqua'], spellbook['Dia'], spellbook['Marakunda'], spellbook['Aques']], 300, 41, 300, 90, 45, "water", "wind")
player3 = Player("Shengyong", [spellbook['Garula'], spellbook['Tarukaja'], spellbook['Magaru'], spellbook['Punch']], 410, 42, 160, 140, 45, "wind", "fire")
player4 = Player("Luna", [spellbook['Agi'], spellbook['Rakukaja'], spellbook['Tetrakarn'], spellbook['Dia']], 350, 43, 210, 120, 45, "fire", "water")
players = [player1, player2, player3, player4]

# Boss
ShadowAkari = Boss("Shadow Akari", [spellbook['Agilao'], spellbook['Maragi'], spellbook['Sweep'], spellbook['Abduction']], 2048, 55, 980, 135, 47, "fire")
enemies = [ShadowAkari]

print("Shadow Akari: I don't belong anywhere! Why can't I be like everyone else and fit in?")
print("Shengyong: ...")
print("Shadow Akari: What good are high grades if no one cares about me? Poor me, I act like I'm above it all, \
    but really I just want someone, anyone, to view me as human!")
print("Akari: No...you aren't me!")

while(player1.hp > 0 and ShadowAkari.hp > 0):
    for player in players:
        player.turn(players, enemies)
    ShadowAkari.turn(players)

if player1.hp <= 0:
    print("Azu: Oh no! Senpai!!!!")

if ShadowAkari.hp <= 0:
    print("Yixue: I never knew Akari had her own Shadow too...")
    print("Luna: Akari! Are you ok?!")
    print("Akari: Nggggh...")
    print("Akari: I...")
    print("Akari: ...You're right. I pushed away people because I thought they would reject me…but that's not true.")
    print("Akari: I simply never gave anyone the chance to reach out. You are me. Now let's face the future together.")
    print("The strength of heart required to face oneself has been made manifest...")
    print("Akari has obtained the facade used to overcome life's hardships, the Persona Archimedes!")