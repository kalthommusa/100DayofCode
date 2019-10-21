import re
"""
Search the string to see if it starts with "Successfully" and ends with "Day57"
"""
day57="Successfully passed Day57"
x=re.search("^Successfully.*Day57$",day57)

if(x):
	print("Yes! We hsve a match")
else:
	print("No match")
