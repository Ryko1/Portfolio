
from background_pkg import functions
from background_pkg.class_ext import base
import sys
import time
import random

functions.loading()


while True:
    print("\n == Character Selection ==")
    print("→Warlock \n→Rogue \n→Brawler \n→Knight")
    player = input("Choose your character: ").lower()

    character, my_hp, my_dmg, my_nim, my_def = functions.character(
        player.lower())

    if character:
        # --adds class bonus to rolled stats
        my_rhp = functions.roll_attributes() + my_hp
        my_rdmg = functions.roll_attributes() + my_dmg
        my_rnim = functions.roll_attributes() + my_nim
        my_rdef = functions.roll_attributes() + my_def

    if player == "warlock":
        print("\nWarlock Bonus: +500 Damage")
    elif player == "rogue":
        print("\nRogue Bonus: +500 Nimble")
    elif player == "brawler":
        print("\nBrawler Bonus: +500 Health")
    elif player == "knight":
        print("\nKnight Bonus: +250 Damage"
              "\n              +250 Defense")
    else:
        print("Character not found!")

    print("You have chosen to be a:", character,)
    input("Press any key to roll the dice to decide your skills!")
    print("Health:", my_rhp,
          "\nDamage:", my_rdmg,
          "\nNimble:", my_rnim,
          "\nDefense:", my_rdef)
    break

enemy_attributes = functions.enemies("azazel")
enemy_name, e_hp, e_dmg, e_nim, e_def = enemy_attributes
f_enem = base(enemy_name, e_hp, e_dmg, e_nim, e_def)
f_char = base(character, my_rhp, my_rdmg, my_rnim, my_rdef)

input("\nPress any key to start your adventure! ")
print("\nAs you set foot in your adventure, a",
      f_enem.name, "tried to attack you \nfrom the back...")
print("You managed to see the",
      f_enem.name, "coming and dodged his attack!")


while True:

    up_hp = f_char.hp
    up_nim = f_char.nim
    up_def = f_char.defe
    up_ehp = f_enem.hp
    up_enim = f_enem.nim
    up_edef = f_enem.defe

    if up_hp <= 0:
        print("Fatality!")
        print("You lose!")
        sys.exit()

    elif up_ehp <= 0:
        print("The", f_enem.name, "has has collapsed!")
        print("You Win!")
        break

    a = input("\n→Attack\n→Defend\n→Dodge\n→Flee\nWhat will you do?").lower()
    b = functions.enemy_choice()

    if a == "attack" and b == "attack":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        p = random.randint(1, 10)
        e = random.randint(1, 10)
        if p > e:
            f_char.dmg /= 2
            f_enem.hp -= f_char.dmg
            print("The", f_char.name, "deals", f_char.dmg,
                  "damage to the", str(f_enem.name) + "!")
            print("The", str(f_enem.name) + "'s", "current HP:", f_enem.hp)

        elif p < e:
            f_enem.dmg /= 2
            f_char.hp -= f_enem.dmg
            print("The", f_enem.name, "deals", f_enem.dmg,
                  "damage to the", str(f_char.name) + "!")
            print("The", str(f_char.name) + "'s", "current HP:", f_char.hp)

        elif p == e:
            print("Both fighers clash and knock each other back!")

    elif a == "attack" and b == "defend":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        if f_char.dmg > f_enem.defe:
            dmg = f_char.dmg - f_enem.defe
            f_enem.hp -= dmg
            print("The", f_char.name, "attacks and breaks through the",
                  f_enem.name + "s defense!")
            print("The", str(f_enem.name) + "'s", "current HP:", f_enem.hp)

        elif f_char.dmg < f_enem.defe:
            f_enem.defe -= 100
            print("The", f_enem.name, "defends itself against the attack!")
            print("The", f_enem.name + "'s current defense:", f_enem.defe)

    elif a == "attack" and b == "dodge":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        if f_char.dmg > e_nim:
            f_enem.hp -= f_char.dmg
            print("The", f_enem.name,
                  "tried to evade but got caught in the attack!")
            print("The", f_enem.name, "takes", f_char.dmg, "damage!")
            print("The", str(f_enem.name) + "'s", "current HP:", f_enem.hp)

        elif f_char.dmg < f_enem.nim:
            print("The", f_enem.name, "dodged the attack!")
            f_enem.nim -= 100
            print("The", f_enem.name + "'s current nimble:", f_enem.nim)

    elif a == "defend" and b == "attack":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        if f_char.defe < f_enem.dmg:
            dmg = f_enem.dmg - f_char.defe
            f_char.hp -= dmg
            print("The", f_enem.name, "attacks and breaks through the",
                  f_char.name + "s defense!")
            print("The", str(f_char.name) + "'s", "current HP:", f_char.hp)

        elif f_char.defe > f_enem.dmg:
            f_char.defe -= 100
            print("The", f_char.name, "defends itself against the attack!")
            print("The", f_char.name + "'s current defense:", f_char.defe)

    elif a == "defend" and b == "defend":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        print(f_char.name, "prepares for an attack and Defends!")
        print(f_enem.name, "puts up a shield and Defends!")

    elif a == "defend" and b == "dodge":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        print(
            f_char.name, "uses Defend!")
        print(f_enem.name, "jumps back and Dodges!")

    elif a == "dodge" and b == "attack":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        if f_char.nim > f_enem.dmg:
            print("The", f_char.name, "dodged the attack!")
            f_char.nim -= 100
            print("The", f_char.name + "'s current nimble:", f_char.nim)

        elif f_char.nim < f_enem.dmg:
            f_char.hp -= f_enem.dmg
            print("The", f_char.name,
                  "tried to evade but got caught in the attack!")
            print("The", f_char.name, "takes", f_enem.dmg, "damage!")
            print("The", str(f_char.name) + "'s", "current HP:", f_char.hp)

    elif a == "dodge" and b == "defend":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        print(f_char.name, "sees the enemy's attack and Dodges!")
        print(f_enem.name, "pulls up their shield and Defends!")

    elif a == "dodge" and b == "dodge":
        print("The", f_char.name, "chose", a,
              "===", "The", f_enem.name, "chose", b)
        print(
            "Witnessing the determination of one another...\nBoth leap backwards out of pure instinct...")

    elif a == "flee":
        a = random.randint(1, 1000000)
        if a == 112702:
            print("A 1 in One-Millionth chance has occured!")
            print("A meteor from the sky has struck the",
                  f_enem.name, "instantly dealing a fatal blow!")
            f_enem.hp == 0
            print("The", f_char.name, "Wins!")

        else:
            print("The", f_enem.name, "has stop you in your tracks and attacks!")
            dmg = f_enem.dmg
            f_char.hp -= dmg
            print("The", f_enem.name, "deals", dmg,
                  "to the", str(f_char.name) + "!")
            print("The", str(f_char.name) + "'s", "current HP:", f_char.hp)


""" 
Notes: 
✔️ Player is able to choose a character and roll for their stats, along with added-on
        bonuses that each class possess.
✔️ Class dictionary is complete.
✔️ Enemy dictionary is complete (along with base stats that add to rolled values).
✔️ First Encounter
✔️ Fighting Algorithm
"""
