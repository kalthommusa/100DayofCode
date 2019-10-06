#create a local vaiable called current_day,the variable is not available outside the function
def myfunc():
	current_day="Day48"
	print(current_day)

myfunc()

#The local variable current_day can be accessed from a function within the function
def outer_function():
	current_day="Day48"
	def inner_function():
		print(current_day)
    #calling the inner function inside the outer function
	inner_function()

outer_function()

#create a global variable outside of any function
current_day="Day48"
def my_function():
	print(current_day)

my_function()
