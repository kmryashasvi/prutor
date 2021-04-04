# File I-O - Read
## LAB5
## PROBLEM STATEMENT
This program will read a few files, process them, and answer queries as described next.<br>
The first line of input is a string. This will be used to name the TWO  files that you have to read. If the input is, say uvwx, the two files to be read are uwwxA.txt and uvwxB.txt. 
<br>
The code for the same could be:<br>

```
roll=input()
fileA=roll + 'A.txt'
fileB=roll + 'B.txt'
```
<br>
The next line will contain a string. You have to answer where this string is found, in fileA and/or in fileB or nowhere. NOTE: You need to take care of newlines in the files. They are to be ignored. 
<br>

### Example:
Suppose, we have two files having contents as shown below

```
x123A.txt:   
1
2
3
x123B.txt
def
str
3
baster

INPUT:
x123
1
OUTPUT:
Item 1 found in x123A.txt

NPUT:
x123
str
OUTPUT:
Item str found in x123B.txt

INPUT:
x123
hello
OUTPUT:
Item hello found nowhere

INPUT:
x123
3
OUTPUT:
Item 3 found in both x123A.txt and x123B.txt
```

