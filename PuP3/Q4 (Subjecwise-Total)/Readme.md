# Subjectwise-Total
## LAB3
## PROBLEM STATEMENT
This problem is a continuation of the previous one, you need to create a program for managing marks for the students of some batch. Note that the expected OUTPUT is different.<br>
<br>
The input to the program will be as described next:<br>
The first line will contain a positive integer N. This will be followed by N lines, where each line will contain three items, separated by COMMA (,):
  ```
   Roll Number, Subject Code, Marks
  ```
Here Roll Number is a positive integer, Subject Code is an alpha-numeric string and Marks are integers. Any of the three items can repeat in the input. Also, whitespaces are allowed around the comma.
<br>
You task is to print the TOTAL marks for each Roll Number for each Subject Code on separate lines, sorted first by the Roll Number then by the Subject Code. Each Line in the output will have the form:
 ```
 Roll Number # Subject Code # Marks 
 ```
i.e., items are to be separated by a SPACE-HASH-SPACE ("```#```")  in the output.

### EXAMPLES:
____________________________________
Input:<br>
4<br>
101, CS101, 10<br>
101,   CS102, 20<br>
102, CS102  , 30<br>
101,CS101,-10<br>
<br>
Output:<br>
101 # CS101 # 0<br>
101 # CS102 # 20<br>
102 # CS102 # 30<br>
____________________________________
Input:<br>
6<br>
101, CS101, 10<br>
102,   CS102, 20<br>
102, CS102  , 30<br>
101,CS101,10<br>
101, CS101, 10<br>
102,   CS102, 20<br>
<br>
Output:<br>
101 # CS101 # 30<br>
102 # CS102 # 70<br>
___________________________________
