# Project 04
# Applies rotation cypher using a for loop and indexing


# Functions
def encode (encStr, rotInt):
    # Alphabets
    alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = alpha1[rotInt:] + alpha1[:rotInt] 

    # Cypher
    newStr = ''
    for i in encStr:
        if i.islower() == True:
            newChar = alpha2[alpha1.find(i)]# .find() returns the index of i
            newStr = newStr + newChar
        else:
            newStr = newStr + i
    return newStr

def decode (cryptStr, targetStr):
    for i in range(1, 25):
        testStr = encode(cryptStr, -i)# Reverses the encode function
        if testStr.find(targetStr) != -1:# If match is found
            return i
            break
        else:
            if i < 25:
                continue
            else:
                return 'No matches found.\n'

# Main Loop
## Mode Selection
kill = False
while kill == False:
    print 
    while True:
        inStr = raw_input('Encode (e), Decode (d), or Quit (q): ')
        try:
            mode = str(inStr)
            mode = mode.lower()
            if mode == 'e' or mode == 'd' or mode == 'q': # Option check
                break
            else:
                print 'Invalid option.\n'
        except (TypeError, ValueError):
            print 'Invalid input\n.'

## Mode Inputs
    if mode == 'e':
        ### Input
        while True:
            inStr = raw_input('String to be encoded: ')
            try:
                encStr = str(inStr.strip())
                break
            except (TypeError, ValueError):
                print 'Invalid input.\n'
        while True:
            inInt = raw_input('Rotation integer: ')
            try:
                rotInt = int(inInt)
                if 0 <= rotInt <= 25:
                    break
                else:
                    print 'Invalid input.\n'
            except (TypeError, ValueError):
                print 'Invalid input.\n'
        ### Logic / Output
        print '\n',encode(encStr, rotInt),'\n'

    elif mode == 'd':
        ### Input
        while True:
            inStr1 = raw_input('Encrypted string: ')
            try:
                cryptStr = str(inStr1.strip())
                break
            except (TypeError, ValueError):
                print 'Invalid input.\n'
        while True:
            inStr2 = raw_input('Plaintext target substring: ')
            try:
                targetStr = str(inStr2.strip())
                break
            except (TypeError, ValueError):
                print 'Invalid input.\n'
        ### Logic / Output
        result = str(decode(cryptStr, targetStr))
        if result.isdigit() == True:
            print 'The rotation was',result,'.\n'
        else:
            print result

    else:
        kill = True
print 'Goodbye.'
