# Honors Project 02.1
# Creates a population of bitstrings and evaluates their fitness using classes
# Algorithm
'''
For 100 individuals
    Append individual() to population
For each individual in population
    Print individual
'''

# Imports
import pdb, random

# Classes
class individual(object):
    '''Stores a 100 character bitstring and its fitness'''
    def __init__(self):
        self.bitstring = self.genBitstring()
        self.fitness = self.genFitness(self.bitstring)

    def __str__(self):
        return '%s : %f\n'%(self.bitstring, self.fitness)

    def genBitstring(self):
        '''
        Creates a 100 bit string of random bits.

        Returns: 100 bit string
        Algorithm:
            Seed random
            Create bitstring
                For 100 chars
                    Randomly append 1 or 0 to bitList
                Merge bitList
        '''
        random.seed()
        bitList = []
        for i in range(1,101):
            bitList.append(str(random.randint(0,1)))
        bitString = ''.join(bitList)

        return bitString

    def genFitness(self, bitString):
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
        for i in bitString:
            if i == '1':
                count += 1
        return count

# 100 individuals
population = []
for i in range(0,101):
    population.append(individual())

# Print
for i in population:
    print i
