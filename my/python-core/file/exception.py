#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exception.py - exception

# Date   : 2019/12/13

import os, socket, errno, types, tempfile

class NetworkError(IOError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class FileError(IOError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

def fileArgs(file, mode, args):
        perms = ''
        permd = {'r': os.R_OK,
                 'w': os.W_OK,
                 'x': os.X_OK}
        pkeys = permd.keys()
        sorted(pkeys)
        reversed(pkeys)

        for p in 'rwx':
            if os.access(file, permd[p]):
                perms += p
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args.args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % (mode, myargs[1], perms)

        myargs.append(args.filename)
        return tuple(myargs)

def myConnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error as args:
        v = []
        v.extend([arg for arg in args.args])
        v[1] = "%s %s:%d"  % (v[1], host, port)
        raise NetworkError(tuple(v))

def myOpen(file, mode='r'):
    try:
        fo = open(file, mode)
    except IOError as args:
        raise FileError(fileArgs(file, mode, args))

    return fo


def testFile():
    file = tempfile.mktemp()
    f = open(file, 'w')
    f.close()

    for x in ((0, 'r'),(100, 'r'),(400, 'w'), (500, 'w')):
        try:
            os.chmod(file, x[0])
            f = myOpen(file, x[1])
        except FileError as e:
            print('%s: %s' % (e.__class__.__name__, e))
        else:
            print('file opened opk ... perm ignored')

        f.close()
    os.chmod(file, 777)
    os.unlink(file)


def testNet():
    for x in ('www.baidu.com', 'www.google.com'):
        s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
        try:
            myConnect(s, x, 80)
        except NetworkError as e:
            print('%s: %s' % (e.__class__.__name__, e))
        finally:
            s.close()

testFile()
testNet()
