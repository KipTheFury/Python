'''
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!

Created on 12 Aug 2014

@author: kbennett
'''

def translate(mode, key, string):
    
    if mode == "d":
        key = -key
    
    translated = ""
    
    # for each letter...
    for letter in string:
        
        print letter + "\t",
        # convert to the ascii value
        val = ord(letter)
        
        print "%d \t" % val,
        # add the key value to encrypt/decrypt
        val = val + key
        
        print "%d \t" % val
        # Convert the ascii value to a character and add to a new string
        translated += chr(val)

    return translated
    
test = "This is a test"

encrypted = translate("e", 5, test)
print encrypted

decrypted = translate("d", 5, encrypted)
print decrypted
    