#######################################
# Do Not Change
roll=input()
fileA=roll + 'A.txt'
fileB=roll + 'B.txt'
########################################


########################################
# Your code goes here
x = eval(input())
y = eval(input())
########################################


########################################
# Do Not Change
A, B = open(fileA, 'r'), open(fileB, 'r')
print (A.read())
print (B.read())
A.close()
B.close()
########################################
