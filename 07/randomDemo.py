import random
'''
The random package has a number of functions, but for here the sample function is useful. 
The sample function takes two arguments: a sequence (any sequence) to sample from and an
integer indicating how many samples to provide. Note that this is sampling "without replacement", 
that is the same element may NOT be selected multiple times in one call. However, multiple calls 
of sample make no such guarantee
'''
print 'One sample from a list of ints, 1-100:', random.sample(range(101),1)
print '5 samples, from a list of ints, 1-100:', random.sample(range(101),5)
print 'One sample from a string:', random.sample('abcdefg',1)
print '5 samples from a string:', random.sample('abcdefg',5)

# get the keys from a dictionary
myDict = {'bill':10, 'fred':20, 'herman':30, 'joseph':40, 'susan':50}
theKeys = myDict.keys()

# five samples from the list
print 'Five separate samples of a list of keys, replacement'
for i in range(5):
    print 'Random key is:', random.sample(theKeys,1)

# a list of five samples
print 'One sample of size 5 from the same list, no replacement'
print '5 samples from a key list:', random.sample(theKeys,5)
