#import the regular expressions module
import re
day61="data is the new oil"

#the search() function returns a Match object
x=re.search("data",day61)
print(x)

"""
the span() function prints the position (start- and end-position) of the first match occurrence.
The regular expression searches for any words that starts with a lower case "d"
"""
x=re.search(r"\bd\w+",day61)
print(x.span())

"""
the group() function prints the part of the string where there was a match.
The regular expression searches for any words that starts with a lower case "d"
"""
x=re.search(r"\bd\w+",day61)
print(x.group())
