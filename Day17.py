#check if "Day17" is present in the tuple
x=("Successfully" , "passed" , "Day17")
if "Day17" in x:
	print("Yes, Day17 exist in the tuple")

#repeats an item in a tuple, 17 stars
y=("*",)* 17	
print(y)

#concatenates 2 tuples, tuple x with itself
x+=("Great Work",)
print(x)

#prints the number of items in the tuple
print(len(x))

#using the tuple() method to create a tuple
z=tuple(("Keep moving forward",))
print(z)