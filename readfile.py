from sys import argv

script, filename = argv

# open file
txt = open(filename)



print "The file %r contains: \n" % filename

# Read the contents of the file
print txt.read()

# get length of file
print "File size =  %d bytes" % len(filename)

print "Enter the filename"
filename = raw_input("> ")

txt = open(filename)

print txt.read()

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

# open in "write" mode - truncates existing files
# 'r' - read
# 'a' - append
target = open(filename, 'w')

print "Emptying %r" % filename

# delete file contents
target.truncate()

print ("Rewrite the file")

line1 = raw_input("First Line:")
line2 = raw_input("Second Line:")
line3 = raw_input("Third Line:")

# write to the file
target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

# close the file
print "Closing file..."
target.close()
