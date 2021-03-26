# A program in python to convert fahrenheit temp. to celsius

# Taking user input temp. in fahrenheit
faren = float(input())

# Calculating temp. in celsius
celsi = (faren - 32) * (5 / 9)

# Displaying required result
print('Fahrenheit temperature {} is same as {} degree Celsius.'.format(faren,round(celsi,2)))
