#!/usr/bin/env python
# -*- coding: utf-8 -*-

# makeTestFile.py - makeTestFile

# Date   : 2019/12/10
import os

ls = os.linesep


def makeFile():
    while True:
        fname = input('Enter filename:')
        if os.path.exists(fname):
            print('Error: "%s" already exists' % fname)
        else:
            break

    all = []
    print('Enter lines ("." by itself to quit).\n')

    while True:
        entry = input('> ')
        if entry == '.':
            break;
        else:
            all.append(entry)

    try:
        f = open(fname, 'w')
    except IOError as e:
        print('open file error: ' + e)
    else:
        f.writelines(['%s%s' % (x, ls) for x in all])
        f.close()

    try:
        f = open(fname, 'r')
    except IOError as e:
        print('file open error:' + e)

    else:
        for eachLine in f:
            print(eachLine, end='')
        f.close()
