#import the json module 
import json

day56={
	"name":"Kaly",
	"age":25,
	"married":True,
	"divorced":False,
	"children":("Maick","Moley"),
	"pets":None,
	"cars":[
	 {
	 "model":"BMW230",
	 "mpg":27.5
	 },
	 {
	 "model":"Ford Edge",
	 "mpg":24.1
	 }
	 ]
}
#use 4 indents to make it easier to read the result
print(json.dumps(day56, indent=4))

#sort the result alphabetically by keys
print(json.dumps(day56, indent=4, sort_keys=True))