'''
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)

Created on 12 Aug 2014

@author: kbennett
'''

import getpass

passwordfile = "password_protected.txt"

txt = open(passwordfile)

line = txt.readline().split(' ')

stored_username = line[0]
stored_password = line[1]

print stored_username
print stored_password

while True:

    username = raw_input("Username: ")
    password = getpass.getpass()

    if username == stored_username and password == stored_password:
        print "Access granted"
        break
    else:
        print "Access denied"