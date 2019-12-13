#!/usr/bin/env python
# -*- coding: utf-8 -*-

# file.py - file

# Date   : 2019/12/13
import os

for tmpdir in ['/tmp', r'c:\temp']:
    if os.path.isdir(tmpdir):
        break
    else:
        print('no temp directory available')
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print('*** current directory is %s' % cwd)

    print('*** creating example directory ..')
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print('*** now working directory is %s' % cwd)
    print('*** origin directory listing: ')
    print(os.listdir(cwd))

    print('*** creating test file ...')
    with open('test', 'w') as f:
        f.write('foo\n')
        f.write('bar\n')

    print('*** upated directory listing: ')
    print(os.listdir(cwd))

    print('*** renaming "test" to "filetest.txt"')
    os.rename('test', 'filetest.txt')
    print('*** updated dirctory listing: ')
    print(os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print('** full file path')
    print(path)

    print('** (pathname, basename) == ')
    print(os.path.split(path))

    print('*** (filename, extension) == ')
    print(os.path.splitext(os.path.basename(path)))

    print('*** displaying file contents:')
    with open(path, 'r') as f:
        for x in f:
            print(x, end='')

    print('*** deleting test file')
    os.remove(path)
    print('*** updated directory listing:')
    print(os.listdir(cwd))
    os.chdir(os.pardir)

    print('*** deleting test directory')
    os.rmdir('example')
    print('*** Done')
