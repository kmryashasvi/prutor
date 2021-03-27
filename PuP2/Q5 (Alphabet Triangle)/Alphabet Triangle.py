# A program in python to print staircase of alphabets of given height

# Getting height from user
height = int(input())

for i in range(height):              # Printing rows

    print("_",end="")                # Printing '_' at the begining of a row
    
    for j in range(i+1):             # Printing elements of rows
    
        print(chr(65+j),end="_")     # chr(<ascii serial number>) returns ascii characters
                                         # A is at 65th position in ascii chart
                                         
    print()                          # Printing a new line after every row is printed
    
