#prompt the user for an input and store them in a variable
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number")) 

#ask the operation
operant = input("Choose the operation (+, -, *, /):.")

# perform the calculations using the operant
match operant:
    case '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case '-':
        result = num1 - num2
        print(f'The result is {result}.')
    case '*':
        result = num1 * num2
        print(f'The result is {result}.')
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f'The result is {result}.')
        else:
            print("Cannot divide by zero.")   
    case _ :
        print("Invalid operant. Please choose from +, -, *, /. ")         
            