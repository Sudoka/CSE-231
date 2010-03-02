import glob
'''
The '*' character is a matcher. It matches any sequence of characters (including no characters)
in a list of file names. The glob function returns a list, as strings, of all the files in
a directory that match the pattern. As demonstrated (and as required), only works in the 
directory the python program is run from.
'''
print '%-16s: %s'%("Ending in '.txt'",glob.glob('*.txt'))   # any file that ends in '.txt'
print '%-16s: %s'%("Ending in '.py'", glob.glob('*.py'))    # any file that ends in '.py'
print '%-16s: %s'%("Has a 'p' in it", glob.glob('*p*'))     # any file that has a 'p' in it somewhere, anywhere
print '%-16s: %s'%("Ends in 'y'",     glob.glob('*y'))      # any file that has, as its LAST character, a 'y'
print '%-16s: %s'%("Begins with 'v'", glob.glob('v*'))      # any file that has, as its FIRST character, a 'v'

