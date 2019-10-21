import re
#The findall() function returns a list containing all matches
day58="Successfully passed Day57"
x=re.findall("ss",day58)
print(x)
x=re.findall("Success",day58)
print(x)
x=re.findall("Successfully",day58)
print(x)