# A program to find total marks of all the students by summing marks of different subjects

# Getting number of inputs to be provided
test = int(input())

# Declaring a dictionary
marks = {"roll":"marks"}

# Irerating through every output
for i in range(1,(test+1)):
    # Getting input comma separated values
    lis = list(map(str, input().split(',')))
    # Removing the whitespaces from input taken
    lis[0] = lis[0].strip()
    lis[1] = lis[1].strip()
    lis[2] = lis[2].strip()
    
    # Declaring a key in the dictionary if the student is not already added in the dictionary
    if int(lis[0]) not in marks:
        marks[int(lis[0])] = 0

    # Updating marks of the student
    marks[int(lis[0])] += int(lis[2])

# Making a seprate list all of the final keys and values for convenience 
mkey = list(marks.keys())
mval = list(marks.values())

# Displaying all the keys with their corresponding values
for i in range(1,len(mkey)):
    print(mkey[i],":",mval[i],sep="")
    
