# Project 09
# Section 16
# Implements Spider Solitare given Card and Deck classes

# Algorithm:
'''
Initialize game
    Instructions
    Get difficulty
    Build stock
    Deal cards
Play
    For each turn
        Get input
        React accordingly
        Print updated tableau
'''

# Imports
import cards, pdb

# Global Variables
DIFFICULTY = 0 
POINTS = 500
REMAINING = 50
TURNS_TAKEN = 0 
WIN = False

# Functions
def deal10():
    '''
    Deals a card to the bottom of each stack.

    Algorithm:
        Check that there is at least 1 card per stack
        For each stack
            Append a card from stock
        Update remaining stock
    '''
    # Check for card in each stack
    minLen = True
    for stack in tableau:
        if len(stack) == 0:
           minLen = False 
    # Deal
    if stock.empty() == False:
        for stack in tableau:
            stack.append(stock.deal())
        global REMAINING
        REMAINING -= 10
    else:
        print 'No cards remaining in stock.'

def move(num, s1, s2):
    '''
    Moves a number of cards from stack to stack.

    Algorithm:
        Adjust for index
        Append the last [num] cards to specified stack
        Delete from old Stack
        If result is a full run, score
        Turn last card of first stack
        Update globals
    '''
    # Adjust for index
    s1 -= 1
    s2 -= 1
    # Append
    for i in range((len(tableau[s1]) - num), len(tableau[s1])):
        tableau[s2].append(tableau[s1][i])
    # Remove from original
    for i in range(0, num):# For the number of cards moved
        del tableau[s1][len(tableau[s1])-1]# Remove last card from the first list
    # If run is created, update score
    ## Starting at King
    k = 0 # Initialize index of king
    for i in range(0, len(tableau[s2])):
        if tableau[s2][i].get_rank() == 13:
            k = i
    ### If rank1 > rank2, continue until rank2 is ace
    seqSwitch = True
    for i in range(k, len(tableau[s2])-1):
        if tableau[s2][i].get_rank() > tableau[s2][i+1].get_rank():
            pass
        else:
            seqSwitch = False
    if seqSwitch == True and tableau[s2][len(tableau[s2])-1].get_rank() == 1:
    ## Delete cards from K-A
        for i in range(1, 14):
            del tableau[s2][len(tableau[s2])-1]
    ## Turn next bottom card
        tableau[s2][len(tableau[s2])-1].set_hidden(False)
    ## Add 100 to score
        global POINTS
        POINTS += 101 #101 so that net gain for a run move is 100
    # Turn bottom card
    if tableau[s1][len(tableau[s1]) - 1].get_hidden() == True:
        tableau[s1][len(tableau[s1]) - 1].set_hidden(False)
    # Update globals
    global TURNS_TAKEN
    TURNS_TAKEN += 1
    global POINTS
    POINTS -= 1

def play():
    '''
    Algorithm:
        As long as player doesn't quit and hasn't won
            For each turn
                Get input
                React accordingly
                Print updated tableau
                Check if game has been won
    '''
    # Check if game has ended
    kill = False
    global WIN
    while kill == False and WIN == False:
    # Get input
        command = raw_input('Command:(type \'h\' for help) ')
        # Move
        if command[0].lower() == 'm':
        ## Parse command 
            cl = command.split()
        ## Check command syntax
            if len(cl) == 4:# Has all required args
                if cl[1].isdigit() and cl[2].isdigit() and cl[3].isdigit(): # Proper argument types
                    for i in range(1,4):
                        cl[i] = int(cl[i])
                    if valid(cl[1], cl[2], cl[3]) == True:
                        move(cl[1], cl[2], cl[3])
                else:
                    print 'Invalid syntax.'
                    printHelp()
            else:
                print 'Invalid syntax.'
                printHelp()
        elif command[0].lower() == 'd':
            deal10()
        elif command[0].lower() == 'h':
            printHelp()
        elif command[0].lower() == 'q':
            kill = True
        else:
            print 'Unknown command: %s'%(command)

        # Print tableau
        printTableau()

        # Check for win
        emptyTableau = True
        for i in range(0, 10):
            if len(tableau[i]) > 0:
                emptyTableau = False
        if stock.empty() == True and emptyTableau == True:
            WIN = True
        
def printHelp():
    ''' Prints the help message'''
    print '\nResponses are:\n'
    print '\t\'m [number of cards] [stack A] [stack B]\' to move a certain number of cards from stack A to stack B'
    print '\t\'d\' to deal cards'
    print '\t\'h\' for help'
    print '\t\'q\' to quit'

def printTableau():
    '''
    Prints the tableau.

    Algorithm:
        Find the number of rows to print
        Print header
        Print cards
            For the number of desired rows
                Create rowList by appending stack[row] for each stack
                Print rowList
        Status
    '''
    # Find number of rows
    numRows = 0
    for stack in tableau:
        if len(stack) > numRows:
            numRows = len(stack)
    # Print header
    print '\nTableau:'
    print '\t  1\t  2\t  3\t  4\t  5\t  6\t  7\t  8\t  9\t 10'
    # Cards
    for row in range(0, numRows):# For each row-to-be
        rL = []# Create a list of values
        for stack in range(0, len(tableau)):# For each stack
            try:
                rL.append(tableau[stack][row])# Append to rowList the [row]th card in [stack]
            except IndexError:
                rL.append('   ')
        print '\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'%(rL[0], rL[1], rL[2], rL[3], rL[4], rL[5], rL[6], rL[7], rL[8], rL[9])
    # Status
    print '----------'
    print 'Stock: %d cards left\n'%(REMAINING)
    print 'Score: %d'%(POINTS)
    print 'Moves: %d'%(TURNS_TAKEN)

def valid(num, s1, s2):
    '''
    Checks whether a move is valid.

    Arguments: Number of cards to move, stacks
    Returns: Valid boolean
    Algorithm:
        Validate stack numbers
        Adjust for index
        Validate number of cards
        Validate sequence
            Number
            Suit
    '''
    validBool = True
    # Validate stack numbers
    if validBool == True:
        if 1 <= s1 <= 10 and 1 <= s2 <= 10:
            pass
        else:
            validBool = False
            print 'Invalid stack number(s).'
    # Adjust for index
    s1 -= 1
    s2 -= 1
    # Validate number of cards
    ## Enough cards in stack
    if validBool == True:
        if num > len(tableau[s1]):
            validBool = False
            print 'Not enough cards in stack.'
    ## Cards are face-up
    if validBool == True:
        for i in range((len(tableau[s1]) - num), len(tableau[s1])):
            if tableau[s1][i].get_hidden() == True:
                validBool = False
                print 'Can\'t move facedown cards.'
                break
    # Make tempStack
    if validBool == True:
        tempStack = []
        tempStack.append(tableau[s2][len(tableau[s2]) - 1])
        for i in range((len(tableau[s1]) - num), len(tableau[s1])):
            tempStack.append(tableau[s1][i])
    # Selected cards must be a run
        for i in range(1, len(tempStack)):
    ## each card's value must be less than that of previous card
            if tempStack[i].get_rank() == (tempStack[i-1].get_rank() - 1):
                pass
            else:
                validBool = False
                print 'Cards can only be moved to a card with the next-highest value.'
                break
    ## Same suit if difficulty 4
            global DIFFICULTY
            if DIFFICULTY == 4:
                if tempStack[i].get_suit() == tempStack[i-1].get_suit():
                    pass
                else:
                    validBool = False
                    print 'Cards can only be moved to a card with the same suit.'
                    break

    return validBool


# Initialize game
## Instructions
print 'Rules of Spider Solitaire:'
print 'The object of Spider Solitaire is to remove all of the cards from the ten stacks at the top of the window in the fewest number of moves.'
print '\nTo remove cards from the ten stacks at the top of the window, move the cards from one column to another until you line up a suit of cards in order from king to ace. When you line up a complete suit, those cards are removed.'
print '\nTableau:'
print '\tYou can move a card from the bottom of a stack to an empty stack.'
print '\tYou can move a card from the bottom of a stack to a card with the next highest value, regardless of suit or color.'
print '\tYou can move a set of cards all of the same suit, and in order, as if they were one card.'
print '\nStock:'
print '\tDealing from the deck moves 1 card to each stack.\n'
## Get difficulty
while True:
    inStr = raw_input('Command: (type \'1\' for one suit, type \'4\' for four suits) ')
    try:
        DIFFICULTY = int(inStr)
        if DIFFICULTY == 1 or DIFFICULTY == 4:
            break
        else:
            print 'Invalid input.\n'
    except(TypeError, ValueError):
        print 'Invalid input.\n'
## Build Stock
stock = cards.Deck()
tempDeck = cards.Deck()
stock.add_deck(tempDeck)
stock.shuffle()
## Deal Cards
stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9, stack10 = [], [], [], [], [], [], [], [], [], []
tableau = (stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9, stack10)
for i in range(0,4):
    for j in range(0,6):
        tableau[i].append(stock.deal())
        tableau[i][j].set_hidden()
for i in range(4,10):
    for j in range(0,5):
        tableau[i].append(stock.deal())
        tableau[i][j].set_hidden()
for i in range(0,10):
    tableau[i][(len(tableau[i]) - 1)].set_hidden(False)# Show bottom cards

# Play
printHelp()
printTableau()
play()
print '\n----------\n'
if WIN == True:
    print 'YOU WIN!!!\n'
print 'Turns taken: %d'%(TURNS_TAKEN)
print 'Final score: %d'%(POINTS)
print '\nThanks for playing!'
