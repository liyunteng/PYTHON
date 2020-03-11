#!/usr/bin/env python
# -*- coding: utf-8 -*-

# gcd.py - gcd

# Date   : 2020/01/06
import random


def gcd(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a = b
        b = c

a = random.randrange(1, 10000)
b = random.randrange(1, 10000)
gcd(119, 544)
