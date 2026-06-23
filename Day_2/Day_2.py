print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?"))
tip = int(input("How much tip do you give?"))
people = int(input("How much people will split the bill?"))
total = total_bill + tip
equal_amount_of_money = total / people
print("Each person will pay " + str(equal_amount_of_money) )