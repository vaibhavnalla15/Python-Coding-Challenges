""" Create a Python program that converts temperature from Celsius to Fahrenheit or Fahrenheit to Celsius based on user choice. """

temperature_value = float(input("Enter a Temperature value:- "))
unit_type = input('Enter C for Celsius, F for Fahrenheit:- ').upper()

if unit_type == "C":
    converted_temp = (temperature_value * 9/5) + 32
    print(f"Converted Temperature is {converted_temp}F")
elif unit_type == "F":
    converted_temp = (temperature_value - 32) * 5/9
    print(f"Converted Temperature is {converted_temp}C")
else:
    print("Invalid unit. Use 'C' or 'F'.")

