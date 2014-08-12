'''
write a program that will allow the user to to_sort digits, and arrange them in numerical order.
for extra credit, have it also arrange strings in alphabetical order

Created on 12 Aug 2014

@author: kbennett
'''

def do_sort(to_sort):
    
    array = []
    
    for i in to_sort:
        array.append(i)
    
    array.sort()
    return array  

to_sort = raw_input("What do you want to sort? :")
print do_sort(to_sort)

# one line solution
print sorted(raw_input(">>"))