#!/usr/bin/env python
# -*- coding: utf-8 -*-

# insert_sort.py - insert_sort

# Date   : 2019/12/25
from random import randrange


def insert_sort_rec(seq, i):
    if i == 0 : return
    insert_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1


def insert_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1],seq[j] = seq[j], seq[j-1]
            j-=1
        print(seq)


l = [randrange(10 ** 3) for x in range(10)]
# l = [x for x in range(100)]
l = l[::-1]
print(l)
# insert_sort_rec(l, len(l)-1)
insert_sort(l)
print(l)
