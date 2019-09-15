#one line if statement
x=100
y=27
z=2019
if x > y: print("Successfully passed Day27")
#one line if else statement
print("Successfully passed Day26") if y > x else print("Successfully passed Day27")
#test if x is greater than y AND if z is greater than x
if x > y and z > x:
	print("Successfully passed Day27")

#test if x is greater than y OR if z is greater than x
if y > x or z > x:
	print("Successfully passed Day27")	

#nested if statements
if x > y:
	print("Successfully passed Day27")
	if z > x:
		print("Successfully passed Day27")
	else:
		print("Successfully passed Day26")