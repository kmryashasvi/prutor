# A Program in python to replace not...bad with good and print same string if nothing found

# Taking user input
inpu = input()

# Converting given string to lower case for ease of comparison 
inp = inpu.lower()

# Finding indes of "not" and "bad"
ind_not = inp.find("not")
ind_bad = inp.find("bad")


if ind_not == -1 or ind_bad == -1: 
    
    # Printing same string if nothing is found
    print(inpu)                            
    
elif ind_bad<ind_not:
    
    # Printing same string if "not" and "bad" are found in wrong order
    print(inpu)                            
    
else:
    # Dividing string into several parts (part1= part before not) (Part2= Part after bad)
    if ind_not == 0:
        part1 = ""
    else:
        part1 = inpu[:(ind_not-1)+1]

    if ind_bad == len(inp)-1:
        part2 = ""
    else:
        part2 = inpu[(ind_bad+3):]
    
    # Printing result after concatenation in appropriate cases
    if inpu[ind_not] == 'n':
        print(part1+"good"+part2)
    else:
        print(part1+"Good"+part2)
