from sys import argv

# 	My first python program

print "Hello World"
print "This is my first Python Program"

#	Maths functions

print "2 + 2 = ", 2 + 2 
print "20 / 5 = ", 20 / 5
print "3 * 4 = ", 3 * 4

#	Variables 

cars = 10
wheels = 4

print "number of wheels on 10 cars =", cars * wheels

#	Formatted strings

name = "Kyle"
age = 26

#%s for string, %d for digit, %r for raw
print "My name is %s and I am %d" % (name, age)

#	Input

#comma at the end of the line prevents a newline
print "What is your name?",
name = raw_input()

print "How old are you?",
age = raw_input()

print "Your name is %r and you are %r years old" % (name, age)

height = raw_input("How tall are you in inches?")

print "You are %r inches tall" % height

#	Command line arguments

#first arg is script name
script, first, second, third = argv

print "This program is called: %r" % script

print "first argument: %r" % first
print "second argument: %r" % second
print "third argument: %r" % third
