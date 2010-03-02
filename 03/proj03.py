# Project 03
# Counts occurrences of a digit in a given number
# 01/26/10

# Input
## Number
while True:
    inStr1 = raw_input('Enter an integer: ')
    try:
        number = int(inStr1)
        break
    except (TypeError, ValueError):
        print 'Invalid input.\n'

## Digit
while True:
    inStr2 = raw_input('Enter a digit: ')
    try:
        digit = int(inStr2)
        if 0 <= digit <= 9:
            break
        else:
            print 'A digit must be an integer 0-9.\n'
    except (TypeError, ValueError):
        print 'Invalid input.\n'

# Counting Algorithm
## Init
counter = 0
place = 1
modNumber = abs(number)

## Break Number Into Digits
while (modNumber / 10) > 0:
    modNumber = (abs(number) / place)# If number is negative, Bad Things happen
    if (modNumber % 10) == digit:
        counter += 1 # Conditional increment
    place = place * 10

# Output
print '\nThe number of',digit,'s in',number,'is',counter,'.'
