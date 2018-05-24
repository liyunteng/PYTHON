#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: practice

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 17:19:48 liyunteng>

import re

# 1-1
data = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
for x in data:
    m = re.match('[bh][aiu]t', x)
    print(m.group())

# 1-2
data = ['Li Yunteng', 'Ma Huateng', 'Ma Yun', 'Li Yanhong']
for x in data:
    m = re.match('(\w+) (\w+)', x)
    print(m.groups())

# 1-6
data = ['http://www.baidu.com', 'https://www.baidu.com',
        'https://www.qq.com', 'http://www.163.com',
        'http://www.peking.edu', 'https://www.org.net',
        'http://www.abc.edu.cn', 'https://www.abc.xxx.com']
for x in data:
    m = re.match('http[s]?://www.(\w+)\..*(com|edu|net)', x)
    if m is not None:
        print(m.group(), m.groups())

# 1-11
data = ['liyunteng@gmail.com',
        'li_yunteng@163.com',
        'liyutneng@streamocean.com',
        'liyunteng@jlu.edu.cn',
        '123@gmail.com']
for x in data:
    m = re.match('(\w+)@(\w+)(\.\w+)+', x)
    if m is not None:
        print(m.group(), m.groups())
