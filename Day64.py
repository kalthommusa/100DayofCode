"""
The try block will generate an exception, because x is not defined
Since the try block raises an error, the except block will be executed
"""
try:
	print(x)
except:
	print("An exception occurred")

#The try block does not raise any errors, so the else block wil be executed
x="Successfully passed Day64"
try:
	print(x)
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

#The finally block gets excuted no matter if the try block raises any errors or not
try:
	print(x)
except:
	print("Something went wrong")
finally:
	print("The 'try except' is finished")
