#collect and store the user input in a variable called number
number = int(input("Enter a number to see its multiplication table:"))

# use a for loop to iterate the numbers from 1-0

for x in range(1,10):
    print(f"{number} * {x} = {number * x}")