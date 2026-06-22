import random

print("Hello! Welcome to the number guessing game!")

L = 10
ss = random.randint(1, 10)

while True:
    guess = int(input("Guess the number from 1 to 10: "))

    if guess < ss:
        print("Too low!")
    elif guess > ss:
        print("Too high!")
    else:
        print("Correct! You win!")
        break
    if guess == 10:
        print ("sorry, you lost!")
        break
