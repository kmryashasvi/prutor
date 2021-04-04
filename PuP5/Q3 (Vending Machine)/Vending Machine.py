
def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e: 
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x
        
## Code to read __VendingItems__.csv

A = open('__VendingItems__.csv')
C = A.read().split('\n')
C = C[:-1]
D = []
for i in C:
    D.append(i[:-3])

dic = {}
for j in C:
    dic[j[:-3]]=int(j[-2:])

## Enforce the constraints using Exception Handling
def inp():
    try:
        y = input()
        return dic[y]
    except Exception as e:
        print("Available Items are {}.\nTry Again.".format(D))
        return inp()
## Code to read user inputs
cost = inp()
q = read_int()

## Act once the inputs are OK.
if cost > q:
    print("Sorry, can not buy item. Not enough money")
else:
    print("Thank you for your purchase. Enjoy")

if cost < q:
    print("Do not forget to collect your change, {} Rs.".format(q-cost))


