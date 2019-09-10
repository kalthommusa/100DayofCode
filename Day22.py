#craete an empty dictionary
dic={}
print(dic)

#create and print a dictionary
dic={
	"challenge":"100DaysOfCode",
	"current_day":"Day22",
	"Year":2020
}
print(dic)

#access en item by its key
x=dic["current_day"]
print(x)

#get the value of the "model" key
x=dic.get("current_day")
print(x)

#change the value of a specific item 
dic["Year"]=2019
print(dic)

#print all key names in the dictionary, one by one
for i in dic :
	print(i)

#print all values in the dictionary, one by one
for i in dic :
	print(dic[i])

#using values() method to print all values in the dictionary
for i in dic.values() :
	print(i)
	
#using values() method without for loop
print(dic.values())