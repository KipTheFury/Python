
number_list = [1,2,3,4,5]
string_list = ["abc", "def", "ghi"]
mixed_list = ["one", 2, "three", 4, "five"]

print string_list[2]
print string_list[1]

# For loops

# %d for digits
for number in number_list:
	print "Number: %d" % number

# %s for strings
for string in string_list:
	print "String: %s" % string

# use %r for raw data	
for mixed in mixed_list:
	print "Mixed: %r" % mixed
	
# empty list
elements = []

# loop 0-5
for i in range(0,6):
	print "Adding %d to the list" % i
	# add number to the list
	elements.append(i)

for i in elements:
	print "%d" % i

print
	
# While loops
i = 0
while i < 6:
	elements.append(i)
	i += 1
	
for i in elements:
	print "%d" % i