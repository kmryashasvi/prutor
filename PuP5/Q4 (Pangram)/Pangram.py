# Taking user input in lower case
ans = input().lower()

# Creating a list of length 26 to calculate frequency of alphabets
lis = []
for i in range(26):
    lis.append(0)
alp = "abcdefghijklmnopqrstuvwxyz"

# Calculating frequencies of all alphabets
for i in ans:
    if i in alp:
        lis[ord(i)-97] += 1
        
# Listing the alphabets which doesn't occur
remlis = ""
for i in range(26):
    if lis[i]==0:
        remlis += " "+ chr(97+i) + ","

# Printing result
if 0 not in lis:
    print("Yes, the string is a pangram.")
else:
    remlis = remlis[:-1]+"."
    print("No, the string is NOT a pangram. Missing letter(s) is(are)"+ remlis)
