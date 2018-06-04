#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: threading with class

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/30 17:59:45 liyunteng>

import threading
from time import ctime, sleep

loops = [4, 2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())

    def getResult(self):
        return self.res


def loop(nloop, nsec):
    sleep(nsec)

def main():
    print('starting at:',ctime())
    threads = []
    nloops = range(len(loops))


    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)


    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
