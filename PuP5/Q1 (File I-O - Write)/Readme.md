This program is about the "```eval```" function, and writing to files. The program will read a few lines of input, process it, and create files as described next.
The first line of input is a string. This will be used to name the TWO  files that you have to create. If the input is, say ```uvwx```, the two files to be created are ```uwwxA.txt``` and ```uvwxB.txt```. 
<br>

The code for the same could be:<br>

```
roll=input()
fileA=roll + 'A.txt'
fileB=roll + 'B.txt'
```

The next two lines will contain items that need to be evaluated as python lists, using "eval function. For example, if one line of the input is: 
[1+2, "Hi"+"There"]
you should be able to evaluate it as a list [3, "HiThere"].

The two lines will contain the same number of elements.
Your task is to write the elements of the the two lists in the two files, fileA and fileB, respectively. There should be NEWLINE (```\n```) printed in the file to separate the list items.

Finally, use the following code will print the two files on the output:

```
A, B = open(fileA, 'r'), open(fileB, 'r')
print (A.read())
print (B.read())
A.close()
B.close()
```

### Example:
INPUT:<br>
x123<br>
[1, 1+2, "def_" + "abc"]<br>
["int", "float", "str"]<br>
<br>
<br>
OUTPUT:<br>
1<br>
3<br>
def_abc<br>
<br>
int<br>
float<br>
str<br>
<br>
<br>
(The two files created will be x123A.txt and x123B.txt in this case).
