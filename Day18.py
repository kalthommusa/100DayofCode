#task 1 for week3
x=["Successfully" , "Passed" , "Day18"]

#method 1
x.append("Great Work!")
print(x)
#method 2
y=["Keep Moving Forward"]
x.extend(y)
print(x)
#method 3
print(x.count("Day18"))
#method 4
print(x.index("Day18"))
#method 5
x.reverse()
print(x)
#method 6
x.sort()
print(x)