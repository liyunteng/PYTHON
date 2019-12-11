#!/usr/bin/env python
# -*- coding: utf-8 -*-

# displayNumberType.py - displayNumberType

# Date   : 2019/12/10

def displayNumberType(num):
    print(str(num) + ' is ', end='')
    if isinstance(num, (int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all!')


displayNumberType(-69)
displayNumberType(9999999999999999999)
displayNumberType(98.6)
displayNumberType(-5.2+1.9j)
displayNumberType('xxx')
