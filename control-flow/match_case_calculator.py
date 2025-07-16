# Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

inputs = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero."
            print(result)
            exit()
        else:
            result = num1 / num2

print("The result is", result)
