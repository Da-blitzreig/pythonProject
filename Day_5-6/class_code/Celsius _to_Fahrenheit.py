def c_to_f_converter():
    print("Welcome to the Celsius to Fahrenheit converter!")
    celsius = int(input("Give me the Celsius:"))
    calculation = (celsius * 9/5) + 32
    print("The temperature in Fahrenheit is " + str(calculation))
c_to_f_converter()
