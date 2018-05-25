#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: download from ftp server

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/25 23:32:08 liyunteng>

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/firefox/releases/latest'
FILE = 'xxx.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)


    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')


    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed to "%s"' % DIRN)


    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)

    else:
        print('*** Download "%s" to CWD' % FILE)

    f.quit()

if __name__ == '__main__':
    main()
