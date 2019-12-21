'''
checkRatelimit.py
check a rate limit of Twitter API.
If use of API is over the rate limit, return True.
Else use of API is under the rate limit, return False.

In the end of codes, this refresh conf.py about the rate limit.
'''
from conf import rate_status_init, datetime_format
from util import makeDict2json
from util import isDatetimeFormat, makeDatetime2string
import datetime as dt

class RateLimitChecker(object):
    def __init__(self, status):
        self.initRateStatus(status)

    def __call__(self):
        self.refreshRateStatus()

    def values(self):
        return {
            'limit' : self.limit,
            'current' : self.current,
            'start' : self.start,
            'interval' : self.interval
        }

    def initRateStatus(self, status):
        self.limit = status['limit']
        self.current = status['current']
        if not isDatetimeFormat(status['start']):
            self.start = dt.datetime.now()
        else:
            self.start = dt.datetime.strptime(status['start'], datetime_format)
        self.interval = status['interval']

    def refreshRateStatus(self):
        if not isinstance(self.start, dt.datetime):
            raise Exception('start time is not datetime format.')
        else:
            now = dt.datetime.now()
            elapsed_time = now - self.start
            if elapsed_time.seconds > self.interval:
                self.start = now
                self.current = 0
            if self.current < self.limit:
                self.current += 1
            else:
                print(f'current:{self.current} is over the limit:{self.limit}.')

    def writeRateStatus(self, path):
        status = {
            'limit' : self.limit,
            'current' : self.current,
            'start' : dt.datetime.strftime(self.start, datetime_format),
            'interval' : self.interval
        }
        makeDict2json(status, path)
        
    def isOverRateLimit(self):
        return self.current >= self.limit


def _test():
    # init test
    status = rate_status_init
    print('# init test')
    print('init status is', status)
    checker = RateLimitChecker(status)
    print('checker.values is', checker.values())

    # call test
    print('# call test')
    print('status before refresh', checker.values())
    for _ in range(10):
        checker.refreshRateStatus()
    print('status after refresh', checker.values())

    # rate check
    print('# rate check')
    print('checker.isOverRateLimit', checker.isOverRateLimit())

    # output test
    print('# output test')
    checker.writeRateStatus('rate_status.json')


if __name__ == '__main__':
    _test()