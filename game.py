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


def describe_area():
    print("""
You find yourself in a dark forest...
You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Try to enter the cave.
    4. Type i to view your inventory.
    5. Quit
""")


def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")


def show_inventory(player):
    if len(player.inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Inventory:", ", ".join(player.inventory))


def main():
    player = welcome_player()
    describe_area()

    while True:
        choice = input("What will you do (1, 2, 3, 4, or 5): ")

        if choice == "1":
            print(f"{player.name}, you step into the dark woods.")
            if not player.has_lantern:
                add_to_inventory(player, "lantern")
                player.has_lantern = True
            else:
                print("You already picked up the lantern here.")

        elif choice == "2":
            print(f"{player.name}, you walk toward the mountain pass.")
            if not player.has_map:
                add_to_inventory(player, "map")
                player.has_map = True
            else:
                print("You already picked up the map here.")

        elif choice == "3":
            if player.has_lantern:
                print("You enter the cave because you have the lantern.")
            else:
                print("It is too dark to continue without a lantern.")

        elif choice == "4" or choice.lower() == "i":
            show_inventory(player)

        elif choice == "5":
            print("Thanks for playing.")
            break

        else:
            print("Invalid choice. Try again.")


main()