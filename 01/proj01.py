# Project 1
# Accepts inputs to calculate ship mass and travel times
# 1/13/10


# Imports
from math import sqrt

# Input
while True: # Validation loop
    inStr = raw_input('Enter the percentage of the speed of light: ')
    try:
        percentSpeedLight = float(inStr)
        if percentSpeedLight >= 0 and percentSpeedLight < 100: # Checks range
            break
        else:
            print 'Invalid input.\n'
    except (TypeError, ValueError): # Exec if type or value error, enters loop.
        print 'Invalid input.\n'

# Calculation
## Given Variables
mass0 = int(70000)
velocityLight = int(299792458)
velocity = float(((percentSpeedLight / 100) * velocityLight))

## Given Distances
alpha0 = float(4.3)
barnard0 = float(6.0)
betelgeuse0 = float(309.0)
andromeda0 = float(2000000)

## Factor Equation
factor = float(1.0 / sqrt(1 - ((velocity ** 2) / (velocityLight ** 2))))

## Modified Values
mass1 = mass0 * factor
alpha1 = alpha0 / factor
barnard1 = barnard0 / factor
betelgeuse1 = betelgeuse0 / factor
andromeda1 =  andromeda0 / factor

#Output
print 'Travelling at ',percentSpeedLight,'% of the speed of light:\n'
## Weight of Ship
print 'The ship weighs ',mass1,' kilograms.'
## Travel Times
print 'Time to Alpha Centauri is ',alpha1,' years.'
print 'Time to Barnard\'s Star is ',barnard1,' years.'
print 'Time to Betelgeuse is ',betelgeuse1,' years.'
print 'Time to Andromeda is ',andromeda1,' years.'
