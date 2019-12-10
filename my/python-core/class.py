#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class.py - class

# Date   : 2019/12/10


class FooClass(object):
    '''my very first class: FooClass'''
    version = 0.1               # class (data) attribute

    def __init__(self, nm = 'John Doe'):
        '''constructor'''
        self.name = nm
        print('Created a class instance for %s' % nm)

    def showname(self):
        '''display instance attribute and class name'''
        print('Your name is %s' % self.name)
        print('My name is %s' % self.__class__.__name__)

    def showver(self):
        '''display class(static) attribute'''
        print(self.version)

    def addMe2Me(self, x):
        '''apply + operator to argument'''
        return x+x


f = FooClass('lyt')
f.showname()
f.showver()
f.addMe2Me(2)
