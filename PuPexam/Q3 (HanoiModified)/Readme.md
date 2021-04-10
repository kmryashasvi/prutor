# HanoiModified
## PUP-EXAM
## PROBLEM STATEMENT
[10 Points]

###Towers of Hanoi Variant:

In the classic problem, we have three poles, A, B, C and N discs that fit onto the poles. The discs differ in size and are initially arranged on pole A in order from largest disc at the bottom to smallest disc at the top. The task is to move the stack of discs to pole C, while obeying the following rules: 
 
* Move only one disc at a time.
* Never place a disc on a smaller one. 

Here you have to solve Towers of Hanoi problem with the extra restrictions that 
 
* you are not allowed to directly transfer a disk from A to C.
* you are not allowed to directly transfer a disk from C to A. 

 In other words, every move must go involve pole B.

### INPUT:
a non-negative integer N, 0≤N≤15

### OUTPUT:
Movement of disks. The helper function to print the moves is given below.

### NOTE:
Use the following function (given) to print the move, to avoid mismatch due to whitespace. You can change rest of the code (it just gives a skeleton for traditional Tower Of Hanoi).
<br>
* the basic move of one disk: DO NOT CHANGE THIS
```python
NumOutput = 0
NumPerLine = 8
def move(From, To) :
    global NumOutput
    if (NumOutput%NumPerLine == 0):
        print('\n%5d:' % NumOutput, end=' ') # another way of printing formatted data
    else:
        print(end=' ')
    print('{}->{}'.format(From, To), end=' ')
    NumOutput += 1
    
    # End of the basic move of one disk: DO NOT CHANGE ABOVE
```

