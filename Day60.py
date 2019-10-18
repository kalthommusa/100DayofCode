#import the json module
import json
day60=("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")
print(type(day60))
#convert from Python to JSON
x=json.dumps(day60)
#return a JSON string
print(x)
print(type(day60))
