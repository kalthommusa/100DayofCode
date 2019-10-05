#challenge 1 for week 7
"""
create a perant class nemed Library
and use the __init__() function 
to assign values for book and shelf properties
"""
class Library:
	def __init__(self, book, shelf):
		
		self.book=book
		self.shelf=shelf
"""
create an object of the perant "Library" class
and pass values for book and shelf
"""
day46=Library(300, 45)

#access and print the properties of the perant "Library" class
print("There are:", day46.book, "Books distributed over", day46.shelf, "Shelves in the Library")
