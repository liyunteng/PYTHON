#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: udp server

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 18:34:23 liyunteng>

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message ...')
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(),
                                         data.decode('utf-8')), 'utf-8'), addr)
    print('recived from and returned to: ', addr)

udpSerSock.close()
