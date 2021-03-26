# A program in python to find a given string is palindrome or not.

# Approach: 1.Break the string into two parts.2.Reverse one part.3.Compare both parts after converting them to upper case.

# Getting user input (a string)
string = input()
leng = len(string)

# Determining breakpoint
n1=int(leng/2)
n2=int((leng+1)/2)

# Breaking String into two parts
if leng % 2 == 0:             # If length of given string is even
    string1=string[0:n1+1]
    string2=string[n1::]
else:                         # If length of given string is odd
    string1 = string[0:n2-1]
    string2=string[n2::]
    
string2=string2[::-1]  # Reversing the second part

# Converting both parts into upper case and comparing them 
if string1.upper()==string2.upper():
    print('{} is a palindrome.'.format(string))
else:
    print(string,'is NOT a palindrome.')
    
