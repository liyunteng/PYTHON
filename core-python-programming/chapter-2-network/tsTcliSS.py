#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: SocketServerTCP client

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 20:27:19 liyunteng>

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes('%s\r\n' % data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.strip().decode('utf-8'))
    tcpCliSock.close()
