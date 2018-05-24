#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: udp client

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 18:33:37 liyunteng>
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
