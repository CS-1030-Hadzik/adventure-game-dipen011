class Player:
    def __init__(self):
        self.inventory = []
        self.has_lantern = False
        self.has_map = False
        self.health = 100


def show_status(player):
    print("\n----------------------")
    print("Health:", player.health)

    if len(player.inventory) == 0:
        print("Inventory: empty")
    else:
        print("Inventory:", ", ".join(player.inventory))
    print("----------------------")


def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\nYou found both the treasure and the rare herbs.")
        print("You win the game!")
        return True
    return False


def check_lose(player):
    if player.health <= 0:
        print("\nYour health has reached 0.")
        print("You lost the game.")
        return True
    return False


def explore_dark_woods(player):
    print("\nYou walk into the dark woods.")

    if not player.has_lantern:
        print("You found a lantern under a tree.")
        player.has_lantern = True
        player.inventory.append("lantern")
    else:
        print("You already found the lantern here.")


def explore_mountain_pass(player):
    print("\nYou climb up the mountain pass.")

    if not player.has_map:
        print("You found a map near the rocks.")
        player.has_map = True
        player.inventory.append("map")
    else:
        print("You already found the map here.")


def explore_cave(player):
    print("\nYou try to explore the cave.")

    if player.has_lantern:
        if "treasure" not in player.inventory:
            print("You use the lantern to see inside the cave.")
            print("You found treasure.")
            player.inventory.append("treasure")
        else:
            print("You already found the treasure in the cave.")
    else:
        print("It is too dark to enter the cave without a lantern.")
        print("You lose 10 health.")
        player.health -= 10


def explore_hidden_valley(player):
    print("\nYou try to find the hidden valley.")

    if player.has_map:
        if "rare herbs" not in player.inventory:
            print("You use the map and find the hidden valley.")
            print("You found rare herbs.")
            player.inventory.append("rare herbs")
        else:
            print("You already found the rare herbs in the valley.")
    else:
        print("You cannot find the hidden valley without a map.")
        print("You lose 10 health.")
        player.health -= 10


def stay_still(player):
    print("\nYou stay still and do nothing.")
    print("You lose 10 health.")
    player.health -= 10


def main():
    player = Player()

    print("Welcome to the Adventure Game.")
    print("Your goal is to find the treasure and the rare herbs.")
    print("Be careful because losing health can end the game.")

    while True:
        show_status(player)

        print("\nWhat would you like to do?")
        print("1. Explore dark woods")
        print("2. Explore mountain pass")
        print("3. Explore cave")
        print("4. Explore hidden valley")
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
            print("\nThanks for playing.")
            break
        else:
            print("\nInvalid choice. Please try again.")
            continue

        if check_win(player):
            break

        if check_lose(player):
            break


main()