import random

#of type int
x=5
#of type float
y=5.2
#of type complex
z=5j

print(type(x))
print(type(y))
print(type(z))

print("")

#convert from int to float
a=float(x)
#convert from float to int
b=int(y)
#convert from int to complex
c=complex(x)

print(type(a))
print(type(b))
print(type(c))

print("")

#returns a random number between 1 and 10
print(random.randrange(1,10))
