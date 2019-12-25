#!/usr/bin/env python
# -*- coding: utf-8 -*-

# celeb.py - celeb

# Date   : 2019/12/25
from random import randrange


def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u
    return None


def celeb(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2, n+1):
        if G[u][v]: u = c
        else:       v = c
    if u == n:      c = v
    else:           c = u
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None


n = 10
l = [[randrange(2) for x in range(n)] for x in range(n)]
# c = randrange(n)
c = n // 2
for i in range(n):
    l[i][c] = 1
    l[c][i] = 0
for x in l:
    print(x)
#x = naive_celeb(l)
x = celeb(l)
print(x)
