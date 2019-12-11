#!/usr/bin/env python
# -*- coding: utf-8 -*-

# file.py - file

# Date   : 2019/12/09

try:
    f = open('file.py', 'r')
    for x in f:
        print(x, end='')
except IOError as e:
    print(e)
finally:
    f.close()
