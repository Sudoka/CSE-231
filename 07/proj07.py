# Project 07
# Section 016
# Uses dictionaries and globbing to make flashcards

# Algorithm
'''
Select vocab file
    Find .txt files in directory
    Input selection
        Parse file into dictionary
            File is a dictionary
        Check dict for vocab
            At least 1 item
            Only alpha in line
Print number of English words
Prompt for number of words tested
    Default all
    Keep within max
Quiz
    Select random entries
    Quiz each entry
    Count number of correct answers
    Compile dictionary of wrong answers
    Output final score
Write
    Prompt
        Default yes
    Location
        Default wrong.txt
        Prompt for overwrite

'''

# Imports
import datetime, glob, os.path, pdb, random

# Functions
def isVocab(testDict):
    '''
    Tests whether an object is a vocabulary dictionary.
    Assumes validity, switches if a test fails.

    Arguments: Target dictionary
    Returns: Yes/no bool
    Algorithm:
        Length check
        Keys
            Alpha
        Value Tuples
            Values
                Alpha
    '''
    vocabSwitch = True
    # Contains word lists
    if len(testDict) == 0:
        vocabSwitch = False
    # Keys
    for key in testDict.iterkeys():
        for i in key:
            if i.isalpha() == False and i.isspace() == False:
                vocabSwitch = False
    # Values
    for valueTuple in testDict.itervalues():
        for value in valueTuple:
            for i in value:
                if i.isalpha() == False and i.isspace() == False:
                    vocabSwitch = False
    return vocabSwitch

def pullDict(inFile):
    '''
    Opens and parses a given text file into a vocabulary dictionary.
    
    Arguments: Target vocab file
    Returns: Formatted vocab dictionary
    Algorithm:
        Read
        Parse
            Clean
            Split by language
            Split Spanish words into list
        Create dictionary from list
    '''
    # Read
    dictFile = open(inFile, 'r')
    dictString = dictFile.read()
    initVocabList = dictString.split('\n')
    # Parse
    ## Trim empty lines
    for i in initVocabList:
        if i == '':
            initVocabList.remove(i)
    ## Split English and Spanish
    listList = []
    for line in initVocabList:
        listList.append(line.split(':'))
    ## Split Spanish into list
    for i in listList:
        i[1] = tuple(i[1].split(','))# Converts Spanish list into tuple
    # Convert list into dictionary
    vocabDict = {}
    for i in listList:
        vocabDict.update({i[0]: i[1]})
   
    return vocabDict

def quiz(key, value):
    '''
    Quizzes the user on a given word and its translation(s).

    Arguments: English key, Spanish values
    Returns: Boolean whether answer was correct
    Algorithm:
        Present word and number of Spanish equivalents
        Get answer
            Sanitize
        Evaluate whether correctly translated
        Print results
    '''
    print '\n-----\n'
    print 'English word: ',key
    print 'Enter %d equivalent Spanish word(s).'%(len(value))
    correctBool = True
    # Take input for each
    for i in value:
        inStr = raw_input('Word :')
    ## Only alpha
        inList = []
        for j in inStr:
            if j.isalpha() or j.isspace():
                inList.append(j)
        word = ''.join(inList)
    # Evaluate
    ## if both answers are correct, return value is true
        if word in value: 
            continue
        else:
            correctBool = False
    # Print results
    if correctBool == True: print 'Correct!'
    else: print 'Incorrect.'
    # Return
    return correctBool

def write(wrongDict, targetFile):
    '''
    Writes a dictionary of incorrect entries to the target file.

    Arguments: Dictionary of missed words, file to write to
    Algorithm:
        Open target
        For each key
            Write key
            For each value corresponding to key
                Write value
                If value isn't last value, append ','
            Newline
        Close
    '''
    # Open
    writeFile = open(targetFile, 'w')
    # Write entry
    for key in wrongDict.keys():
    ## Key
        writeFile.write(key)
        writeFile.write(':')
    ## Value(s)
        for value in wrongDict[key]:
            # If key has multiple values
            if value == wrongDict[key][(len(wrongDict[key])) - 1]:
                writeFile.write(value)
            else:
                writeFile.write('%s,'%value)
        writeFile.write('\n')
    # Close
    writeFile.close()
    print 'Incorrect answers written to',targetFile,'.'

def writeWrong(wrongDict):
    '''
    Determines whether to write incorrect answers, and if so, to where.
    Depends on write().

    Arguments: Dictionary of missed words
    Algorithm:
        Get target file
            Check if file exists
                If so, prompt for overwrite
                If not, write
    '''
    # Prompt for file to write to
    inStr1 = raw_input('Filename (Defaults to \'wrong.txt\'): ')
    if inStr1 == '':
        target = 'wrong.txt'
    else:
        target = inStr1
    ## Check if it already exists
    ### If so, ask to overwrite
    if os.path.isfile(target) == True:
        while True:
            inStr2 = raw_input('File already exists. Overwrite? (Y/n): ')
    #### Default to yes
            if inStr2 == '':
                write(wrongDict, target)
                break
            else:
    #### Validate answer
                ovrList = []
                for i in inStr1:
                    if i.isalpha(): ovrList.append(i)
                ovr = ''.join(ovrList)
                ovr = ovr.lower()
                if ovr.isalpha() == True:
    #### Evaluate answer
                    if ovr[0] == 'y':
                        write(wrongDict, target)
                        break       
                    elif ovr[0] == 'n':
                        break
                else:
                    print 'Invalid input.\n'
    ### If not, create
    else:
        write(wrongDict, target)
                

# Select vocab file
## Find .txt files in directory
fileList = glob.glob('*.txt')
while True:
## Print files found
    print 'Select a file:'
    for i in fileList:
        print '\t',i
## Input
    selFile = raw_input('File: ')
    try:
        open(selFile, 'r')
## Parse file into dict if possible
        quizDict = pullDict(selFile)
## Check if dict contains vocab
        if isVocab(quizDict) == True:
            break
        else:
            print 'File is not a valid vocabulary dictionary.\n'
    except IOError:
        print 'Invalid filename.\n'


# Print number of English words in dict
print '%s contains %d entries.'%(selFile, len(quizDict))

# Prompt for number of words to be tested
while True:
    inStr1 = raw_input('Quiz on how many words? (Defaults to all) ')
    try:
        inWords = int(inStr1)
    except (ValueError, TypeError):
        'Invalid input.\n'
    if inStr1 != '':
        if 1 <= inWords <= len(quizDict):
            numWords = inWords
            break
        else:
            'Invalid input. There aren\'t that many words in the dictionary.\n'
    else:
        numWords = len(quizDict)# Default to all
        break

# Quiz
## init numCorrect, wrongDict
numCorrect = 0
wrongDict = {}
## For # of words specified
### Select random word pair
random.seed(datetime.time)
subDict = random.sample(quizDict, numWords)
for i in subDict:
### quiz(entry)
    correct = quiz(i, quizDict[i])
### if quiz returns true, increment numCorrect
    if correct == True:
        numCorrect += 1
### else add to wrongDict
    else:
        wrongDict.update({i: quizDict[i]})
## Output final score
print '\n-----\n'
print '%d out of %d correct.'%(numCorrect, numWords)

# Create file of incorrect answers?
## Prompt
while True:
    inStr2 = raw_input('Write incorrect answers to a new dictionary? (Y/n): ')
    if inStr2 == '':
        writeBool = 'y'
        break
    else:
        writeList = []
        for i in inStr2:
            if i.isalpha(): writeList.append(i)
        writeBool = (''.join(writeList)).lower()
        if writeBool.isalpha(): break
## Evaluate
if writeBool == 'y': writeWrong(wrongDict)
else: print 'Exiting without writing.'
