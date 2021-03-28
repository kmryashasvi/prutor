# GraphViz
## LAB3
## PROBLEM STATEMENT
In this problem you need to create a program for managing Graphs.<br>
The input to the program will be as described next:<br>
<br>
The first line will contain a positive integer N. N denotes the number of nodes in the graph. Nodes themselves are numbered from 0 to N−1. <br>
The second line will contain a non-negative integer M (M≥0). This will be the number of edges in the graph (However, some of these could be invalid/duplicate).<br>
The next M lines each will contain a pair of integers i,j representing a directed edge i→j. Self edges (i→i) are allowed. However, multi-edges  (two or more instances of i→j) have to be stored only once.<br>
Last line will contain an integer k.<br>
<br>
The output of the program is:<br>
<br>
If k represents a valid node, print all the nodes s such that s→k is a (directed) edge in the graph. The nodes have to be in sorted order, separated by COMMA (no whitespace).
<br>
If k does not represent a valid node, print "ERROR: Invalid Node."<br>
### EXAMPLES
___________________________________
INPUT:<br>
3<br>
4<br>
0,1<br>
1,2<br>
2,0<br>
0,2<br>
2<br>
<br>
OUTPUT:<br>
0,1<br>
_____________________________
<br>
INPUT:<br>
3<br>
4<br>
0,1<br>
0,2<br>
2,0<br>
0,2<br>
2<br>
<br>
OUTPUT:<br>
0<br>
_____________________________
<br>
INPUT:<br>
1<br>
0<br>
0<br>
<br>
OUTPUT:<br>
<br>              
(Note empty output)<br>
_____________________________

### NOTE: Remember that
* Self edges (i→i) are allowed. 
* Multi-edges  (two or more instances of i→j) have to be counted only once.
