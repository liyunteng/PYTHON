#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: amazon bookmark

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/31 15:06:45 liyunteng>

from atexit import register
from threading import Thread
from time import ctime
import re
import urllib3

urllib3.disable_warnings()
REGEX = re.compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

pm = urllib3.PoolManager()
def getRanking(isbn):
    page = pm.urlopen('GET', '%s%s' % (AMZN, isbn))
    page.close()
    data = page.data.decode()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print('- %s ranked %s' % (ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        # _showRanking(isbn)
        Thread(target=_showRanking, args=(isbn,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
