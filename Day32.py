#task1 for week5
#print odd numbers from 1 to 17
print("Odd Numbers: ")
for i in range(1,18,2):
	print(i)

#another way to print odd numbers
for i in range(0,18):
	if i %2!=0:
		print("Odd Number: "+ str(i))


#print even numbers from 0 to 16
print("Even Numbers: ")
for i in range(0,18,2):
	print(i)

#another way to print even numbers
for i in range(0,18):
	if i %2==0:
		print("Even Number: "+ str(i))

		