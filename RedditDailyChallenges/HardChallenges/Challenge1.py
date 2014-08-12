'''
we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user_input user_input and great code!

Created on 11 Aug 2014

@author: Kyle
'''
import random

def new_random():
    return random.randint(low, high)

high = 100
low = 1
guess = new_random()

count = 0
user_input = ""

print "Think of a number between 1 and 100, I'll try to guess it, Enter (h) if its higher, (l) if its lower or (y) if its correct"
raw_input("Ready? Hit Enter to start...")

while not user_input == "y":

        prompt = "Is it %d" % guess
        user_input = raw_input(prompt)
        
        if not user_input =="y":       
                if user_input == "h":
                        low = guess + 1
                        count +=1
                        guess = new_random()

                elif user_input == "l":
                        high = guess - 1
                        count +=1
                        guess = new_random()
                else:
                        print "Invalid Input"
        
print "It was %d! I got it in %d guesses!" % (guess, count)
