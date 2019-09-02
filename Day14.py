#returns a slice object
x=["Successfully" , "passed" , "Day14"]
print(x[1:3])

#check if "Day14" is present in the list.
if "Day14" in x:
	print("Yes, 'Day14' is in our list: "+ str(x))
	print("Great work so far...")
	print("14 Days of progress --> 14 Stars for your progress:")
	#repeats an item in a list	
	y=['*']*14
	print(y)

#combine 2 lists into one list
y=["of the 100DaysOfCodes" , "challenge"]
z=x + y
print(z)
