# Ackermann Limited
## LAB4
## PROBLEM STATEMENT
### Recall the Ackermann function:
```
A(0,n)     = n+1
A(m+1,0)   = A(m,1)
A(m+1,n+1) = A(m,A(m+1,n))
```

As you may have noticed, Ackermann function grows so quickly that it exhausts recursion depth very quickly. You will now write a program to avoid overflow.

The input to the program are THREE non-negative integers: m,n,T separated by COMMA (and optional whitespaces around comma).

The program attempts to compute A(m,n). if the TOTAL number of calls to A to compute the value is strictly less than T, then it prints the value and the number of calls made for the computation.  Otherwise (number of calls ≥T) it prints an error message. See the examples below.

### EXAMPLES:
<br>
INPUT: 0, 1, 5<br>
OUTPUT: Result = 2 in 1 calls<br>
<br>
INPUT: 0, 1, 0<br>
OUTPUT: Aborted<br>
<br>

### NOTES:
1. Note that the limit (threshold) applies to the TOTAL number of calls, not the recursion depth.
2. You will need to follow the recursive specification exactly to match the output. Changing it (modifying the base case, or changing the order of recursive calls) may result in a different output. In such cases, my automated grading script may fail. Please request re-grading after evaluation in case you feel your computation is correct but the marks are deducted.
