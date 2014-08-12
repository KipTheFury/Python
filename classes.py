
#Object superclass
class Person(object):
	
	#constructor
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
	
	def printout(self):
		print "Name: %s" % self.name
		print "Age: %d" % self.age
		print "Height: %d" % self.height

# Inherits from Person class 
class Employee(Person):

	def __init__(self, name, age, height, salary):
		
		# Super constructor
		super(Employee, self).__init__(name, age, height)
		self.salary = salary

	def printout(self):
		# super printout()
		super(Employee, self).printout()
		print "Salary: %d" % self.salary

		
kyle = Person("Kyle", 26, 220)
louise = Person("Louise", 26, 140)

bob = Employee("Bob", 34, 120, 23000)

kyle.printout()
louise.printout()

bob.printout()

