import datetime

today = datetime.date(2025, 10, 21)
today.day
today.month
today.year
print(today)

time_now = datetime.time(15, 15, 59)
time_now.hour
time_now.minute
time_now.second
print(time_now)

complete = datetime.datetime(2025, 10, 21, 15, 15, 59)
print(complete)

now = datetime.datetime.now()
print(now)

now_utc = datetime.datetime.now(datetime.timezone.utc)
print(now_utc)

print(now.strftime("%d-%b-%Y"))
print(now.strftime("Today is %d of %B of %Y"))


datetime_str = "12-Jul-2023"
print(datetime.datetime.strptime(datetime_str, "%d-%b-%Y"))

date_1 = datetime.datetime.strptime("12-Jul-2023", "%d-%b-%Y")
date_2 = datetime.datetime.strptime("01-Jan-2024", "%d-%b-%Y")
difference = date_2 - date_1
print(difference)
print(difference.days)

diff = datetime.datetime.now() + datetime.timedelta(days=1)
print(diff)
