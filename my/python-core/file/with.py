#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with.py - with

# Date   : 2019/12/13
class Mycontext():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')
        print(exc_type, exc_value)

    def do(self):
        print(self.name)
        # a


def test():
    with Mycontext('abc') as mc:
        mc.do()


test()
