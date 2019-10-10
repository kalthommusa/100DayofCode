#import the datetime module and display the full current date
import datetime
day52=datetime.datetime.now()
print(day52)

#return the year
print(day52.year)
#return the name of the day
day=day52.strftime("%A")

#return the name of the month
month=day52.strftime("%B")

#return the time
time=day52.strftime("%X")

print("Successfully passed Day52 on",day,month,"at",time)

#display the date
print(day52.strftime("%x"))
