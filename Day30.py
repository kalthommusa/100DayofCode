#returns the numbers from 0 to 30 nusing the range() function
for i in range(31):
	print(i)

#returns the numbers from 1 to 30 using the start parameter
for i in range(1,31):
	print(i)

#increment the sequence with 3
for i in range(1,31,3):
	print(i)

#prints all numbers from 1 to 30, and prints a message when the loop has ended
for i in range(1,31):
	print(i)
else:
	print("Successfully passed Day30")

#prints each adjective for every fruit
x=["red", "big", "tasty"]
y=["apple", "banana", "cherry"]
for i in x:
	for j in y:
		print(i,j)