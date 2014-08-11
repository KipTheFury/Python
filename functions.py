
# argument array
def sum(*args):
	arg1, arg2 = args
	sum = arg1 + arg2
	print "%d + %d = %d"  % (arg1, arg2, sum)
	
# defined arguments
def multiply(first, second):
	print "%d * %d = %d" % (first, second, first * second)

# return statement
def divide(first, second):
	return first/second
	
sum(1234, 5678)
multiply(12, 34)

first=50
second=10

print "%d / %d = %d" % (first, second, divide(first, second))