# Safe Bitcoins
## LAB4
## PROBLEM STATEMENT
You've saved the password to access your Bitcoins on your personal computer. You have created an application that encrypts the password. To decrypt, you need to perform an operation between two integers, say A and B, as described below - 

1. Let X and Y be the numbers obtained by REVERSING A and B. For example, the reverse of 123 is 321, and the reverse of 320 is 23 (leading zeroes are discarded)
2. If both X and Y are PRIME, then the answer is X + Y
3. If EXACTLY ONE of X and Y is PRIME, then the answer is A +  B
4. Otherwise, the answer is A * B

Your task is to write a program to help you perform this operation.

**Input**: Two COMMA-separated integers A and B. There can be any number of white-spaces in the input.<BR>
**Output** : A single integer that is the result of applying the operation described above on the input integers.
<BR>
**Constraints:** <BR>
1≤A,B≤10000

### Example:
Input:<BR>
142   ,123<BR>
Output:<BR>
265<BR>

### Explanation : The reverse of 142 is 241 (prime) and that of 123 is 321 (not prime). Hence the answer is A + B = 142 + 123 = 265

### IMPORTANT : Make sure your code is modular i.e. you REUSE as much of the code as possible USING FUNCTIONS. You may LOSE MARKS if this guideline is not followed.
