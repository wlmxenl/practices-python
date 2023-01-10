# https://docs.python.org/zh-cn/3/library/time.html
import time

print("当前时间（单位秒）：%d" % int(time.time()))
print(time.asctime()) # Tue Jan 10 21:07:43 2023
print(time.tzname) # ('中国标准时间', '中国夏令时')
print(time.localtime()) # 当地时间   (tm_year=2023, tm_mon=1, tm_mday=10, tm_hour=21, tm_min=33, tm_sec=24, tm_wday=1, tm_yday=10, tm_isdst=0)
print(time.gmtime())    # UTC 时间   (tm_year=2023, tm_mon=1, tm_mday=10, tm_hour=13, tm_min=33, tm_sec=24, tm_wday=1, tm_yday=10, tm_isdst=0)
# https://docs.python.org/zh-cn/3/library/time.html#time.strftime
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
