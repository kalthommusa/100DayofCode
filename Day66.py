#Using the index numbers with placeholders to display the expected result
day=66
txt="Work"
x="You have Successfully Passed Day{0}...Great {1}!"
print(x.format(day, txt))

x="You have Successfully Passed Day{1}...Great {0}!"
print(x.format(txt,day))

#Using named indexes with placeholders to display the expected result
x="You have Successfully Passed Day{day}...Great {txt}!"
print(x.format(day="66", txt="Work"))
