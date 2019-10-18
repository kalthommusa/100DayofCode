#import the regular expressions module
import re

#replace every white-space character with the number 59
day59="Keep Moving Forward"
x=re.sub("\s","59",day59)
print(x)
#replace the first 1 occurrence of the white speace with number 59
day59="Keep Moving Forword"
x=re.sub("\s","59",day59,1)
print(x)

#the search function returns a Match object
day59="Successfully Passed Day59"
x=re.search("Day59",day59)
print(x)

"""
the span() function prints the position (start- and end-position) of the first match occurrence.
The regular expression searches for any words that starts with an upper case "D"
"""
x=re.search(r"\bD\w+",day59)
print(x.span())

#the string property returns the search string 
x=re.search(r"\bD\w+",day59)
print(x.string)

"""
the group() function prints the part of the string where there was a match.
The regular expression searches for any words that starts with an upper case "D"
"""
x=re.search(r"\bD\w+",day59)
print(x.group())
