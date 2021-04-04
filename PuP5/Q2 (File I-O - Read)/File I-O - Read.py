#######################################
## Do not Change
roll=input()
fileA=roll + 'A.txt'
fileB=roll + 'B.txt'
########################################
# Your code goes here
nam = input()

# Opening files in reading mode
a,b = open(fileA), open(fileB)
A = a.read()
B = b.read()

# Checking and printing result if the input exists in the files
if (nam in A) and (nam in B):
    print("Item {} found in both {} and {}".format(nam,fileA,fileB))
elif nam in A:
    print("Item {} found in {}".format(nam,fileA))
elif nam in B:
    print("Item {} found in {}".format(nam,fileB))
else:
    print("Item {} found nowhere".format(nam))
    
# Closing the files
a.close()
b.close()
