class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False


def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return Player(name)


def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up {item}.")


def show_inventory(player):
    if len(player.inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Inventory:", ", ".join(player.inventory))


def explore_dark_woods(player):
    print(f"\n{player.name}, you walk into the dark woods.")
    if not player.has_lantern:
        print("You find a lantern under a tree.")
        player.has_lantern = True
        add_to_inventory(player, "lantern")
    else:
        print("You already found the lantern here.")


def explore_mountain_pass(player):
    print(f"\n{player.name}, you head toward the mountain pass.")
    if not player.has_map:
        print("You find a map near the rocks.")
        player.has_map = True
        add_to_inventory(player, "map")
    else:
        print("You already found the map here.")


def explore_cave(player):
    print(f"\n{player.name}, you try to explore the cave.")
    if player.has_lantern:
        print("You use the lantern to see inside the cave.")
        if "treasure" not in player.inventory:
            add_to_inventory(player, "treasure")
            print("You found treasure in the cave.")
        else:
            print("You already found the treasure here.")
    else:
        print("It is too dark to enter the cave without a lantern.")


def explore_hidden_valley(player):
    print(f"\n{player.name}, you search for the hidden valley.")
    if player.has_map:
        print("You use the map to find the hidden valley.")
        if "rare herbs" not in player.inventory:
            add_to_inventory(player, "rare herbs")
            print("You found rare herbs in the valley.")
        else:
            print("You already found the rare herbs here.")
    else:
        print("You cannot find the hidden valley without a map.")


def main():
    player = welcome_player()

    while True:
        print("\nChoose an action:")
        print("1. Explore dark woods")
        print("2. Explore mountain pass")
        print("3. Explore cave")
        print("4. Explore hidden valley")
        print("5. Show inventory")
        print("6. Quit")

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
            show_inventory(player)
        elif choice == "6":
            print("Thanks for playing.")
            break
        else:
            print("Invalid choice. Try again.")


main()