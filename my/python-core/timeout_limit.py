#!/usr/bin/env python
# -*- coding: utf-8 -*-

# timeout_limit.py - timeout_limit

# Date   : 2019/12/13
import signal
from functools import wraps


class TimeoutException(Exception):
    def __init__(self, error = 'Timeout'):
        Exception.__init__(self, error)


def timeout_limit(timeout_time):
    def wrapper(func):
        def handler(signum, frame):
            raise TimeoutException(error='%s Timeout %d' %
                                   (func.__name__, timeout_time))

        @wraps(func)
        def deco(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout_time)
            func(*args, **kwargs)
            signal.alarm(0)
        return deco
    return wrapper


import time
@timeout_limit(3)
def test():
    time.sleep(1)

test()
