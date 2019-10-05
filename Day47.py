#challenge 2 for week 7
#import the perant "Library" class 
from Day46 import Library

#create a child class named Science_Section
class Science_Section(Library):
	#add a "name" parameter to the Science_Section "child" class
    def __init__(self, book, shelf, name):
    	super().__init__(book, shelf)
    	self.name=name
    #add a method to the Science_Section "child" class
    def printselectedsection(self):
    	print("Selected Section :",self.name)
"""
create an object of the Science_Section "child" class
and pass values for book, shelf and name 
that will change the inherted values of book and shelf
"""
day47=Science_Section(20, 4, "Physics books") 
#access and print the value of "name" property 
day47.printselectedsection()
#access and print the reassigned values for "book" and "shelf" properties
print("Updating,\nThere are:",day47.book,"Books distributed over",day47.shelf,"Shelves in the Library")
