### Dates ###

from datetime import datetime

now = datetime.now()

print(now.year) # print(datetime.now().year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
timestamp = now.timestamp() # print(datetime.now().timestamp())

print(timestamp)


def print_date(date):
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2026, 7, 28, 15, 30, 45)

print_date(year_2023)

from datetime import time

current_time = time(15, 30, 45)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2026, 7, 28)

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year + 1, current_date.month, current_date.day + 3)
print(current_date)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

"""
diff = year_2023.time() - current_time # No deja
print(diff) 
"""

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)