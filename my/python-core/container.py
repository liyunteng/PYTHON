#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list.py - list

# Date   : 2019/12/09

# list
aList = [1, 2, 3, 4, 'abc']
print(aList)
print(aList[0])
print(aList[2:])
print(aList[:-1])
print(aList[0:])

# tuple
aTuple = ('robots', 77, 93, 'try')
print(aTuple)
print(aTuple[:3])

# dict
aDict = {'host': 'earth'}
print(aDict)
aDict['port'] = 80
print(aDict)
print(aDict.keys())
print(aDict.values())
