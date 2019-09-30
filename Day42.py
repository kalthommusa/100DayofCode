"""
create a function that prints a greeting 
and execute it on the p1 object
"""
class Person:
	def __init__(self, name, age):
		#the instances/properties/attributes of the class
		self.name=name
		self.age=age

	def myfunc(self):
		print("Hello World, My Name is "+self.name+"\nI'm "+str(self.age)+" years old")

day42=Person("John", 36)
#modify property
day42.age=40
#delete property, will cause an error
del day42.age
#delete object, will cause an error
del day42
day42.myfunc()
