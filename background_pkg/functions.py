
import time
import random


def loading():
    for progress in range(0, 101, 1):
        loading_bar = " " + "█" * (progress // 2) + " " * \
            (50 - (progress // 2)) + " "
        loading_string = "Loading..."
        loading_display = loading_string + loading_bar
        print(loading_display, end='\r')
        time.sleep(0.1)
    print("\nWelcome to")
    print("██████   ███████      ████       ███████                ████     ")
    print("██   ██  ██    ██   ██    ██       ███                ██    ██   ")
    print("██████   ██████    ██      ██      ███    ██████     ██      ██  ")
    print("██       ██   ██    ██    ██   ██  ███                ██    ██   ")
    print("██       ██    ██     ████      █████                   ████   \n")


def enemies(enemy):
    enemies_data = {
        "goblin": {"name": "Goblin", "Health": 100, "Damage": 150, "Nimble": 400, "Defense": 100},
        "troll": {"name": "Troll", "Health": 1000, "Damage": 400, "Nimble": 50, "Defense": 500},
        "dragon": {"name": "Dragon", "Health": 1500, "Damage": 1000, "Nimble": 800, "Defense": 700},
        "azazel": {"name": "Fallen Angel", "Health": 2000, "Damage": 1000, "Nimble": 1500, "Defense": 1500}
    }

    enemies = enemies_data.get(enemy.lower())

    if enemies:
        return enemies["name"], enemies["Health"], enemies["Damage"], enemies["Nimble"], enemies["Defense"]
    else:
        return None, None, None, None, None


def character(player):
    characters = {
        "warlock": {"name": "Warlock", "Health": 0, "Damage": 500, "Nimble": 0, "Defense": 0},
        "rogue": {"name": "Rogue", "Health": 0, "Damage": 0, "Nimble": 500, "Defense": 0},
        "brawler": {"name": "Brawler", "Health": 500, "Damage": 0, "Nimble": 0, "Defense": 0},
        "knight": {"name": "Knight", "Health": 0, "Damage": 250, "Nimble": 0, "Defense": 250}
    }

    characters = characters.get(player.lower())

    if characters:
        return characters["name"], characters["Health"], characters["Damage"], characters["Nimble"], characters["Defense"]
    else:
        return None, None, None, None, None


def roll_attributes():
    dice = random.randint(1, 20)
    attribute = dice * 100
    return attribute


def enemy_choice():
    action = ["attack", "defend", "dodge"]
    e_action = random.choice(action)
    return e_action
