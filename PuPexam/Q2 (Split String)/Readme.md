# Split String
## PUP-EXAM
## PROBLEM STATEMENT
[15 Points]

Write a program that accepts a string ```S``` and a number '```k```'. The program splits ```S``` into two strings, ```S1``` and ```S2``` where ```S1``` has all ODD bunches of ```k``` characters from ```S```, and ```S2``` contains all EVEN bunches of k characters from ```S```. That is, given sufficiently long S, 
* ```S1``` contains characters at indices ```0``` to ```k-1```,followed by the characters at the indices ```2k``` to ```3k-1```, followed by ```4k``` to ```5k-1``` and so on.  
* ```S2``` contains characters at indices ```k``` to ```2k-1```,followed by the characters at the indices `3k` to `4k-1`, followed by `5k` to `6k-1`, and so on.
<br>
Take, for example, the string "question" and the value of 'k' to be 2. Then, <br>
S1 = quti     -- qu followed by ti<br>
S2 = eson     -- es followed by on<br>
<br>
Note that the last bunch (in S1 and /or S2) may not have all the k characters, if len(S) is not a multiple of 2k.<br>
<br>
The OUTPUT of the program is the tuple (S1, S2).  Use "print" to print the tuple directly.<br>

### NOTE:  
1. First line of the input contains the string S and the second line contains positive integer k. 
2. The string size will not exceed 1000 characters. The string does not contain white-spaces.
3. Assume k>0, and k<1000.
4. The last bunch may not be of size 'k'.

### Examples:

INPUT:
```
question
3
```
OUTPUT:
```
('queon', 'sti')
```
INPUT:
```
brown-bears
2
```
OUTPUT:
```
('brn-ar', 'owbes')
```
