#task2 for week4
dic={
	"name":"pigeon",
	"type":"bird",
	"skin_cover":"feathers"
} 
print(dic) 

#prints the value of the "type" key
x=dic["type"]
print(x)

#another way to prints the value of the "type" key
x=dic.get("type")
print(x)

#changes the value of the "skin_cover" key
dic["skin_cover"]="hair"
print(dic)

#prints all values in the dictionary, one by one
for i in dic :
	print(dic[i])