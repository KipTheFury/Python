'''
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.

Created on 12 Aug 2014

@author: kbennett
'''
bottles = 99

while bottles > 0:
    if bottles > 1:
        print "%d bottles of beer on the wall\n%d bottles of beer" % (bottles, bottles)
    else:
        print "%d bottle of beer on the wall\n%d bottle of beer" % (bottles, bottles)    
    
    print "take one down, pass it around"
    bottles -= 1 
    
    if bottles > 1:
        print "%d bottles of beer on the wall\n" % bottles
    elif bottles > 0:
        print "%d bottle of beer on the wall\n" % bottles
    else:
        print "No more bottles of beer on the wall" 