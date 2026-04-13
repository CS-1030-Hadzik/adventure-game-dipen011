class Player:
    def __init__(self):
        self.inventory = []
        self.has_lantern = False
        self.has_map = False

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"You picked up {item}.")


def find_lantern(player):
    if player.has_lantern:
        print("You already have the lantern.")
    else:
        print("You found a lantern in the dark woods.")
        player.has_lantern = True
        player.add_item("lantern")


def find_map(player):
    if player.has_map:
        print("You already have the map.")
    else:
        print("You found a map near the mountain pass.")
        player.has_map = True
        player.add_item("map")


def explore_cave(player):
    if player.has_lantern:
        print("You use the lantern to explore the cave.")
        if "treasure" not in player.inventory:
            player.add_item("treasure")
            print("You found treasure in the cave.")
        else:
            print("You already found the treasure here.")
    else:
        print("It is too dark to explore the cave without a lantern.")


def explore_hidden_valley(player):
    if player.has_map:
        print("You use the map to find the hidden valley.")
        if "rare herbs" not in player.inventory:
            player.add_item("rare herbs")
            print("You found rare herbs in the valley.")
        else:
            print("You already found the rare herbs here.")
    else:
        print("You cannot find the hidden valley without a map.")


def show_inventory(player):
    if len(player.inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Inventory:", ", ".join(player.inventory))


def main():
    player = Player()

    print("Welcome to the Adventure Game.")

    while True:
        print("\nChoose an action:")
        print("1. Explore dark woods")
        print("2. Explore mountain pass")
        print("3. Explore a nearby cave")
        print("4. Search for a hidden valley")
        print("5. Show inventory")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            find_lantern(player)
        elif choice == "2":
            find_map(player)
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