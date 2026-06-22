import random

def roll_dice():
    sides = int(input("How many sides on the dice? "))
    result = random.randint(1, sides)
    print(f"You rolled: {result}")

roll_dice()
