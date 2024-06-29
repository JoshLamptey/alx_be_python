# ask the user for input
pattern = int(input("Enter the size of the pattern:"))

#check to make sure its a positive integer
if pattern <= 0:
    print("Please enter a positive integer")
else:
    #set the row
    row = 0

# draw the pattern with the number
while row < pattern:
    for column in range(pattern):
        print("*", end="")

    print() # to  move to the next line

    #increase the row counter
    row += 1    