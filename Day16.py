#an empty tuple
x=()
print(x)
#create a tuple
x=("Successfully" , "passed" , "Day16")
print(x)
#a tuple contains only one item 
x=("Day16",)
print(x)
#the data inside a tuple can be of one or more data types
x=("Successfully" , "passed" , "Day" , 16)
print(x)
#return the item in position 2
x=("Successfully" , "passed" , "Day16")
print(x[2])
#iterate through the items and print the values
for i in x:
	print(i)

#display parts of the tuple
print(x[1:3])
#this will raise an error because the tuple is no longer exists
del x
print(x)	