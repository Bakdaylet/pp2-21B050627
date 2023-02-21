import datetime

today = datetime.datetime.now()
x = datetime.timedelta(1)
yesterday = today - x
tomorrow = today + x

print(yesterday.strftime("%A"))
print(today.strftime("%A"))
print(tomorrow.strftime("%A"))