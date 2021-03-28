# A program in python to print a list by multiplying every element of a given list by 2

# Taking user input as a list
lis = list(map(int, input().split(',')))

# Multiplying every element in the list by 2 by iterating through every element
for i in range(len(lis)):
    lis[i] *= 2
    
# Printing the final list
print(lis)
