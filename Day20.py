#create an empty set
set={}
print(set)
#displays an unordered set without duplicate items
set={5,"Day20",3,5}
print(set)
#loop through the set and prints the values
set={"Successfully" , "passed" , "Day20"}
for i in set:
	print(i)

#check if "Day20" is present in the set
print("Day20" in set)
#add an item to a set, using the add() method
set.add("Great Work")
print(set)
#add multiple items to a set, using the update() method
set.update(["Keep","Move","Forward"])
print(set)