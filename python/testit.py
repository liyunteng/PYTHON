#!/usr/bin/env python

def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as e:
        result = (False, str(e))
    return result

def test():
    funcs = (int, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print('-'*20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print('%s(%s) = ' % (eachFunc.__name__, str(eachVal)), retval[1])
            else:
                print('%s(%s) = ' % (eachFunc.__name__, str(eachVal)), retval[1])

if __name__ == '__main__':
   test()                