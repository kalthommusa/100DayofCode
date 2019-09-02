#an empty list
x=[]
print(x)
#a list of numbers
x=[1,2,3,4,5]
print(x)
#a list of strings
x=["Successfully" , "passed" , "Day13"]
print(x)
#combined list numbers and strings
x=["Successfully" , "passed" , "Day" , 13]
print(x)
#access a specific list item by its index
x=["Successfully" , "passed" , "Day13"]
print(x[2])
#print all of the list items using for loop
x=["Successfully" , "passed" , "Day13"]
for i in x :
	print(i)
#change the value of a list item by its index 
x=["Successfully" , "passed" , "Day13"]
x[1]="completed"
print(x)
#delete a list item by its index
x=["Successfully" , "passed" , "Day13"]
del x[0]
print(x)
#deletes the entire list , will cause an error
x=["Successfully" , "passed" , "Day13"]
del x
print(x)
