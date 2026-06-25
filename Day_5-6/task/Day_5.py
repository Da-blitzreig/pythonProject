import random


print("Welcome to the random number generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_numbers = input("How much numbers do you want?")
nr_letters = input("How much letters do you want?")
nr_symbols = input("How much symbols do you want?")

if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
  print("Invalid value, enter a number instead.")
else:
  password = []

  random_letter = random.randint(0, 51)
  for i in range(0, int(nr_letters)):
    random_letter = random.randint(0, 51)
    password.append(letters[random_letter])

  random_number = random.randint(0,9)
  for i in range(0, int(nr_numbers)):
    random_number = random.randint(0,9)
    password.append(numbers[random_number])

  random_symbol = random.randint(0,8)
  for i in range(0, int(nr_symbols)):
    random_symbol = random.randint(0,8)
    password.append(symbols[random_symbol])

  random.shuffle(password)
  print(f"Here is your password: {''.join(password)}")