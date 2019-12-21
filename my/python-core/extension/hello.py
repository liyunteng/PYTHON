#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hello.py - hello

# Date   : 2019/12/21
import ctypes
import struct

library = ctypes.cdll.LoadLibrary('/home/lyt/libhello.so')

library.hello()
library.fac(4)
library.fac(8)

library.test.argtype = [ctypes.c_int, ctypes.c_float, ctypes.c_char_p]
library.test.restype = ctypes.c_void_p
a = ctypes.c_int(10)
b = ctypes.c_float(12.34)
c = ctypes.c_char_p(b'fine, thank you')
library.test(a, b, c)


class stu(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_int),
        ("name", ctypes.c_char * 128),
        ("sex", ctypes.c_int),
        ("next", ctypes.c_void_p)
    ]


s = stu()
s.id = 10
s.name = b'liyunteng'
s.sex = 1
s.next = 0
library.setTest(ctypes.byref(s))

library.getTest.restype = ctypes.POINTER(stu)
x = library.getTest(10)
print(x.contents.id,
      x.contents.name,
      x.contents.sex,
      x.contents.next)
