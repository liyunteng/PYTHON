#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tsUserv.py - tsUserv

# Date   : 2019/12/13
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpServSock = socket(AF_INET, SOCK_DGRAM)
udpServSock.bind(ADDR)

while True:
    print('waiting for message ...')
    data, addr = udpServSock.recvfrom(BUFSIZE)
    res = '[%s] %s' % (ctime(), data.decode('utf-8'))
    udpServSock.sendto(res.encode('utf-8'), addr)

udpServSock.close()
