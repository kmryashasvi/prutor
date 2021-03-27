# A program in python to find a given number is Amstrong number or not

# Taking input
num = input()

cube_sum = 0

# Iterating through every digit of the given input and calculating sum of cubes after converting them into integer
for n in num:
    cube_sum += int(n)**3
    
# Printing result after comparing sum of cubes and the input
if cube_sum == int(num):
    print("Sum of Cubes is {}. It is the same as the number {}.".format(cube_sum,num))
else:
    print("Sum of Cubes is {}. It is NOT same as the number {}.".format(cube_sum,num))
    
