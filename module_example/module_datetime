# https://docs.python.org/zh-cn/3/library/datetime.html
from datetime import datetime, date, time as dtime, timezone
import time

print("------------------------ datetime-date ------------------------")
# date(year, month, day)
print(date.today()) # 2023-01-10
print(date.fromisoformat('2023-01-10')) # 2023-01-10
print(date.today().weekday()) # 1, 返回一个整数代表星期几，星期一为0，星期天为6。
print(date.today().isoweekday()) # 2, 返回一个整数代表星期几，星期一为1，星期天为7。
print(date.today().isocalendar()) # IsoCalendarDate(year=2023, week=2, weekday=2), year, week 和 weekday。
print(date.today().isoformat()) # 2023-01-10, 返回一个以 ISO 8601 格式 YYYY-MM-DD 来表示日期的字符串
print(date.today().ctime()) # Tue Jan 10 00:00:00 2023
print(date.fromtimestamp(time.time())) # 2023-01-10， 日期格式化
print(date(2020, 10, 30)) # 2020-10-30, 日期格式化

print("------------------------ datetime-datetime ------------------------")
# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
print(datetime.now()) # 2023-01-10 22:11:10.491895
print(datetime.now(timezone.utc)) # 2023-01-10 22:11:10.491895
print(datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")) # 2006-11-21 16:30:00
print(datetime.now().date()) # 2023-01-10
print(datetime.now().time()) # 22:29:42.325833
print(datetime.now().year) # 2023

print("------------------------ datetime-time ------------------------")
# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
print(dtime.fromisoformat('04:23:01')) # 04:23:01