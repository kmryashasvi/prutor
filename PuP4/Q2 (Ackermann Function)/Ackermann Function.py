# Defining a function to calculate ackermann function
def acker(m,n):
    if m >= 0 and n >= 0:
        if m == 0:
            return n + 1
        elif n == 0:
            return acker(m - 1,1)
        else:
            return acker(m - 1, acker(m, n - 1))

# Converting input into int automatically removes whitespaces
# Taking input as a list of int
lis = list(map(int,input().split(',')))

# Printing result
print(acker(lis[0], lis[1]))
