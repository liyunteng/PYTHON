#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description:

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/30 17:59:07 liyunteng>

from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))

    print('*** SINGLE THREAD')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())


    print('\n*** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].name, ":", threads[i].getResult())

    print('all DONE')

main()
