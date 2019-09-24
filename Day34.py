#passing a List as a parameter
def my_function(food):
	for x in food:
		print(x)

fruits=["apple","banana","cherry"]
my_function(fruits)

#recursion example
def recursion(k):
	if k>0:
		result=k+recursion(k-1)
		print(result)
	else:
		result=0

	return result

print("Recursion Example :")
recursion(6)