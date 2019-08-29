x="Successfully passed Day"
y=9
print(x+str(y))

#format() method inserts number into string
x="Successfully passed Day{}"
y=9
print(x.format(y))

#format() method takes unlimited number of arguments
x=9
y=100
txt="This is day{} of the {}DaysOfCode challenge"
print(txt.format(x,y))

#returns the indexed  arguments in the placeholders
x=9
y=100
txt="This is day{1} of the {0}DaysOfCode challenge"
print(txt.format(y,x))
