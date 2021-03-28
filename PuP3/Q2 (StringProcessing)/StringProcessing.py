# A program to print number of strings in a provided list satisfying given conditions


# Getting user input as a list
lis = list(map(str, input().split(',')))

# Declaring a counter variable to calculate number of strings
count = 0

# Iterating through every string
for s in lis:
    # Checking given conditions in the strings
    if (len(s) > 1) and (s[0] == s[-1]):
        count += 1      # Updating counter if satisfied
        
# Printing the number of appropriate strings found
print(count)
