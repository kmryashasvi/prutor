# A program in python to print reverse and sum of original and reversed number.


# Taking user input (with no prompt)
num = str(int(input()))
""" Reason for above nested casting: for cases when user input is "0009"
                               when we convert "0009" to integer, we get 9,
                               When we again convert 9 to string "9" to enable slicing,
                               To easily reverse the number."""

# Geting reversed number through slicing
rev_num = int(num[::-1])  

#Calculating sum
sum = int(num) + rev_num

# Printing Results
print('Reverse:',rev_num)
print('Sum:',sum)
