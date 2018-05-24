#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: gen data

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/21 19:10:24 liyunteng>

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxunicode
from time import ctime

import sys
tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(maxunicode)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
                                      dom, choice(tlds),
                                      dtint, llen, dlen))

print(sys.version_info)
print(sys.ps1)
