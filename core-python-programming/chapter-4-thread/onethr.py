#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: one thread

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/30 17:32:01 liyunteng>

from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('startint at:', ctime())
    loop0()
    loop1()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
