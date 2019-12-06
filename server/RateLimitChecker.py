'''
checkRatelimit.py
check a rate limit of Twitter API.
If use of API is over the rate limit, return True.
Else use of API is under the rate limit, return False.

In the end of codes, this refresh conf.py about the rate limit.
'''
from conf import rate_status
from util import makeDict2json
from util import isDatetimeFormat, makeDatetime2string
import datetime as dt

class RateLimitChecker(object):
    def __init__(self, status):
        return self.initRateStatus(status)

    def __call__(self):
        return self.refreshRateStatus():

    def initRateStatus(self, status):
        self.limit = status['limit']
        self.current = status['current']
        if not isDatetimeFormat(status['start']):
            now = dt.datetime.now()
            status['start'] = makeDatetime2string(now)
        self.start = status['start']
        self.interval = status['interval']

    def refreshRateStatus(self):
        if not isDatetimeFormat(self.start):
            raise Exception('start time is not datetime format.')
        else:
            now = dt.datetime.now()
            elapsed_time = now - self.start
            if elapsed_time.seconds > self.interval:
                self.start = makeDatetime2string(now)
                self.current = 0
            if self.current < self.limit:
                self.current += 1

    def writeRateStatus(self, path):
        status = {
            'limit' : self.limit,
            'current' : self.current,
            'start' : self.start,
            'interval' : self.interval
        }
        makeDict2json(status, path)
        
    def isOverRateLimit(self):
        return self.current'] >= self.limit']


if __name__ == '__main__':
    checkRatelimit()