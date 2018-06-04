#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: sleep

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/30 17:35:48 liyunteng>

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads=[]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()


    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
