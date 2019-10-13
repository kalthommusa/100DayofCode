#import the json module 
import json

day55='{"challenge":"100DaysOfCode","current_day":"Day55","year":2019}'
#parse and convert from JSON to Python
x=json.loads(day55)
#return a Python dictionary
print(x["current_day"])

#a Paython dictionary
day55={
	"challenge":"100DaysOfCode",
	"current_day":"Day55",
	"year":2019
}
#convert from Python to JSON
x=json.dumps(day55)
#return a JSON 
print(x)