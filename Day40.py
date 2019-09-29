#task2 for week6
#print positive numbers in a list
my_Day40=[-4, -6, -5, -1, 2, 3, 7, 9, 88]

def positive_Numbers(x):
	for i in x:
		if (i>=0):
			print("Positive Number :"+str(i))

positive_Numbers(my_Day40)

#another way to print positive numbers in a list(Lambda function)
positive_Numbers = list(filter(lambda varX: varX >= 0,my_Day40))
print("The positive numbers in the list ="+str(positive_Numbers))