
import urllib

address = raw_input("Open what address:")
connection = urllib.urlopen(address)

pageStr = connection.read()

print "This is the contents of the page"
print pageStr
