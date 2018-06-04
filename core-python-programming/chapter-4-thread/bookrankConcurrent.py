#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: book rank with concurrent

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/31 19:07:05 liyunteng>

import re
from concurrent.futures import ThreadPoolExecutor
from time import ctime
from urllib.request import urlopen
import urllib3

urllib3.disable_warnings()
pm = urllib3.PoolManager()
REGEX = re.compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    # print('{0}{1}'.format(AMZN, isbn))
    page = pm.urlopen('GET', '{0}{1}'.format(AMZN, isbn))
    page.close()
    return REGEX.findall(page.data.decode())
    # page = urlopen('{0}{1}'.format(AMZN, isbn), timeout=60)
    # # print(page.read())
    # page.close()
    # # return REGEX.findall(page.read())[0]


def _main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(len(ISBNs)) as executor:
        for isbn, ranking in zip(
                ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s' % (ISBNs[isbn], ranking))
    print('all DONE at:', ctime())

_main()
