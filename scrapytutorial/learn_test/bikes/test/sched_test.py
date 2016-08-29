import sched
import time
from threading import Timer


def print_time(num):
    print int(time.time()), "X - %d" % num


def print_some_times():
    num = 0
    s = sched.scheduler(time.time, time.sleep)
    while True:
        s.enter(1, 1, print_time, [num])
        s.run()
        num += 1


def print_some_y():
    while True:
        time.sleep(1)
        print '\nTick'
        time.sleep(1)
        print '\nTock'


Timer(0, print_some_times, ()).start()
Timer(0, print_some_y, ()).start()
