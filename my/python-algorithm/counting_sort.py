#!/usr/bin/env python
# -*- coding: utf-8 -*-

# counting_sort.py - counting_sort

# Date   : 2019/12/25
from collections import defaultdict
from random import randrange


def counting_sourt(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        B.extend(C[k])
    print(C)
    print(B)
    return B

# l = [x for x in range(10, 0, -1)]
l = [randrange(10 ** 2) for x in range(10)]
l.append(1)
l.append(2)
print(l)
r = counting_sourt(l)
