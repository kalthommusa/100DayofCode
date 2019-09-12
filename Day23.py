dic={
	"challenge":"100DaysOfCode",
	"current_day":"Day23",
	"Year":2019
}
#check if "current_day" is present in the dictionary
if "current_day" in dic:
	print("Successfully passed Day23")

#return the number of items in the dictionary
print(len(dic))
#add an item to the dictionary
dic["language"]="Python"
print(dic)
#remove an item using pop() method
dic.pop("launguge")
print(dic)
#remove an item using popitem() method
dic.popitem()
print(dic)
#remove an item using del
del dic["challenge"]
print(dic)
#The clear() keyword empties the dictionary
dic.clear()
print(dic)
#delete the dictionary comlpetly
del dic
print(dic)