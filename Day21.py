#create a set using the set() constructor 
x=set(("Successfully" , "passed" , "Day21"))
print(x)
#prints the length of the set
print(len(x))
#removes "Successfully" by using the remove() method
x.remove("Successfully")
print(x)
#removes "passed" by using the discard() method
x.discard("passed")
print(x)

set={"Successfully" , "passed" , "Day21"}
#removes the last item by using the pop() method
x=set.pop()
#return value of the pop() method is the removed item
print(x)
print(set)
#delete all the items in the set
set.clear()
print(set)
#delete the set completely from the memory
del set
print(set)