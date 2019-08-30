x=11
y=100 
z=x 
#returns False because one of the conditional statements are true
print(x>y and x<y)

#returns True because one of the conditional statements are true
print(x>y or x<y)

#returns False because x is not equal to y
print(x==y)

#returns True because x is not equal to y
print(x!=y)

#returns False because x is not the same object as y
print(x is y)

#returns True because x is not the same object as y
print(x is not y)

#returns True because z is the same object as x
print(z is x)

#returns True because x is the same object as z
print(x is z)

x= "Successfully passed Day11"
#returns True because the sequence "Day11" is in the x string
print("Day11" in x)

