#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: ts Server

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 18:21:30 liyunteng>

from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' % (ctime(),
                                           data.decode('utf-8')), 'utf-8'))

    print('disconnect from:', addr)
    tcpCliSock.close()

tcpSerSock.close()
