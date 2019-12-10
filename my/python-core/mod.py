#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mod.py - mod

# Date   : 2019/12/10
'''this is a test module'''

import sys
import os

debug = True

class FooClass(object):
    '''Foo Class'''
    pass


def test():
    '''test function'''
    foo = FooClass()
    if debug:
        print('run test()')


if __name__ == '__main__':
    test()
