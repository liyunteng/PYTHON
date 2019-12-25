#!/usr/bin/env python
# -*- coding: utf-8 -*-

# stupid_sort.py - stupid_sort

# Date   : 2019/12/24
from random import randrange
import cProfile

l = [randrange(10 ** 4) for i in range(100)]

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


print(l)
# cProfile.run('gnomesort(l)')
# print(l)

cProfile.run('s=mergesort(l)')
print(s)
