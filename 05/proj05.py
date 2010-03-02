# Project 5
# CLI for We Feel Fine
# 2/9/10

# Imports
import pdb
import string
import urllib

# Feelings
feelings = [['better', 0], ['bad', 0], ['good', 0], ['right', 0], ['guilty', 0], ['sick', 0], ['same', 0], ['shit', 0], ['sorry', 0], ['well', 0], ['down', 0], ['alone', 0], ['happy', 0], ['great', 0], ['comfortable', 0], ['sad', 0], ['free', 0], ['lost', 0], ['stupid', 0], ['tired', 0], ['weird', 0], ['lonely', 0], ['old', 0], ['home', 0], ['ill', 0]]

# Input
## Age
while True:
    inInt1 = raw_input('Age (All): ')
    if inInt1 == '':
        break
    try:
        age = int(inInt1)
        break
    except (TypeError, ValueError):
        print 'Invalid input. May be an integer.\n'

if inInt1 != '': ageRange = ((age / 10) * 10)

## Gender (1=male, 0=female)
while True:
    inStr1 = raw_input('Gender (All): ')
    if inStr1 == '':
        break
### Error Check
    try:
        inStr1 = str(inStr1)
    except (TypeError, ValueError):
        print 'Invalid input. Must be male, female, or their respective initial letters.\n'
### Validity
    if inStr1.isalpha() == False:
        for i in inStr1:# Remove non-alpha chars
            if i.isalpha() == False:
                inStr1 = inStr1.strip(i)
    inStr1 = inStr1.lower()# Uniform case
    if inStr1.isalpha() == True:# If remaining string has alpha characters
        testStr1 = inStr1[0]# Test the first character
        if testStr1 == 'm' or testStr1 == 'f':
            break
        else:
            print 'Invalid input. Must be male, female, or their respective initial letters.\n'
    else:
        print 'Invalid input. Must be male, female, or their respective initial letters.\n'
if inStr1 != '':
    gender = ''
    if testStr1 == 'm':
        gender = 1
    if testStr1 == 'f':
        gender = 0

## City (string, spaces allowed)
while True:
    inStr2 = raw_input('City (All): ')
    if inStr2 == '':
        break
    try:
        city = str(inStr2)
        break
    except (TypeError, ValueError):
        print 'Invalid input.\n'

if inStr2 != '':
    if city.isalpha() == False:
        for i in city:
            if i.isalpha() == False:
                city = city.strip(i)
    city = city.lower()
    city = city.strip()

## Other Feelings
while True:
    inStr3 = raw_input('Additional feelings (None): ')
    if inStr3 == '':
        break
    try:
        inStr4 = str(inStr3)
        break 
    except (TypeError, ValueError):
        print 'Invalid input. Accepts a list of adjectives, separated by whitespace.'

otherStr = ''
if inStr3 != '':
    for i in inStr4:
        if i in string.punctuation:
            i = ''
        otherStr += i
otherList = otherStr.split()
### Prepend to Valid Feelings
for i in otherList:
    feelings.insert(0, [i, 0])

# Query
## Assembly
url = 'http://api.wefeelfine.org:8080/ShowFeelings?display=text&returnfields=feeling,posttime' # posttime used to work around empy data when no specifications passed
if inInt1 != '': url += '&agerange='+str(ageRange)
if inStr1 != '': url += '&gender='+str(gender)
if inStr2 != '': url += '&city='+str(city)
## Send
print '\nRequesting',url
queryConnect = urllib.urlopen(url)
queryData = queryConnect.read()
queryConnect.close()

# Parsing
## Remove numbers
cleanData = ''
for i in queryData:
    if i.isdigit() == True:
        i = ''
    cleanData += i
## Separate
feelList = cleanData.split()
## Clean
for line in feelList:
    if line == '<br>':
        feelList.remove(line)
print '\nStripped data:\n'


# Count against valid feeling list
for feelArray in feelings:
   for feel in feelList:
        if feel == feelArray[0]: feelArray[1] += 1

# Formatting and Output
for feelArray in feelings:
    print '%11s : %2d' % (feelArray[0], feelArray[1])
