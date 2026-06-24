print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
first_options = input("You're at a cross road. Where do you want to go? Type left or right")
if first_options == "left":
    print("You've come to a lake there is an island in the middle of the lake")
    second_choice = input("Type wait to wait for a boat, type swim to swim to swim across")
    if second_choice == "wait":
        print("You've arrived at the island unharmed, there are 3 doors, one yellow, one blue, and one red.")
        third_choice = input("Only one has the treasure, choose carefully")
        if third_choice == "yellow":
            print("You found the treasure! You win!")
        elif third_choice == "blue":
            print("You enter a room with a serial killer. Game over")
        elif third_choice == "red":
            print("As you open the treasure, it wsa a decoy, lava falls on you. Game over.")
        else:
            print("Invalid choice")
    elif second_choice == "swim":
        print("A bunch of piranhas eat you alive. Game over")
    else:
        print("Invalid choice")
elif first_options == "right":
    print("you fell in a hole. Game over")
else:
    print("invalid choice.")