"""
Adventure Game
Author: Dipendra Adhikari
Description: Simple text-based game
"""

# Welcome message
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# Ask name
player_name = input("What is your name, adventurer? ")

# Concatenation
print("Welcome, " + player_name + "! Your journey begins now.")

# f-string
print(f"Welcome, {player_name}! Your journey begins now.")

# Starting area
starting_area = """
You find yourself in a dark forest.
The sound of leaves moving around you feels strange.
There is a small path in front of you...
"""
print(starting_area)

# Decision
decision = input("Do you want to take the path? (yes or no): ").lower()

# Response
if decision == "yes":
    print(f"{player_name}, you walk forward into the forest.")
elif decision == "no":
    print(player_name + ", you stay where you are.")
else:
    print("You are confused and do nothing.") 