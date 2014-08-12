'''
Created on 12 Aug 2014

@author: kbennett
'''
string_morse ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/"
    }

morse_string = dict((v,k) for k, v in string_morse.iteritems())

def string_to_morse(string):
    
    string = string.upper()
    
    morse = ""
    
    for i in string:
        morse += string_morse[i] + " "
    
    return morse.strip()

def morse_to_string(morse):
    
    string = ""
    morse = morse.split("/")
    
    for word in morse:
        
        chars = word.split(" ")
                
        for char in chars:
            if not char == '':
                string += morse_string[char]
        
        string += " "
    
    return string.strip()
    
test_string = "My name is Kyle"    
test_morse = "-- -.-- / -. .- -- . / .. ... / -.- -.-- .-.. ."

print string_to_morse(test_string)
print morse_to_string(test_morse)        
