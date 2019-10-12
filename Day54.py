#import the datetime module 
import datetime
day54=datetime.datetime.now()

#return the current date and time
print("Current Date and Time:",day54)

#return the name of the current day
day=day54.strftime("%A")

#return the name of the current month
month=day54.strftime("%B")

#return the time
time=day54.strftime("%X")

print("Successfully Passed Day54 on",day,month,"at",time)

#another way/formats to get current date and time
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	