import time
import datetime

thatDay = datetime.datetime.strptime('2016-08-13', '%Y-%m-%d')

for days in range(5):
    currentDay = thatDay + datetime.timedelta(days=days)
    days += 1
    timeArray = time.mktime(currentDay.timetuple())
    print currentDay, currentDay.weekday() + 1, int(timeArray)