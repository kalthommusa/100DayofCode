#prints the number of items in the list
x=["Successfully" , "passed" , "Day15"]
print(len(x))
#using the append() method to append an item
x.append("Great work")
print(x)
#inserts an item as the first position
x.insert(0, "Wow")
print(x)
#removes the specified item.
x.remove("Great work")
print(x)
#removes the specified item by it's index
x.pop(3)
print(x)
#makes a copy of a list with the list() method
y=x.copy()
print(y)
#any change in list x will not affect list y
x.pop(0)
print(x)
print(y)
#copy a list using list() method
y=list(x)
print(y)
#using the list() constructor to make a list
y=list(("Successfully" , "passed" , "Day15"))
print(y)
#delete the entire list items
x.clear()
print(x)