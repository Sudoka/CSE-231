# Honors Project 02
# Creates a population of bitstrings and evaluates their fitness
# Algorithm
'''
For 100 individuals
    Generate bitstring
        100 bits
        Random
        Print
    Evaluate fitness
        Count 1s
        Store
'''

# Imports
import datetime, pdb, random, string

# Functions
def fitness(individual):
    '''
    Evaluates fitness based on number of 1 bits.

    Arguments: Bitstring
    Return: Fitness float
    Algorithm:
        Initialize count
        For each bit in string
            If 1, increment count
    '''
    count = 0
    for i in individual:
        if i == '1':
            count += 1
    return count
        

def genIndividual():
    '''
    Creates a 100 bit string of random bits.

    Returns: Individual array
    Algorithm:
        Seed random
        Create bitstring
            For 100 chars
                Randomly append 1 or 0 to bitList
            Merge bitList
        Create individual
            Append bitList
            Assign fitness
    '''
    # Create Bitstring
    random.seed()
    bitList = []
    for i in range(1,101):
        bitList.append(str(random.randint(0,1)))
    bitString = ''.join(bitList)
    # Create individual
    individual = [bitString, 0.0]

    return individual

# 100 individuals
population = []
for i in range(0,101):
    population.append(genIndividual())

# Evaluate fitness
for individual in population:
    individual[1] = fitness(individual[0])

# Print individuals
for individual in population:
    print individual
