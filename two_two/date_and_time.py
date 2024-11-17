import datetime

time_now = datetime.datetime.now()
print(time_now)
print(time_now.year)
print(time_now.second)
print(time_now.month)
print(time_now.isoweekday())

es_day = datetime.datetime(2015,2,22,13)
print(es_day)


my_time = "2023/12/05 12 hours, 30 mins, 10 sec"
python_date = datetime.datetime.strptime(my_time, "%Y/%m/%d %H hours, %M mins, %S sec")
print(python_date)
print(python_date.day)
print(python_date.year)
human_date = python_date.strftime("Year:%y, Month:%B, Day:%d")
print(human_date)