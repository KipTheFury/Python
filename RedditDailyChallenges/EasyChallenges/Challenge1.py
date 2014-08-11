'''
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.

Created on 11 Aug 2014

@author: Kyle
'''
name = raw_input("Name?:")
age = raw_input("Age? :")
redditUsername = raw_input("Reddit UserName?:")

print "Your Name is %r, you are %r years old and your username is %r" % (name, age, redditUsername)
