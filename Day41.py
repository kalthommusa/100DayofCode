#create a Class nemed MyClass
class MyClass:
	x="Hello World"
"""
creat an object to call the created class 
and print the value of x
"""
day41=MyClass()
print(day41.x)
"""
create another Class nemed Person
and use the __init__() function 
to assign values for name and age
"""
class Person:
	def __init__(self, name, age):
		#the instances/properties/attributes of the class
		self.name=name
		self.age=age

day41=Person("John", 36)
print(day41.name)
print(day41.age)
