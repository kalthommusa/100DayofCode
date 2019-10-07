#global variable
current_day="Day49"
#the function will print the local current_day
def printLocalVariable():

	current_day="Day49"
	print(current_day)
    #using the global keyword makes the variable belongs to the global scope
	global global_current_day
	global_current_day="Day49"

printLocalVariable()
#the code will print the global current_day
print(current_day)
#access and print the global_current_day 
print(global_current_day)
