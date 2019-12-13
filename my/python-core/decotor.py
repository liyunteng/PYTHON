#!/usr/bin/env python
# -*- coding: utf-8 -*-

# decotor.py - decotor

# Date   : 2019/12/13
import time
from functools import wraps, partial


def run_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('%s => [%f]' % (func.__name__,
                              end_time - start_time))
    return wrapper


def run_time1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('%s => [%f]'% (func.__name__,
                             end_time - start_time))
    return wrapper


def run_time2(content):
    def wrapper1(func):
        @wraps(func)            # update func.__name__ ...
        def wrapper2(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('%s => [%f] %s' % (func.__name__,
                                     end_time - start_time,
                                     content))
        return wrapper2
    return wrapper1


class DelayFunc:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        print('DelayFunc %s' % self.func.__name__)
        return self.func(*args, **kwargs)


class DelayFunc1:
    def __init__(self, duration):
        self.duration = duration

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('DelayFunc1 %s %d' % (func.__name__, self.duration))
            time.sleep(self.duration)
            func(*args, **kwargs)
        return wrapper

class DelayFunc2:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        print('DelayFunc2 %s %d' % (self.func.__name__, self.duration))
        time.sleep(self.duration)
        return self.func(*args, **kwargs)


def delay(duration):
    return partial(DelayFunc2, duration)


instances = {}
def singleton(cls):
    def get_instance(*args, **kwargs):
        cls_name = cls.__name__
        print('-- 1 --')
        if not cls_name in instances:
            print('-- 2 --')
            instance = cls(*args, **kwargs)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance

@run_time
def test1():
    print('test1')

@run_time1
def test2(a):
    time.sleep(a)
    print('test2')

@run_time2('hello')
@delay(1)
@DelayFunc
@DelayFunc1(1)
def test3(a, b):
    time.sleep(a)
    time.sleep(b)
    print('test3')

@singleton
class Test4:
    _instance = None

    def __init__(self, name):
        print('==== new instance =====')
        self.name = name


test1()
test2(1)
test3(1, 2)
t = Test4('lyt')
t = Test4('abc')
t.name

##########################

def logged(when):
    def log(f, *args, **kwargs):
        print('''Called: \nfunction: %s\nargs: %r\nkwargs: %r''' % (f, args, kwargs))

    def pre_logged(f):
        def wrapper(*args, **kwargs):
            log(f, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kwargs):
            now = time.time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print('time delta: %s' % (time.time() - now))
        return wrapper

    try:
        return {"pre": pre_logged,
                "post": post_logged}[when]
    except KeyError as e:
        raise ValueError(e)

@logged('post')
def hello(name):
    print('hello %s' % name)

hello('world')
