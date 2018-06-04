#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: lock

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/31 15:31:36 liyunteng>

from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = current_thread().name
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))

    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] Finished %s (%d secs)' % (ctime(), myname, nsec))
        print('(remaining: %s)' % (remaining or 'NONE'))


def _main():
    print('Starting at:', ctime())
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())

_main()
