# Project 11
# Evolves a robot controller to follow trails
# To Do:
## refactor to use individual.fitness var 
## routlette wheel

# Algorithm
'''
ga.run()
'''

# Imports
import pdb, random, world

# Classes

class ga(object):
    '''Runs the genetic algorithm.'''

    def __init__(self, popSize, offspringPopSize, mutOffspring, mutBit):
        '''
        Initializes 200 individuals.

        Arguments:
            population size
            number of offspring
            percent of offspring mutated
            probability a bit mutates
        Algorithm:
            Store variables
            Create initial population
        '''
        # Store vars
        self.popSize = popSize
        self.offspringPopSize = offspringPopSize
        self.mutOffspring = mutOffspring
        self.mutBit = mutBit
        # Initial population
        self.popList = []
        for i in range(0, popSize):
            self.popList.append(individual())
        self.offspringList = []
        self.nextGenList = []

    def fitnessProportionateSelection(self, null, k, pool):
        '''
        Select individuals proportional to their fitness.

        Arguments: null (for interchangability), num selected, pool to draw from
        Returns: indecies of first k individuals selected
        Algorithm:
            Find totalFitness of pool
            For k individuals
                init
                    randomValue b/w 0 and totalFitness
                    sumFitness to 0
                    individualList
                For each individual
                    add fitness to sumFitness
                    if sumFitness >= randomValue
                        save individual as selected
        '''
        # Find totalFitness
        totalFitness = 0
        for i in pool:
            totalFitness += i.fitness
        # Select k individuals
        indexList = []
        while len(indexList) < k:
            # Setup
            random.seed()
            randomValue = random.randint(0,totalFitness)
            sumFitness = 0
            # Select
            for j in range(0,len(pool)):
                sumFitness += pool[j].fitness
                if sumFitness >= randomValue:
                    if j not in indexList: # Unique
                        indexList.append(j)
                        break
                    else:
                        continue

        return indexList

    def tournamentSelection(self, n, k, pool):
        '''
        Selects individuals for crossover based on fitness.

        Arguments: sample size, num individuals selected, pool to draw from
        Returns: list of indecies of k fittest individuals
        Algorithm:
            Randomly select n individuals
                Generate n random indexes
                Create list of tuples w/ index and fitness for each individual
            Sort list by fitness greatest to least
            Select fittest k individuals
        '''
        # Random selction
        ## Index List
        indexSet = set([])
        while len(indexSet) < n:
            indexSet.add(random.randint(0,(len(pool)-1)))
        ## Individual tuples list
        #pdb.set_trace()
        indTupList = []
        for i in indexSet:
            indTupList.append((pool[i].fitness, i))# Append (fit, index)
        # Sort by fitness
        indTupList.sort()
        indTupList = indTupList[::-1] # Highs first
        # Select fittest k
        fitIndexList = [i[1] for i in indTupList[0:k]]# Index of each fit tuple
                    
        return fitIndexList

    def run(self):
        '''
        Runs the GA for 20 generations.

        Algorithm:
            For 20 generations
                Create offspring
                    until len(offspringList) == offspringPopSize
                        find two parents
                            tournamentSelection(2,1)
                        cross over
                        add result to offspringList
                Mutate mutOffspring% of offspringList
                    for each offspring
                        if random int < mutOffspring
                            individual.mutate()
                Add offspring to parents' population
                Create next generation
                    select popSize individuals using tournamentSelection(2,1)
                    add selected to next gen
                Overwrite original population with next gen population
                    clear popList
                    move nextGenList to popList
                Find the fittest matrix of this population
                Print fittest matrix to a file
            Print world of the fittest individual
        '''
        # 20 generations
        for i in range(0,20):
            print 'Creating generation %d.'%(i+1)
        ## Create offspring
            while len(self.offspringList) != self.offspringPopSize:
                parent1 = self.fitnessProportionateSelection(2,1,self.popList)
                parent2 = self.fitnessProportionateSelection(2,1,self.popList)
                addTup = self.popList[parent1[0]].crossover(self.popList[parent2[0]])
                self.offspringList.append(addTup[0])
                self.offspringList.append(addTup[1])
        ## Mutate
            random.seed()
            for i in range(0,len(self.offspringList)):
                if random.randint(0,100) < self.mutOffspring:
                    self.offspringList[i].mutate(self.mutBit)
        ## Add to population
            for i in range(0,len(self.offspringList)):
                self.popList.append(self.offspringList.pop())
        ## Create next generation
            for i in range(0,self.popSize):
                self.nextGenList.append(self.popList[self.fitnessProportionateSelection(2,1,self.popList)[0]])
        ## Overwrite
            [self.popList.pop() for i in range(0,len(self.popList))]
            [self.popList.append(self.nextGenList.pop()) for i in range(0,len(self.nextGenList))]
        ## Find fittest individual
            fitList = [0, 0]
            for i in range(0, len(self.popList)):
                if self.popList[i].fitness > fitList[1]:
                    fitList[0] = i
                    fitList[1] = self.popList[i].fitness
        ## Print fittest matrix to a file
            writeFile = open('fittest.txt', 'a')
            writeObj = str(self.popList[fitList[0]])+'\n'
            writeFile.write(writeObj)
        # Print world of fittest individual
        self.popList[fitList[0]].evalFitness(True)
        print str(self.popList[fitList[0]])
        print 'For the fittest member of each generation, see fittest.txt.'

class individual(object):
    '''Represents a robot controller as a Braitenberg matrix.'''

    def __init__(self, matrix = []):
        '''
        Creates a Braitenberg matrix as a list of 6 numbers from -5 to 5.

        Algorithm:
            Create matrix
            If matrix is empty
                Append 6 numbers
                    Random -5 to 5
            Fitness
        '''
        # Create
        self.matrix = matrix
        # Check for contents
        if self.matrix == []:
        ## Append
            random.seed()
            self.matrix = [random.randint(-5,5) for i in range(0,6)]
        # Fitness
        self.fitness = self.evalFitness()

    def __str__(self):
        '''Prints the matrix and its fitness.'''
        return 'Matrix: '+str(self.matrix)+'\tFitness: '+ str(self.fitness)

    def __repr__(self):
        '''Prints the matrix.'''
        return str(self.matrix)

    def mutate(self, mutation_rate):
        '''
        Mutates an individual.

        Arguments: rate
        Algorithm:
            Seed
            For each matrix number
                if random < rate
                    generate new number
        '''
        # Seed
        random.seed()
        # Determine
        for i in range(0, len(self.matrix)):
            if random.randint(0,100) < mutation_rate:
                self.matrix[i] = random.randint(-5,5)

    def crossover(self, other):
        '''
        Produces two offspring by two-point crossover.

        Arguments: other individual
        Returns: tuple containing two individuals
        Algorithm:
            Create three segments out of each matrix
                Slice at two random points
            Swap center sections
            Create new individuals in offspringList
        '''
        # Create segments
        random.seed()
        i1 = random.randint(0,(len(self.matrix)-2))
        i2 = random.randint(i1, len(self.matrix))
        # Swap
        matrix1 = self.matrix[:i1] + other.matrix[i1: i2] + self.matrix[i2:]
        matrix2 = other.matrix[:i1] + self.matrix[i1: i2] + other.matrix[i2:]
        # New individuals
        new1 = individual(matrix1)
        new2 = individual(matrix2)

        return (new1, new2)

    def evalFitness(self, Print = False):
        '''
        Tests how many new squares the robot visits in 25 moves.

        Arguments: print toggle
        Returns: fitness points
        Algorithm:
            Init points
            Init world
            For each move
                Get sensor values from world
                Determine what to do (getActuators)
                    If both positive, 1 forward
                    If L positive, 1 square R
                    If R positive, 1 square L
                Move the agent in the world
                Check result
                    If on breadcrumb, 5 pts
                    If on dash, 1 pt
                    If on finish, 10 pts
        '''
        # Points
        points = 0
        # World
        world1 = world.World('World1.txt')
        # Each Move
        for i in range(0,25):
        ## Get sensor values
            senseTup = world1.getSensorValues()
        ## Determine action
        ### Actuators
            actuators = [0, 0]
            for i in range(0,2): # For each actuator
                for j in range(0, len(senseTup[0])): # For each sensor value
                    matrixElem = i * len(senseTup) + j # Element is actuator index * number of matrix values + present index in sensor val list
                    actuators[i] += self.matrix[matrixElem] * senseTup[0][j] # Actuator is selected element multiplied by present sensor val
            leftAct = actuators[0]
            rightAct = actuators[1]
        ## Move
            if leftAct > 0 and rightAct > 0:
                if Print == True:
                    print 'Moving forward.'
                world1.moveAgent(1)
            elif leftAct > 0:
                if Print == True:
                    print 'Moving right.'
                world1.moveAgent(2)
            elif rightAct > 0:
                if Print == True:
                    print 'Moving left.'
                world1.moveAgent(0)
        ## Check result
            if world1.isBreadcrumb() == True:
                points += 5
            elif world1.isDash() == True:
                points += 1
            elif world1.isFinal() == True:
                points += 10

        if Print == True:
            world1.printWorld()

        return points

# Run
ga = ga(200,50,50,25)
ga.run()
