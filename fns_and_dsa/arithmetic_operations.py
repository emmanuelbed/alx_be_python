# Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

def perform_operation(num1, num2, operation):
    num1 = int(num1), num2 = int(num2)

    if operation == "divide" and num2 == 0:
        print("Division by zero not possible") 
        exit()
    else:
        # match operation:
        #     case "add":
        #         result = int(num1) + int(num2)
        #     case "subtract":
        #         result = int(num1) - int(num2)
        #     case "multiply":
        #         result = int(num1) * int(num2)
        #     case "divide":
        #         result = int(num1) / int(num2)
        if operation == "add":
            result = num1 + num2
        elif operation =="subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2

    return result

