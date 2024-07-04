# the function that performs all the operation

def perform_operation(num1, num2, operation):
    #use if and elif to do the arithmetics.
    if operation == "add":
        add = num1 + num2
        return add
    elif operation == "subtract":
        subtract = num1 - num2
        return subtract
    elif operation == "multiply":
        multiply = num1 * num2
        return multiply
    elif operation == "divide":
        if num2 == 0:
            print("Error: number cannot be divided by 0")
        else:
            divide = num1 / num2
            return divide
    else:
        print("Invalid Operation Selected")

        