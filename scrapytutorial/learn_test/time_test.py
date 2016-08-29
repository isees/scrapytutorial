import time
import datetime
from time import gmtime, strftime

thatDay = datetime.datetime.strptime('2016-08-13', '%Y-%m-%d')

for days in range(8):
    currentDay = thatDay + datetime.timedelta(days=days)
    days += 1
    timeArray = time.mktime(currentDay.timetuple())
    print currentDay, currentDay.weekday() + 1, int(timeArray)

millis = int(round(time.time() * 1000))
print millis


def get_current_timestamp():
    return int(round(time.time()))


def int_to_time(ten_digit_number):
    return datetime.datetime.fromtimestamp(ten_digit_number)


date = int_to_time(1471536000)
print '1471536000 >> %r' % date
print 'Current timestamp >> %r' % get_current_timestamp()
print 'Current time >> %r' % int_to_time(get_current_timestamp())
print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print time.strftime('%Y-%m-%d %H:%M:%S')
