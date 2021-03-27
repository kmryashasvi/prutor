# A program in python to print staircases of given height

# Taking user input (height of the pattern)
height = int(input())

# Checking if the input is valid
if height <= 0:
    print("Please enter an integer greater than zero (0)")
else:
    for i in range(height):            # Printing rows
        for j in range(i+1):           # Printing elements in a row
            print("*",end='')
        print()                        # Priting new-line at the end of every row
        
