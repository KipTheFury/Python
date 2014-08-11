from sys import argv

script, first, second, third = argv

if first > second:
	print "First is greater than second"
elif first < second:
	print "Second is greater than First"
else:
	print "First and Second are equal"
	
if (first > third) and (second > third):
	print "first and second are greater than third"
else:
	print "Third is greater than first and second"

if (first > third) or (second > third):
	print "first or second are greater than third"
else:
	print "Third is greater than first and second"

if not (first + second) == third:
	print "First + second does not equal Third"
else:
	print "first + second equal third"