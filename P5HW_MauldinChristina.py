# Christina Mauldin

# 11/21/2024

#P5HW

# Creatting a text based game using functions

import random

# Creathing character functions
def create_character():
    print()
    print("---- 🦸Create a new character 🦹----")
    print()
    name = input("What is your character's name? ")
    role = input(" Is this gonna be a Hero or a Villain? ")
    health = random.randint(50,100)
    attack_points = random.randint(10,20)
    special_power = input("What are their special powers? ")
    print()

    character = {
        "Name": name,
        "Role": role.title(),
        "Health": health,
        "Attack Points": attack_points,
        "Special Power": special_power,
        }
    print(f"{name} has been creacted!!")
    print()
    return character

# Displaying character list with a function
def display_character(character_list):
    print("📜 List of all characters 📜")
    print()
    if not character_list:
        print("Who is that?? try again!")
        return
    for index, character in enumerate(character_list, 1):
        print()
        print(f"Superhero/villain {index}:")
        for key, value in  character.items():
            print(f" {key}: {value}")


# Creating the battle
def battle(attacker, defender):
    print(f"\n⚔️ Battle Time!!⚔️")
    print()
    print(f"{attacker['Name']} attacks {defender['Name']}!")
    print()
    damage = random.randint(5, attacker["Attack Points"])
    defender["Health"] -= damage
    print(f"{attacker['Name']} dealt {damage} damage to {defender['Name']}!")
    print()
    print(f"{defender['Name']}'s health is now {defender['Health']}")
    if defender["Health"] <= 0:
        print(f"💀{defender['Name']} has been defeated!💀")
        return True
    return False

# Create the main function
def main():
    characters = []
    while True:
        print()
        print("----✩Superhero vs Villain Game✩----")
        print()
        print("1. Create a character")
        print("2. Display all character")
        print("3. Battle characters")
        print("4. End the game")
        print()
        choice = input("Choose a option: ")
        print()

        if choice == "1":
            characters.append(create_character())
        elif choice == "2":
            display_character(characters)
        elif choice == "3":
            if len(characters) < 2:
                print("You need two characters to battle!")
                continue
            print("-----⚔Choose characters to battle⚔-----")
            print()
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char['Name']} ({char['Role']})")

            try:
                print()
                attacker_index = int(input("Choose the attacker: ")) - 1
                defender_index = int(input("Choose the defender: ")) - 1

                if attacker_index == defender_index:
                    print("You can't fight yourself. try again!")
                    continue

                attacker = characters[attacker_index]
                defender = characters[defender_index]
                if battle(attacker, defender):
                    characters.pop(defender_index)
            except (IndexError, ValueError):
                print("Invalid input, try again.")
        elif choice == "4":
            print("Thank you for playing, Goodbye!!👋")
            break
        else:
            print("Invalid choice. Please select again.")


# Call the main function
if __name__ == "__main__":
    main()
