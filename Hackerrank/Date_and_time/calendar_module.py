__author__ = 'anna'
import calendar
c = calendar.TextCalendar()
print(c.formatyear(2015))
print(c.formatmonth(2016, 5))

date = '08 05 2015'
month, day, year = map(int, date.split())
print(month, day, year)
weekday = calendar.weekday(year, month, day)
print(calendar.day_name[weekday].upper())
