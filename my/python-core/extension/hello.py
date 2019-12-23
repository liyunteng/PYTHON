#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hello.py - hello

# Date   : 2019/12/21
import ctypes
import struct

library = ctypes.cdll.LoadLibrary('/home/lyt/libhello.so')

library.hello()
print(library.fac(4))
print(library.fac(8))

# argument
library.test.argtype = [ctypes.c_int, ctypes.c_float, ctypes.c_char_p]
library.test.restype = ctypes.c_void_p
a = ctypes.c_int(10)
b = ctypes.c_float(12.34)
c = ctypes.c_char_p(b'fine, thank you')
library.test(a, b, c)

# struct
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
print('id =', x.contents.id,
      'name =', x.contents.name,
      'sex =', x.contents.sex,
      'next =', x.contents.next)

# callback
def callback(a, b):
    print('v1 =',a, 'v2 =', b)
    return a*b


c_callback = ctypes.CFUNCTYPE(ctypes.c_int,
                              ctypes.c_int,
                              ctypes.c_int)(callback)
print('idx =',library.register_callback(c_callback))
print('idx =',library.register_callback(c_callback))
print('idx =',library.register_callback(c_callback))
library.run_callback()

# struct + callback
class py_callback_all(ctypes.Structure):
    _fields_ = [
        ('callback1', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)),
        ('callback2', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)),
        ('callback3', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
    ]

def cb_1(a):
    print('cb_1:', a)
    return a * 1

def cb_2(a):
    print('cb_2:', a)
    return a * 2

def cb_3(a):
    print('cb_3:', a)
    return a * 3

cb_all = py_callback_all()
cb_all.callback1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(cb_1)
cb_all.callback2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(cb_2)
cb_all.callback3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(cb_3)
library.run_callback_all.argtypes = [py_callback_all]
library.run_callback_all(cb_all)
