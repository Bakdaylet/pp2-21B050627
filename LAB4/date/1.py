import datetime

x = datetime.datetime.now()

days = datetime.timedelta(5)

days_ago = x - days
print(days_ago.strftime("%A"))