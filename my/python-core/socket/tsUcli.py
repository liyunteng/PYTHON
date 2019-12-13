#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tsUcli.py - tsUcli

# Date   : 2019/12/13
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
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
