# Taking input s and k
s = input()
k = int(input())

# Declaring strings s1 and s2
s1 = ""
s2 = ""

# Associating values of s1 ans s2 from s 
while len(s)>0:
    s1 += s[0:k]
    s = s[k:]
    s2 += s[0:k]
    s = s[k:]
    
# Making a tuple to be printed in desired format
a = (s1,s2)
# Printing result
print(a)
