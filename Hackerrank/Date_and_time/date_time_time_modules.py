__author__ = 'anna'

import time
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime())
my_tuple = (2011, 6, 2, 15, 6, 0, 0, 0, 0)
print(time.mktime(my_tuple))
print(time.localtime(time.mktime(my_tuple)))
print()
print(datetime.datetime.utcnow())
print(datetime.datetime.now())
print(datetime.datetime.now().isoformat())

print('Challenge:')
t_stamp_1 = "Sun 10 May 2015 13:54:36 -0700"
t_stamp_2 = "Sun 10 May 2015 13:54:36 +0000"
time_1 = datetime.datetime.strptime(t_stamp_1, "%a %d %b %Y %H:%M:%S  %z")
time_2 = datetime.datetime.strptime(t_stamp_2, "%a %d %b %Y %H:%M:%S  %z")
print(time_1, time_2)
t_delta = time_1 - time_2
print(abs(int(t_delta.total_seconds())))
#datetime instance attributes examples
print(time_1.year)
print(time_1.tzinfo)

