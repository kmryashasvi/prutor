# Getting space separated rows of matrix as a list
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

# Iterating through the elements of the matrix and doing required changes
for i in range(2):
    if l1[i]%2 == 0:
        l1[i]*=2
    else:
        l1[i]=0
    if l2[i]%2 == 0:
        l2[i]*=2
    else:
        l2[i]=0
        
# Printing in desired format
print(l1[0],l1[1],sep="#")
print(l2[0],l2[1],sep="#")

