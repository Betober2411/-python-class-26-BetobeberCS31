#=============================================================================
# Course: CS-31 Python Programming
# Project: Random Character Generator + Battle Simulator
# Student: Carlos Farias
# Date 11/22/2026
#============================================================================ 

"""
Random Character Generator + Battle Simulator
----------------------------------------------
Part 1: Generate a fantasy RPG character with random traits.
Part 2: Battle the character against a randomly generated enemy.

Built of the Program, step by step:
  Step 1 - Imports, banner, and the yes/no helper
  Step 2 - Lists of names, races, and classes
  Step 3 - Random race/class selection with a random number + if/elif/else
  Step 4 - Random trait (stat) generation
  Step 5 - Character sheet display
  Step 6 - Battle loop with damage and random healing
  Step 7 - "Fight again?" and "New characters?" loops
"""
import random

# Step 1: the random module is required for everything below

# ---------------------------------------------------------------------------
# Step 2: Lists of possible options
# ---------------------------------------------------------------------------
RACES = ["Human", "Elf", "Dwarf", "Half-Orc", "Halfling"]
CLASSES = ["Warrior", "Wizard", "Rogue", "Cleric", "Ranger"]
ENEMY_NAMES = ["Grimlock", "Zephyra", "Bor the Brute", "Nyx", "Thornwick",
               "Vexa the Cruel", "Durnok", "Selene Darkmoon"]

# The traits every character has (stat name -> (min, max) random range)
TRAITS = {
    "Strength": (3, 18),
    "Wisdom": (3, 18),
    "Dexterity": (3, 18),
    "Charisma": (3, 18),
    "Constitution": (3, 18),
}

# ---------------------------------------------------------------------------
# Helper function (accepts a parameter): keeps asking until the answer is y/n
# ---------------------------------------------------------------------------
def ask_yes_no(question):
    """Ask a yes/no question and return True for 'y', False for 'n'."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Please type 'y' or 'n'.")

# ---------------------------------------------------------------------------
# Step 3: Use a random number + conditionals to choose race and class
# ---------------------------------------------------------------------------
def pick_race_and_class():
    """Roll a die (1-100) to choose a race, then pick a class from the list."""
    roll = random.randint(1, 100)

    if roll <= 30:
        race = "Human"        # 30% chance
    elif roll <= 50:
        race = "Elf"          # 20% chance
    elif roll <= 70:
        race = "Dwarf"        # 20% chance
    elif roll <= 85:
        race = "Half-Orc"     # 15% chance
    else:
        race = "Halfling"     # 15% chance

    char_class = random.choice(CLASSES)  # random.choice picks a random list item
    return race, char_class

# ---------------------------------------------------------------------------
# Step 4: Build a character (a dictionary of random traits)
# ---------------------------------------------------------------------------
def create_character(name):
    """Return a dictionary holding the character's name, race, class, and stats."""
    race, char_class = pick_race_and_class()

    character = {
        "name": name,
        "race": race,
        "class": char_class,
    }

    # Assign a random value to each trait
    for trait, (low, high) in TRAITS.items():
        character[trait] = random.randint(low, high)

    # Hit points: base 20 plus a random bonus, boosted by Constitution
    character["HP"] = random.randint(20, 40) + character["Constitution"]
    character["max_hp"] = character["HP"]  # remember starting HP for rematches
    return character

# ---------------------------------------------------------------------------
# Step 5: Display the character sheet
# ---------------------------------------------------------------------------
def display_character(character, title="Character Sheet"):
    """Print the character's info in an easy-to-read format."""
    print(f"\n~*~*~ {title} ~*~*~")
    print(f"Name:          {character['name']}")
    print(f"Race:          {character['race']}")
    print(f"Class:         {character['class']}")
    print(f"HP:            {character['HP']}")
    for trait in TRAITS:
        print(f"{trait + ':':<15}{character[trait]}")
    print("=" * 25)

# ---------------------------------------------------------------------------
# Step 6: Battle simulator
# ---------------------------------------------------------------------------
def attack(attacker, defender):
    """One attack: damage is based on Strength, with a bonus for high Dexterity."""
    damage = random.randint(1, 10) + attacker["Strength"] // 2
    # Dexterity gives a chance of a critical hit (double damage)
    if random.randint(1, 20) <= attacker["Dexterity"] // 4:
        damage *= 2
        print(f"  CRITICAL HIT! {attacker['name']} strikes hard!")
    defender["HP"] -= damage
    print(f"  {attacker['name']} hits {defender['name']} for {damage} damage.")

def maybe_heal(character):
    """25% chance to heal a bit, based on Wisdom."""
    if random.randint(1, 100) <= 25:
        heal = random.randint(1, 6) + character["Wisdom"] // 3
        character["HP"] = min(character["HP"] + heal, character["max_hp"])
        print(f"  {character['name']} heals {heal} HP!")

def battle(player, enemy):
    """Loop rounds until one (or both) fighters reach 0 HP or less."""
    round_number = 1
    while player["HP"] > 0 and enemy["HP"] > 0:
        print("\n*****************************")
        print(f"        BATTLE - Round {round_number}")
        print("*****************************")
        print(f"You:   {player['name']} ({player['race']} {player['class']}) HP: {player['HP']}")
        print(f"Enemy: {enemy['name']} ({enemy['race']} {enemy['class']}) HP: {enemy['HP']}\n")

        # Both fighters attack each round
        attack(player, enemy)
        attack(enemy, player)

        # Only living fighters get a chance to heal
        if player["HP"] > 0:
            maybe_heal(player)
        if enemy["HP"] > 0:
            maybe_heal(enemy)

        round_number += 1

    # Declare the winner
    print("\n*****************************")
    if player["HP"] <= 0 and enemy["HP"] <= 0:
        print("Tie! Both knocked out.")
    elif enemy["HP"] <= 0:
        print(f"{player['name']} wins the battle!")
    else:
        print(f"{enemy['name']} wins the battle. Better luck next time!")
    print(f"Your remaining HP:  {player['HP']}")
    print(f"Enemy remaining HP: {enemy['HP']}")
    print("*****************************")

# ---------------------------------------------------------------------------
# Step 7: Main program flow
# ---------------------------------------------------------------------------
def main():
    print("~~~~~*~~~*~~~~~*~~~*~~~~~*~~~*")
    print("|Random Character Generator! |")
    print("~~~~~*~~~*~~~~~*~~~*~~~~~*~~~*\n")

    play_again = True
    while play_again:
        if ask_yes_no("Would you like to generate a character?"):
            # Ask for a name, or provide one if the user leaves it blank
            name = input("What name would you like to use for your character? "
                         "(press Enter for a random one): ").strip()
            if name == "":
                name = random.choice(ENEMY_NAMES)
                print(f"Your character will be called {name}.")

            player = create_character(name)
            display_character(player)

            # Offer a battle
            if ask_yes_no("\nWould you like to battle another character?"):
                fighting = True
                while fighting:
                    # Reset player HP so rematches start fresh
                    player["HP"] = player["max_hp"]
                    enemy = create_character(random.choice(ENEMY_NAMES))
                    print("\nA challenger appears!")
                    display_character(enemy, title="Enemy Sheet")
                    battle(player, enemy)
                    fighting = ask_yes_no("\nWould you like to fight again?")
            else:
                print("No battle today. Maybe next time!")

            # Ask about a whole new set of characters
            play_again = ask_yes_no("\nWould you like to generate a new set of characters?")
        else:
            play_again = False

    print("\nThanks for playing!")

# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()