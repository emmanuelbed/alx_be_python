# Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

user_temp = input("Enter the temperature to convert: ")

try:
    temperature = float(user_temp)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

conv_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32


if conv_type ==  "C":
    value = convert_to_fahrenheit(user_temp)
    print(user_temp,"°C is", value,"°F")
elif conv_type == "F":
    value = convert_to_celsius(user_temp)
    print(user_temp, "°F is", value, "°C")                                                                                                                                                                                                                                                                   
else:
    print("Sorry, you entered an invalid Type")

