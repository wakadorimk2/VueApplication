'''
checkRatelimit.py
check a rate limit of Twitter API.
If use of API is over the rate limit, return True.
Else use of API is under the rate limit, return False.

In the end of codes, this refresh conf.py about the rate limit.
'''
from conf import rate_status
import datetime as dt

def checkRatelimit(status):
    now = dt.datetime.now()
    diff = now - status['started']
    if diff.seconds > 60:
    return answer

if __name__ == '__main__':
    checkRatelimit()