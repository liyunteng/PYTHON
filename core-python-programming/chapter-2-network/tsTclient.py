#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: ts client

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 18:17:50 liyunteng>
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.send(bytes('', 'utf-8'))
tcpCliSock.close()
