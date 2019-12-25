#!/usr/bin/env python
# -*- coding: utf-8 -*-

# select_sort.py - select_sort

# Date   : 2019/12/25
from random import randrange


def select_sort_rec(seq, i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    select_sort_rec(seq, i-1)


def select_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]
        print(seq)


l = [randrange(10 ** 3) for x in range(10)]
# l = [x for x in range(100, 0, -1)]
print(l)
# select_sort_rec(l, len(l)-1)
select_sort(l)
print(l)
