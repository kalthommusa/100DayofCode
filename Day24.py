#make a copy of a dictionary with the copy() method
dic={
	"challenge":"100DaysOfCode",
	"current_day":"Day24",
	"Year":2019
}
x=dic.copy()
print(x)
#make a copy of a dictionary with the dict() method
x=dict(dic)
print(x)
#make a new dictionary using the dict() constructor 
x=dict(challenge="100DaysOfCode",current_day="Day24",Year=2019)
print(x)
#make nested dictionaries of three dictionaries
language1={
	"name":"Pyhton",
	"developed_by":"Google",
	"developed_year":1991
}
language2={
	"name":"Javascript",
	"developed_by":"Netscape",
	"developed_year":1995
}
language3={
	"name":"Swift",
	"developed_by":"Apple",
	"developed_year":2014
}
programming_languages={
	"language1":language1,
	"language2":language2,
	"language3":language3
}
print(programming_languages)