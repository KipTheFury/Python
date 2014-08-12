'''
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!

Created on 12 Aug 2014

@author: kbennett
'''

import random

sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

amount = int(raw_input("How many Passwords? :"))
length = int(raw_input("Password Length? :"))

for i in range(amount):

    password = ''.join(random.sample(sample * length, length))
    
    print password