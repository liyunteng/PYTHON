#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lambda.py - lambda

# Date   : 2019/12/13

(lambda x, y : x ** y)(2, 2)

a = lambda x, y: x + y
a(1, 1)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = filter(lambda x: x % 2 == 0, l)
for x in a:
    print(x)
print()

a = map(lambda x : 2 * x, l)
for x in a:
    print(x)

print()
from operator import add, mul, sub
from functools import partial

add1 = partial(add, 1)
mul1 = partial(mul, 2)
sub1 = partial(sub, 1)          # ?? how to x - 1 ??
baseTwo = partial(int, base=2)
print(add1(1))
print(mul1(2))
print(baseTwo('1000'))
print(sub1(4))
