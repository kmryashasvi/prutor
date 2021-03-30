A = int(input())  
B = int(input())
P = []
Q = []
R = []

for j in range(0, B):
    abc = []
    x = input()
    y = x.split(',')
    abc.append(int(y[0]))
    abc.append(int(y[1]))
    Q.append(abc)
k = int(input()) 
   
if k >= A:
    print("ERROR: Invalid Node.")
    
else:
    for a in Q:
        if a[1] == k:
            R.append(a[0])
    
R.sort()  
pro = []  
for b in R:
    if b not in pro:
        pro.append(b)
print(*pro,sep=",")
