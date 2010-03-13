# Honors Project 01
# Creates a bitstring and evaluates its fitness
# Algorithm
'''
Generate bitstring
    100 bits
    Random
    Print
Evaluate fitness
    Count 1s
    Print
'''

# Imports
import datetime, pdb, random, string

# Functions
def fitness(bitString):
    '''
    Evaluates fitness based on number of 1 bits.

    Arguments: Bitstring
    Return: Fitness integer
    Algorithm:
        Initialize count
        For each bit in string
            If 1, increment count
    '''
    count = 0
    for i in bitString:
        if i == '1':
            count += 1
    return count
        

def genIndividual():
    '''
    Creates a 100 bit string of random bits.

    Returns: Bitstring
    Algorithm:
        Seed random
        For 100 chars
            Randomly append 1 or 0 to bitList
        Merge bitList
    '''
    random.seed(datetime.time)
    bitList = []
    for i in range(1,101):
        bitList.append(str(random.randint(0,1)))
    bitString = ''.join(bitList)
    return bitString


# Generate bitstring
bitString = genIndividual()
print 'Bitstring:',bitString

# Evaluate fitness
fitness = fitness(bitString)
print 'Bitstring\'s fitness is %d.'%(fitness)
