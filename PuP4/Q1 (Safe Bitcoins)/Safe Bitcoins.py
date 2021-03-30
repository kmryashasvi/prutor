# Defining a function which returns True for a Prime Number
def isPrime(n):
    num = n
    if num <= 1:
        return False
    if num == 2:
        return True
    count = 0
    while num !=0:
        if count == 2:
            return False
        if n % num == 0:
            count += 1
        num -= 1
    return True

# Taking comma separated values as a list
lis = list(map(str, input().split(',')))

# Spaces are neglected automatically after casting values to int
a = int(lis[0])
b = int(lis[1])
x = int(lis[0][::-1])
y = int(lis[1][::-1])

# Counting how many of x and y are prime
primeCount = 0
for s in x,y:
    if isPrime(s):
        primeCount += 1

# Printing result
if primeCount == 2:
    print(x+y)
elif primeCount == 1:
    print(a + b)
else:
    print(a * b)
