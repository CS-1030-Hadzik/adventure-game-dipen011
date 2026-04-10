"""
Adventure Game
Author: Dipendra Adhikari
Description: A text-based adventure game where the player explores different areas,
collects items, manages health, and tries to win by finding the treasure and rare herbs.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []


def show_status(player):
    print("\n----------------------------")
    print(f"Player: {player.name}")
    print(f"Health: {player.health}")
    print(f"Inventory: {player.inventory}")
    print("----------------------------")


def explore_dark_woods(player):
    print("\nYou walk into the dark woods.")
    print("The trees are tall and the air feels cold.")

    if "lantern" not in player.inventory:
        print("You found a lantern on the ground.")
        player.inventory.append("lantern")
    else:
        print("You already explored this area and found the lantern.")


def explore_mountain_pass(player):
    print("\nYou travel through the mountain pass.")
    print("The path is steep, but you keep moving forward.")

    if "map" not in player.inventory:
        print("You found an old map between the rocks.")
        player.inventory.append("map")
    else:
        print("You already explored this area and found the map.")


def explore_cave(player):
    print("\nYou enter the cave.")

    if "lantern" not in player.inventory:
        print("It is too dark to see anything.")
        print("You trip over a rock and lose 10 health.")
        player.health -= 10
    else:
        if "treasure" not in player.inventory:
            print("With the lantern, you can see deep inside the cave.")
            print("You found the treasure!")
            player.inventory.append("treasure")
        else:
            print("You already found the treasure here.")


def explore_hidden_valley(player):
    print("\nYou search for the hidden valley.")

    if "map" not in player.inventory:
        print("You do not know where to go without a map.")
        print("You get lost and lose 10 health.")
        player.health -= 10
    else:
        if "rare herbs" not in player.inventory:
            print("The map leads you safely to the hidden valley.")
            print("You found the rare herbs!")
            player.inventory.append("rare herbs")
        else:
            print("You already collected the rare herbs here.")


def stay_still(player):
    print("\nYou stay still and waste time.")
    print("The cold forest air drains your energy.")
    print("You lose 10 health.")
    player.health -= 10


def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\nYou found both the treasure and the rare herbs.")
        print(f"Congratulations, {player.name}! You won the game!")
        return True
    return False


def check_lose(player):
    if player.health <= 0:
        print(f"\n{player.name}, your health has reached 0.")
        print("You lost the game.")
        return True
    return False


def main():
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

    player_name = input("What is your name, adventurer? ")
    player = Player(player_name)

    print(f"\nWelcome, {player.name}! Your journey begins now.")

    starting_area = """
You find yourself in a dark forest.
The sound of leaves moving around you feels strange.
There are different places you can explore from here.
"""
    print(starting_area)

    while True:
        show_status(player)

        print("\nWhat would you like to do?")
        print("1. Explore the dark woods")
        print("2. Explore the mountain pass")
        print("3. Explore the cave")
        print("4. Explore the hidden valley")
        print("5. Stay still")
        print("6. Quit game")

        choice = input("Enter your choice: ")

        if choice == "1":
            explore_dark_woods(player)
        elif choice == "2":
            explore_mountain_pass(player)
        elif choice == "3":
            explore_cave(player)
        elif choice == "4":
            explore_hidden_valley(player)
        elif choice == "5":
            stay_still(player)
        elif choice == "6":
            print("\nThanks for playing!")
            break
        else:
            print("\nThat is not a valid choice. Try again.")
            continue

        if check_lose(player):
            break

        if check_win(player):
            break


main()