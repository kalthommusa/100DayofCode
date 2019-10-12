from datetime import date, timedelta

today= date.today()
yesterday= today - timedelta(1)
tomorrow= today + timedelta(1)

print("Today's date:",today)
print("Yesterday's date:",yesterday)
print("Tomorrow's date:",tomorrow)