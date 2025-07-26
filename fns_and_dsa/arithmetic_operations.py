# Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

def perform_operation(num1, num2, operation):
    if operation == "divide" and num2 == 0:
        print("Division by zero not possible") 
        exit()
    else:
        match operation:
            case "add":
                result = int(num1) + int(num2)
            case "subtract":
                result = int(num1) - int(num2)
            case "multiply":
                result = int(num1) * int(num2)
            case "divide":
                result = int(num1) / int(num2)

    return result

