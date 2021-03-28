# A program to find total marks of all the students by summing marks of different subjects

# Getting number of inputs to be provided
test = int(input())

# Declaring a dictionary
marks = {}

# Irerating through every input
for i in range(1,(test+1)):
    # Getting input comma separated values
    lis = list(map(str, input().split(',')))
    
    # Ignoring input if the input is not provided in the valid format
    if len(lis) != 3:
        continue
    
    # Removing the whitespaces from input taken
    lis[0] = lis[0].strip()
    lis[1] = lis[1].strip()
    lis[2] = lis[2].strip()
    
    # Declaring a key in the dictionary if the student is not already added in the dictionary
    if lis[0]+" # "+lis[1] not in marks:
        marks[lis[0]+" # "+lis[1]] = 0
    
    # Updating marks of the student
    marks[lis[0]+" # "+lis[1]] += int(lis[2])

# Making a seprate list all of the final keys and values for convenience 
mkey = list(marks.keys())
mval = list(marks.values())

# Sorting according to roll number and subject code
counter = -1
while counter != 0:
    counter = 0
    i = 0
    for i in range(len(mkey)-1-i):
        if mkey[i] > mkey [i+1]:
            mkey[i], mkey[i+1] = mkey[i+1], mkey[i]
            mval[i], mval[i+1] = mval[i+1], mval[i]
            counter += 1

# Displaying all the keys with their corresponding values
for i in range(len(mkey)):
    print(mkey[i],mval[i],sep=" # ")
 
