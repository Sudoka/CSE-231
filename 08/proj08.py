# Project 08
# Section 16
# Calculate and graph BMI and other attributes using functions and dictionaries
# To Do:
## Display correlation

# Algorithm
'''
Import data
    Get target file
        Open body.data
        Parse
            Split by line
            Split lines into significant stats
            Create list of stat lists
        Check validity
Create X and Y lists
    Age of each individual
    BMICalc for each individual
Graph
    Age v. BMI
        Regression line
        Draw
    Weight v. Attributes
        Regression line
        Draw
'''

# Imports
import math, pdb
import matplotlib, matplotlib.pyplot as plt, numpy as np

# Functions
def BMICalc(weight, height):
    '''
    Calculates BMI according to a formula.

    Arguments: mass in kg, height in cm
    Returns: BMI float
    Algorithm:
        Convert units
        Formula
    '''
    heightM = height / 100
    BMI = weight / (heightM ** 2)

    return BMI

def attrCalc(CDi, CDep, BCDi, WG, AG, height):
    '''
    Calculates physical attributes according to the given formula.

    Arguments:
        Chest Diameter
        Chest Depth
        Bitrochanteric Diameter
        Wrist Girth
        Ankle Girth
        Height
    Returns: Attribute float
    Algorithm:
        Formula
    '''
    attr = -110 + 1.34 * CDi + 1.54 * CDep + 1.20 * BCDi + 1.11 * WG + 1.15 * AG + .177 * height

    return attr

def calcRegression(XList, YList):
    '''
    Calculates a regression line using the least squares method.

    Arguments: X values, Y values
    Returns: x and y point lists for regression line, correlation
    Algorithm:
        Get variables
        Calculate slope, intercept, correlation
        Create x and y lists
    '''
    # Variables
    sumX = sum(XList)
    sumY = sum(YList)
    sumXY = sum([XList[i]*YList[i] for i in range(0,len(XList))])
    sumXSquared = sum([i**2 for i in XList])
    sumYSquared = sum([i**2 for i in YList])
    numPairs = len(XList)
    # Calculate
    slope = (numPairs*sumXY-(sumX*sumY))/(numPairs*sumXSquared-(sumX)**2)
    intercept = (sumY-(slope*sumX))/numPairs
    correlation = corrCalc(numPairs, sumXY, sumX, sumY, sumXSquared,sumYSquared)
    # Create x and y lists
    XList.sort()
    regXList = []
    regXList.append(XList[0])
    regXList.append(XList[-1])
    regYList = []
    for x in regXList:
        regYList.append(calcRegPoint(slope, intercept, x))

    return (regXList, regYList, correlation)

def calcRegPoint(slope, intercept, X):
    '''
    Transforms a regDict into x and y values

    Arguments: Slope, intercept, regression x point
    Returns: Regression y point
    Algorithm:
        Find endpoints
        Create list of endpoints
    '''
    Y = slope * X + intercept

    return Y

def corrCalc(numPairs, sumXY, sumX, sumY, sumXSquared,sumYSquared):
    '''
    Caclulates the correlation for a regression line.

    Arguments:
        Number of pairs
        Sum of all products of X,Y pairs
        Sum of x vals
        Sum of y vals
        Sum of square of x vals
        Sum of square of y vals
    Returns: Correlation float
    Algorithm:
        Formula
    '''
    # Formula
    correlation = (numPairs*sumXY-(sumX*sumY))/math.sqrt((numPairs*sumXSquared-(sumX)**2)*(numPairs*sumYSquared-(sumY)**2))

    return correlation

def graph(XList, YList, XLabel, YLabel, title):
    '''
    Graphs x against y with regression line.

    Arguments: x list, y list, XLabel, YLabel, title
    Algorithm:
        Generate regression line endpoints
        Draw
    '''
    # Regression line coordinates
    regX, regY, correlation = calcRegression(XList, YList)
    # Draw
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(XList, YList, 'o', regX, regY, 'r-')
    ax.set_title(title)
    ax.set_xlabel(XLabel)
    ax.set_ylabel(YLabel)
    ## Correlation
    plt.annotate('Correlation: %f'%(correlation), (10,10), xytext=None, xycoords='axes pixels')

    plt.show()

def pullData(dataFile):
    '''
    Pulls and parses given dataset.

    Arguments: Data file
    Returns: Data as list of dictionaries of data
    Algorithm:
        Open
        Split into individual lines
        Split individual lines into stats
        Create dictionary
    '''
    # Open
    fileStream = open(dataFile, 'r')
    fileString = fileStream.read()
    fileStream.close()
    # Split into lines
    tempList = fileString.split('\n')
    for i in range(0, len(tempList)):
        tempList[i] = tempList[i].strip()
        tempList[i] = tempList[i].rstrip('\r')
        if tempList[i] == '': del tempList[i]
    # Split individual lines into stats
    for i in range(0, len(tempList)):
        tempList[i] = tempList[i].split()
    # Create dictionaries
    dictList = []
    for line in tempList:
        tempDict = {}
        tempDict['BCDi'] = float(line[2])
        tempDict['CDep'] = float(line[3])
        tempDict['CDi'] = float(line[4])
        tempDict['AG'] = float(line[19])
        tempDict['WG'] = float(line[20])
        tempDict['age'] = float(line[21])
        tempDict['weight'] = float(line[22])
        tempDict['height'] = float(line[23])
        dictList.append(tempDict)

    return dictList


# Import Data
data = pullData('body.dat')

# Create X and Y lists
## Age v. BMI
ageList = [line['age'] for line in data]
BMIList = [BMICalc(line['weight'], line['height']) for line in data]
## Weight v. Attributes
weightList = [line['weight'] for line in data]
attrList = [attrCalc(line['CDi'], line['CDep'], line['BCDi'], line['WG'], line['AG'], line['height']) for line in data]

# Graph
## Age v. BMI
graph(ageList, BMIList, 'Age (Years)', 'Body Mass Index', 'Age v. BMI')
## Weight v. Attributes
graph(weightList, attrList, 'Weight (kg)', 'Physical Attribute Number', 'Weight v. Attributes')
## Without this line, prog ends before user sees 2nd graph
weirdHack = raw_input('Press any key to exit')
