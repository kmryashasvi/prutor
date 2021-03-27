# A Program in python to replace "not...bad" in a string to "good"

# Getting user input
inpu = input()

# Converting whole string to lower case for convenience
inp = inpu.lower()

# Finding index of "not" and "bad"
ind_not = inp.find("not")
ind_bad = inp.find("bad")

# Refusing if string not contains "not...bad" (at least one occurence is needed according to question)
if ind_not == -1 or ind_bad == -1:
    print("Please Enter a string which contains 'not....bad'")
else:
    if ind_not == 0:                     # Making a string of before part of not
        part1 = ""
    else:
        part1 = inpu[:(ind_not-1)+1]

    if ind_bad == len(inp)-1:            # Making a string of after part of bad
        part2 = ""
    else:
        part2 = inpu[(ind_bad+3):]

    if ind_bad == len(inp)-1 and ind_not == 0: # Considering case when keywords are
        print(inpu)                                                      # at beginning/end
    else:
        if inpu[ind_not] == 'n':            # Printing result after concatenation
            print(part1+"good"+part2)
        else:
            print(part1+"Good"+part2)
