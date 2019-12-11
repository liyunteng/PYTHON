#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in.py - built-in

# Date   : 2019/12/04


class Abs:
    def __init__(self, v):
        self.value = v

    def __abs__(self):
        if (self.value > 0):
            return self.value
        else:
            return -self.value


class Callable:
    def __init__(self):
        self.value = 100

    def __call__(self):
        print("running")

    @property
    def value(self):
        '''I'm the 'x' property.'''
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @value.deleter
    def value(self):
        del self._value

    @classmethod
    def classmethod(cls):
        print('Callable classmethod')

    @staticmethod
    def staticmethod():
        print('Callable staticmethod')


def testAbs():
    print('testAbs: ', abs(-3))
    a = Abs(-3)
    print('testAbs: ', abs(a))


def testAll():
    l1 = ['a', 'b', 'c']
    l2 = ['a', 'b', 'c', '']
    print('testAll: ', all(l1))
    print('testAll: ', all(l2))


def testAny():
    l1 = ['', '', '']
    l2 = ['a', '', '']
    print('testAny: ', any(l1))
    print('testAny: ', any(l2))


def testAscii():
    a = Abs(-3)
    print('testAscii: ', ascii(a))
    print('testAscii: ', repr(a))


def testBin():
    print('testBin: ', bin(15))
    print('testBin: ', format(15, '#b'))
    print('testBin: ', format(15, 'b'))


def testHex():
    print('testHex: ', hex(15))
    print('testHex: ', format(15, '#x'))
    print('testHex: ', format(15, 'x'))


def testOct():
    print('testOct: ', oct(15))
    print('testOct: ', format(15, '#o'))
    print('testOct: ', format(15, 'o'))


def testOrd():
    print('testOrd: ', ord('a'))
    print('testChr: ', chr(ord('a')))


def testBool():
    a = ''
    b = 'b'
    print('testBool: ', bool(a))
    print('testBool: ', bool(b))


def testBreakpoint():
    breakpoint()


def testCallable():
    Callable.classmethod()
    c = Callable()
    print('testCallable: ', callable(c))
    if (callable(c)):
        c()


def testCompile():
    exec(compile('print("Hello world!")', '', 'eval'))
    eval(compile('print("Hello world!")', '', 'eval'))


def testAttr():
    c = Callable()
    print('testAttr: ', hasattr(c, 'name'))
    setattr(c, 'name', 'c')
    print('testAttr: ', c.__dict__)
    print('testAttr: ', c.name)
    print('testAttr: ', hasattr(c, 'name'))
    delattr(c, 'name')
    print('testAttr: ', c.__dict__)
    print('testAttr: ', hasattr(c, 'name'))
    print('testAttr: ', dir(c))


def testDivmod():
    r = divmod(10, 3)
    print('testDivmod: ', r)


def testEnumerate():
    session = ['Spring', 'Summer', 'Fall', 'Winter']
    print('testEnumerate: ', list(enumerate(session, start=1)))


def testFilter():
    session = ['Spring', 'Summer', 'Fall', 'Winter', '']
    print('testFilter: ', list(filter(bool, session)))


def testMap():
    session = ['Spring', 'Summer', 'Fall', 'Winter']
    print('testMap: ')
    for var in map(print, session):
        var


def testEval():
    x = 1
    print('testEval: ', eval('x+1'))


def testExec():
    print('testExec: ', exec('print("Hello World")'))
    print('testExec: ', globals())
    print('testExec: ', locals())


def testFloat():
    print('testFloat: ', float('+1.23'))
    print('testFloat: ', float('  -12345\n'))
    print('testFloat: ', float('1e-003'))
    print('testFloat: ', float('-Infinity'))
    print('testFloat: ', float('nan'))


def testFormat():
    print('testFormat: ', '{0} {1} {2}'.format('a', 'b', 'c'))
    print('testFormat: ', '{} {} {}'.format('a', 'b', 'c'))
    print('testFormat: ', '{2} {1} {0}'.format('a', 'b', 'c'))
    print('testFormat: ', '{0} {1} {0}'.format('a', 'b', 'c'))
    print('testFormat: ', 'Cordinates: {latitude} {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print('testFormat: ', 'Cordinates: {latitude} {longitude}'.format(**coord))
    c = 3-5j
    print('testFormat: ', '{0} real: {0.real} imag: {0.imag}'.format(c))
    coord = (3, 5)
    print('testFormat: ', 'X: {0[0]} Y:{0[1]}'.format(coord))
    print('testFormat: ', 'repr() show quotes: {!r}; str() not: {!s}'.format('test1', 'test2'))

    print('testFormat: ', '{:<30}'.format('left aligned'))
    print('testFormat: ', '{:>30}'.format('right aligned'))
    print('testFormat: ', '{:^30}'.format('centered'))
    print('testFormat: ', '{:*^30}'.format('centered'))

    print('testFormat: ', '{:+f} {:+f}'.format(3.14, -3.14))
    print('testFormat: ', '{: f} {: f}'.format(3.14, -3.14))
    print('testFormat: ', '{:-f} {:-f}'.format(3.14, -3.14))

    print('testFormat: ', 'int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42))
    print('testFormat: ', 'int: {0:d}; hex:{0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42))

    print('testFormat: ', '{:,}'.format(123456789))
    print('testFormat: ', '{:.2%}'.format(19/22))

    import datetime
    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    print('testFormat: ', '{:%Y-%m-%d %H:%M:%S}'.format(d))

    from string import Template
    s = Template('$who like $what')
    print('testFormat: ', s.substitute(who='tim', what='kung pao'))
    d = dict(who='tim')
    print('testformat: ', Template('Give $who $100').safe_substitute(d))


def testHash():
    c = Callable()
    print('testHash: ', hash(1))
    print('testHash: ', hash(c))


def testId():
    c = Callable()
    print('testId: ', id(1))
    print('testId: ', id(c))


def testMax():
    n = [1, 2, 3, 4]
    print('testMax: ', max(n))
    print('testMax: ', max(1, 2, 3, 4))


def testMin():
    n = [1, 2, 3, 4]
    print('testMin: ', min(n))
    print('testMin: ', min(1, 2, 3, 4))


def testOpen():
    f = open('built-in.py', 'a')
    f.close()

    with open('built-in.py', 'a') as f:
        pass


def testPow():
    print('testPow: ', pow(2, 3))
    print('testPow: ', 2 ** 3)


def testVars():
    c = Callable()
    print('testVars: ', vars(c))
    print('testVars: ', dir(c))


def testZip():
    s1 = [1, 2, 3, 4]
    s2 = ['a', 'b', 'c']
    print('testZip: ', list(zip(s1, s2)))


def testImport():
    # import os
    os = __import__('os', globals(), locals(), [], 0)
    print('testImport: ', dir(os))


def main():
    print(dir(__builtins__))
    testAbs()
    testAll()
    testAny()
    testAscii()
    testBin()
    testHex()
    testOct()
    testOrd()
    testBool()
    testCallable()
    testCompile()
    testAttr()
    testDivmod()
    testEnumerate()
    testFilter()
    testMap()
    testEval()
    testExec()
    testFloat()
    testFormat()
    testHash()
    testId()
    testMax()
    testMin()
    testOpen()
    testPow()
    testVars()
    testZip()
    testImport()
    # testBreakpoint()


main()
