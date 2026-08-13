import random

names = []

while True:
    name = input("Give me a name: ")
    names.append(name)

    if len(names) >= 2:
        choice = input("Type 1 for a random name, or press Enter to give me another name: ")

        if choice == "1":
            print("Random name:", random.choice(names))
            break