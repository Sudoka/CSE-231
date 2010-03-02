# Project 06
# 02/23/10
# Uses functions to gather, parse, and calculate GDP and unemployment data

# Imports
import matplotlib.pyplot as plt
import numpy as np
import pdb

# Functions
## Get GDP
def getGDP(filename, year):
### Read in
    GDPstream = open(filename, 'r')
    GDPstring = GDPstream.read()
    GDPstream.close()
### Parse data
    yearList = GDPstring.splitlines()
#### Grab all quarters from specified year
    quarterList = []
    for line in yearList:
        if line.find(str(year)) != -1: 
            quarterList.append(line)
#### Split list at spaces into sublists in form [quarterStr, float]
    finalList = []
    for quarter in quarterList:
        finalList.append(quarter.split())
#### Convert values into floats
    for sublist in finalList:
        sublist[1] = float(sublist[1])
### Calculate average
    sum = 0
    for sublist in finalList:
        sum += sublist[1]
    avgGDP = sum / 4
    
    return avgGDP

## Get UE
def getUE(filename, year):
### Read in
    UEstream = open(filename, 'r')
    UEstring = UEstream.read()
    UEstream.close()
### Parse data
    dataList = UEstring.splitlines()
#### Split list at commas
    for line in dataList:
        if line.find(str(year)) != -1: 
            monthList = (line.split(','))
#### Convert values into floats
    for i in range(1,13):
        monthList[i] = float(monthList[i])
### Calculate average
    sum = 0 
    for i in range(1,13):
        sum += monthList[i]
    avgUE = sum / 12

    return avgUE

# Input
## Filenames
### GDP
while True:
    inStr1 = raw_input('GDP file name: ')
    try:
        GDPfile = inStr1
        open(GDPfile, 'r')
        break
    except (TypeError, ValueError):
        print 'Invalid input.\n'
    except IOError:
        print 'File not found. Try using full path, without escape characters.\n'
### UE
while True:
    inStr2 = raw_input('Unemployment file name: ')
    try:
        UEfile = inStr2
        open(UEfile, 'r')
        break
    except (TypeError, ValueError):
        print 'Invalid input.\n'
    except IOError:
        print 'File not found. Try using full path, without escape characters.\n'
## Year
while True:
    inInt = raw_input('Year to examine: ')
    try:
        year = int(inInt)
        if 1948 <= year <= 2008:
            break
        else:
            print 'Invalid year. Must be in range 1948-2008.\n'
    except (TypeError, ValueError):
        print 'Invalid input.\n'

# Computation
avgGDP = getGDP(GDPfile, year)
avgUE = getUE(UEfile, year)

# Output
print '\nFor',year,', the average GDP was',avgGDP,'and average unemployment was',avgUE,'.\n'

# Graph (http://matplotlib.sourceforge.net/examples/index.html)
## Generate Value Arrays
### X values
xArray = np.arange(1948, 2009)
### Y values
#### Y1 (GDP)
y1Array = []
for i in range(1948, 2009):
    y1Array.append(getGDP(GDPfile, i))
#### Y2 (UE)
y2Array = []
for i in range(1948, 2009):
    y2Array.append(getUE(UEfile, i))
## Calculate
fig = plt.figure()
### Axis 1
y1 = fig.add_subplot(111)
y1.set_xlabel('Year')
y1.plot(xArray, y1Array, 'b-')
y1.set_ylabel('Change in GDP', color='b')
for i in y1.get_yticklabels():
    i.set_color('b')
### Axis 2
y2 = y1.twinx()
y2.plot(xArray, y2Array, 'r-')
y2.set_ylabel('Unemployment Rate', color='r')
for i in y2.get_yticklabels():
    i.set_color('r')
## Draw
plt.title('GDP vs. Unemployment')
plt.show()
