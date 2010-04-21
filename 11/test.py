import random


def getActuators (matrix, sVals):
    ''' Computes the values of the actuators (wheels) using the evolved matrix
    and the robot sensor values. Returns the value for the left wheel and the
    right wheel. '''
    leftWheel = 0
    rightWheel = 0
    acts = [0,0] 
  
    for i in range(0,2):
        for j in range(0, len(sVals)):
            matrixElem = i * len(sVals) + j
            acts[i] += matrix[matrixElem] * sVals[j]
            
    leftWheel = acts[0]
    rightWheel = acts[1]
    return leftWheel, rightWheel


lWheel, rWheel = getActuators([1, 0, -5, 2, 1, 1], [1, 2, 1])
print "Left wheel is: ", lWheel
print "Right wheel is: ", rWheel
