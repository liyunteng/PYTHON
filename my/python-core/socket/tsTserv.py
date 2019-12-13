#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tsTserv.py - tsTserv

# Date   : 2019/12/13
import socket
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print('waitting for connection ...')
    tcpCliSock, addr = tcpServSock.accept()
    print('%s:%d connected' % (addr[0], addr[1]) )

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        res = '[%s] %s' % (ctime(), data.decode('utf-8'))
        tcpCliSock.send(res.encode('utf-8'))

    print('%s:%d disconnect' % (addr[0], addr[1]))
    tcpCliSock.close()

tcpServSock.close()
