import random

number = random.randint(1, 100)

while True:
    a = int(input("Welcome to the number guessing game! Pick a number: "))

    if a < number:
        print("too low")
    elif a > number:
        print("too high")
    else:
        print("correct!")
        break