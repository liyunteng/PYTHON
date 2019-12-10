#!/usr/bin/env python
# -*- coding: utf-8 -*-

# loop.py - loop

# Date   : 2019/12/09

flag = 0
# if
if True:
    print(bool(1))

if flag:
    print(bool(flag))
else:
    print(bool(flag))

if flag:
    print(bool(flag))
elif not flag:
    print(bool(flag))


# while
while not flag:
    print(flag)
    flag += 1

# for
l = [1, 2, 3, 4]
for x in l:
    print(x)

for x in range(1, 10):
    print(x)

s = 'abcdefgh'
for x in s:
    print(x)

for i, v in enumerate(s):
    print(i, v)


#
s = [x ** 2 for x in range(10)]
print(s)
s = [x ** 2 for x in range(10) if not x % 2]
print(s)
