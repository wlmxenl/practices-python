# 日历相关
# https://docs.python.org/zh-cn/3/library/calendar.html
# https://blog.csdn.net/y472360651/article/details/82291753
import calendar

# 判断指定是否是闰年，闰年为True，平年为False
print(calendar.isleap(2023)) # False

# 1970 年到 2023 年之间的闰年数量
print(calendar.leapdays(1970, 2023)) # 13

# 获取指定日期为星期几
print(calendar.weekday(2023, 1, 10)) # 1, 星期二

# 打印一年的日历
calendar.prcal(2023, m=6)