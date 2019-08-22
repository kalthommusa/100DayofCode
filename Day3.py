#Variables do not need to be declared with any particular type
x='Day3'
print(x)

#double quotes are the same as single quotes
x="Day3"
print(x)

#it is of type string
Day="3"

#it is of type integer
day=3
"""
Variable names are case-sensitive in python
so Day & day are different variables

"""
print(type(Day))
print(type(day))

#combine both text and variables
x, y =" passed", " Day3"
print("Successfully" + x +y)

#for numbers, the + character works as a mathematical operator
x=5
y=2
print(x+y)

#convert the number into a string to combine text and number
x=" Day"
y=3
print("Successfully passed" + x +str(y)) 