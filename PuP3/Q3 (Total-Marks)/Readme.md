# Total-Marks
## LAB3
### PROBLEM STATEMENT
In this problem (and the next), you need to create a program for managing marks for the students of some batch. <br>
<br>
The input to the program will be as described next:
The first line will contain a positive integer N. This will be followed by at least N lines, where each line will contain three items, separated by COMMA (,):
```
   Roll Number, Subject Code, Marks
```
Here Roll Number is a positive integer, Subject Code is an alpha-numeric string and Marks are integers. Any of the three items can repeat in the input. Also, whitespaces are allowed around the comma.
<br>
You task is to print the TOTAL marks for each Roll Number on separate lines, sorted by the Roll Number. Roll Number and marks are to be separated by a single : in the output.
<br>
### EXAMPLES:
____________________________________
Input:<br>
4<br>
101, CS101, 10<br>
101,   CS102, 20<br>
102, CS102  , 30<br>
102,CS101,-10<br>
<br>
Output:<br>
101:30<br>
102:20<br>
____________________________________
Input:<br>
1<br>
101, CS101, 10<br>
<br>
Output:<br>
101:10<br>
___________________________________ 
