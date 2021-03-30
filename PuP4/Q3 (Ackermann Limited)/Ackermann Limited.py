# Defining a function to calculate ackermann,
# Including globals to find base case of the recursion
def acker(a,b):
    global numCalls,T
    if numCalls == T:
        return
    numCalls += 1
    if a == 0:
        return b + 1
    elif b == 0:
        return acker(a - 1,1)
    elif a > 0 and b > 0:
        return acker(a - 1, acker(a, b - 1))
    else:
        return
    
# Taking input as a list in int
lis = list(map(int,input().split(',')))
m = lis[0]
n = lis[1]
T = lis[2]

numCalls = 0
# Calling the recursive ackermann function
result = acker(m,n)

# Printing result in desired format
if numCalls < T:
    print("Result = {} in {} calls".format(result,numCalls))
else:
    print("Aborted")
