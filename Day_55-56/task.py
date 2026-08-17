import random
number = random.randint(1, 6)
a = int(input("pick a number for the die: "))

if a < number:
    print("wrong")
elif a > number:
    print("wrong")
else:
    print("correct")
6
