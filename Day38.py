#print each item in the cars array
cars=["Ford", "Volvo", "BMW"]
for x in cars:
	print(x)

#add one more element to the cars array
cars.append("Honda")
print(cars)

#delete the last element of the cars array
cars.pop()
print(cars)

#delete the second element of the cars array(indexing)
cars.pop(1)
print(cars)

#delete the element that has the value "Ford"
cars.remove("Ford")
print(cars)

#delete the reference of the array
del cars
print(cars)