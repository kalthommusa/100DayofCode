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
so now we are ready to add functionality in the __init__() function
"""
class Student(Person):
	#add a year parameter to the Student child class
    def __init__(self, fname, lastname, year):
    	#add super() function that will make the Student child class inherit from its parent
    	super().__init__(fname, lastname)

        #add a property called graduationyear to the Student child class
    	self.graduationyear=year

    #add a method called welcome to the Student child class
    def welcome(self):
    	print("Welcome "+self.fname+" "+self.lname+" to the class of "+str(self.graduationyear))

#create an object for the Student child class and pass the values of the arguments
day44=Student("Kalthom", "Musa", 2018)

#execute the fullname() methode that inherited from the Person parent class
day44.fullname()

#print the variable that created in the child Student class 
print("I graduted in "+str(day44.graduationyear))

#execute the welcome() methode that created in the child Student class
day44.welcome()
