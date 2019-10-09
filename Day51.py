#create an alias for mymodule called mx
import mymodule as mx
mx.Callenge100DaysOfCode("Day51")

#import and use the built-in platform module
import platform 
x=platform.system()
print(x)
x=platform.python_version()
print(x)
#List all the defined names belonging to the platform module
x=dir(platform)
print(x)
