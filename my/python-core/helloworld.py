#!/usr/bin/env python
# -*- coding: utf-8 -*-

# helloworld.py - helloworld

# Date   : 2019/12/09
import sys

# print
msg = 'hello world!'
print(msg)
print('%s %d' % ('abc', 123))
print("hello", file=sys.stderr, flush=True)

# file
logfile = open('/tmp/abc', 'a')
print('hello world', file=logfile, flush=True)
logfile.close()


# input
user = input('Enter login name:')
print(user)
