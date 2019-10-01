"""
create a parent class named Person
with firstname and lastname properties
and a fullname method
"""
class Person:
	def __init__(self, fname, lname):
		self.fname=fname
		self.lname=lname

	def fullname(self):
		print("My Name is "+self.fname+" "+self.lname)
"""
create a child class named Student
and add the __init__() function to the child Student class
and keep the inheritance of the Person parent class
"""
class Student(Person):
    def __init__(self, fname, lastname):
    	Person.__init__(self, fname, lastname)
#creat object for class Student and execute the fullname function
day43=Student("Kalthom", "Musa") 
day43.fullname()
