#!/usr/bin/env python
# -*- coding: utf-8 -*-

# prodcons.py - prodcons

# Date   : 2019/12/21
from random import randint
from time import sleep
from queue import Queue
import threading


def writeQ(queue):
    print('producing object for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


def readQ(queue):
    _ = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []

    for i in nfuncs:
        t = threading.Thread(target=funcs[i],
                             args=(q, nloops))
        threads.append(t)
        t.start()
    for i in nfuncs:
        threads[i].join()

    print('all DONE')


if __name__ == '__main__':
    main()
