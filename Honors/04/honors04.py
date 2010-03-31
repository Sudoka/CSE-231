# Honors Project 04
# Creates generations of bitstrings

# Algorithm
'''
Create 1st Generation
    For 2 individuals
        Append individual() to population
    Print
Crossover to make "new" individuals
    Crossover
    Print individuals
Mutation
    Mutate both w/ default rate
        Print
    Mutate each w/ specified rate
        Print
'''

# Imports
import pdb, random

# Classes
class individual(object):
    '''Stores a 100 character bitstring and its fitness'''
    def __init__(self):
        self.bitstring = self.genBitstring()
        self.genFitness()

    def __str__(self):
        return '%s : %d\n'%(self.bitstring, self.fitness)

    def flipBit(self, index):
        '''
        Flips a given bit in a given bitString.

        Arguments: Bit
        Algorithm:
            If bit = 1, make it 0
            If bit = 0, make it 0
            Else can't happen
        '''
        bitList = list(self.bitstring)
        if bitList[index] == '1':
            bitList[index] = '0'
        if bitList[index] == '0':
            bitList[index] = '1'
        else:
            print 'Can\'t happen.'
        self.bitstring = ''.join(bitList)

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

    def genFitness(self):
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
        for i in self.bitstring:
            if i == '1':
                count += 1
        self.fitness = count

    def mutate(self, rate=7):
        '''
        Mutates an individual.

        Arguments: individual of individual class, rate of mutation
        Algorithm:
            For each bit
                if random < rate
                    flip bit
            Regen fitness
        '''
        random.seed()
        for i in range(0, len(self.bitstring)):
            if random.randint(0,100) < rate:
                self.flipBit(i)
        self.genFitness()


# Functions
def crossover(ind1, ind2):
    '''
    Performs double crossover on two individuals' bitstrings.

    Arguments: Two individuals of individual class
    Algorithm:
        Create bitLists
        Divide each bitList into three sections
            Slice at random points
        Swap center sections
        Change bitstrings
        Regen fitness
    '''
    # Bitlists
    bitList1 = [i for i in ind1.bitstring]
    bitList2 = [i for i in ind2.bitstring]
    # Division
    random.seed()
    index1 = random.randint(0,98)
    index2 = random.randint(index1,100)
    newList1 = bitList1[:index1] + bitList2[index1:index2] + bitList1[index2:]
    newList2 = bitList2[:index1] + bitList1[index1:index2] + bitList2[index2:]
    newStr1 = ''.join(newList1)
    newStr2 = ''.join(newList2)

    ind1.bitstring, ind2.bitstring = newStr1, newStr2
    ind1.genFitness()
    ind2.genFitness()

def tournamentSelection(n=3, k=2):
    '''
    Selects k individuals with highest fitness from random selection n.

    Arguments: number to compare, number remaining
    Algorithm:
        Randomly select n individuals
            Generate n random indexes
            Create list of tuples w/ index and fitness for each individual
        Sort list by fitness greatest to least
        Select fittest (first) k individuals
            Print
    '''
    # Randomly select
    ## Index List
    indexSet = set([])
    while len(indexSet) < n:
        indexSet.add(random.randint(0,100))
    ## Individual tuples list
    indTupList = []
    for i in indexSet:
        indTupList.append((population[i].fitness, i))
    print 'Random individuals:\n'
    for i in indexSet:
        print population[i]
    # Sort by fitness
    indTupList.sort()
    indTupList = indTupList[::-1]
    # Select fittest k
    fitList = indTupList[0:k]

    print '\nThe fittest %d of %d individuals:\n'%(k, n)
    for i in fitList:
        print population[(i[1])]
    
# Initial Population
population = []
for i in range(0,100):
    population.append(individual())

# Select
tournamentSelection(5,3)
