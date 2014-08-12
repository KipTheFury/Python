'''
Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

Created on 11 Aug 2014

@author: Kyle
'''

def force(mass, acceleration):
    return float(mass) * float(acceleration)

def mass(force, acceleration):
    return float(force) / float(acceleration)

def acceleration(force, mass):
    return float(force) / float(mass)

while True:
    print "Type F to calculate Force, M for Mass or A for Acceleration:"
    calc = raw_input(">    ")
    
    if calc == "F" or calc == "f":
        mass = raw_input("Mass: ")
        acceleration = raw_input("Acceleration:")
        print "Force given Mass %r and Acceleration %r = %r" % (mass, acceleration, force(mass, acceleration))
    
    elif calc == "M" or calc == "m":
        force = raw_input("Force: ")
        acceleration = raw_input("Acceleration:")
        print "Mass given Force %r and Acceleration %r = %r" % (force, acceleration, mass(force, acceleration))
    
    elif calc == "A" or calc == "a":
        force = raw_input("Force: ")
        mass = raw_input("Mass:")
        print "Acceleration given Force %r and Mass %r = %r" % (force, mass, acceleration(force, mass))
    
    else:
        print "Incorrect selection"