# Project 2
# Uses MacArthur's 115 trick to calculate one's age and birth month
# 1/20/10

# Rules
print '\nThis is a puzzle favored by General MacArthur. You will be asked to secretly type in your birth month (as an integer) and your age. The computer will make a special calculation, yielding a new integer. The computer will then calculate, using only that special number, your birth month and age.\n'

# Input
while True:
    moStr = raw_input('Enter birth month as an integer: ')
    try:
        month = int(moStr)
        if month > 0 and month < 13:
            break
        else:
            print 'Birth month must be an integer. For example, Feb. corresponds with 2, Dec. with 12, etc.\n'
    except (TypeError, ValueError):
        print 'Invalid input.\n'

while True:
    ageStr = raw_input('Enter age as an integer: ')
    try:
        age = int(ageStr)
        if age > 0 and age < 100:
            break
        else:
            print 'Are you quite sure that\'s your age?\n'
    except (TypeError, ValueError):
        print 'Invalid input.\n'

# Calculation
special = (((((month * 2) + 5) * 50) + age) - 365)
print 'Your special number is',special,'.\n'

key = special + 115
keyMonth = key / 100
keyAge = key % 100

# Output
## New "Special" Number
print 'Your new special number is',key,'.'
## Month and Age
print 'The computer calculates that you were born in month',keyMonth,'and are',keyAge,'years old.'
