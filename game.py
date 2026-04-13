inventory = []


def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return name


def describe_area():
    print("""
You find yourself in a dark forest...
You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
    Type 'i' to view your inventory.
""")


def add_to_inventory(item):
    inventory.append(item)
    print(f"You picked up a {item}!")


player_name = welcome_player()
describe_area()

while True:
    choice = input("What will you do (1, 2, 3, or i): ")

    if choice == "1":
        print(f"{player_name}, you step into the dark woods...")
        add_to_inventory("lantern")
    elif choice == "2":
        print(f"{player_name}, you head toward the mountain pass...")
        add_to_inventory("map")
    elif choice == "3":
        print(f"{player_name}, you stay where you are and wait.")
    elif choice == "i":
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:", ", ".join(inventory))
    else:
        print("Invalid choice. Try again.")