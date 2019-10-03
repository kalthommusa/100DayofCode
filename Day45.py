#return an iterator from a tuple, and print each value
mytuple=("apple", "banana", "cherry")
day45=iter(mytuple)
print(next(day45))
print(next(day45))
print(next(day45))

#iterate the values of a tuple using for loop
for day45 in mytuple:
	print (day45)

#strings are also iterable objects, containing a sequence of characters
mystring="apple"
day45=iter(mystring)
print(next(day45))
print(next(day45))
print(next(day45))
print(next(day45))
print(next(day45))

#iterate the characters of a string using for loop
for day45 in mystring:
	print(day45)

"""
create an iterator class that returns numbers,
starting with 1 t0 5, and each sequence will increase by one
"""
class MyNumber:
	def __iter__(self):
		self.a=1
		return self

	def __next__(self):
		x=self.a
		self.a +=1
		return x

day45=MyNumber()
myiter=iter(day45)
#print the numbers 1,2,3,4,5 but if we use for loop it will not stop iterating
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stop after 20 iterations
class MyNumber:
	def __iter__(self):
		self.a=1
		return self

	def __next__(self):
		if self.a <=20:
		   x=self.a
		   self.a +=1
		   return x
		else:
			raise StopIteration


day45=MyNumber()
myiter=iter(day45)

for x in myiter:
	print(x)