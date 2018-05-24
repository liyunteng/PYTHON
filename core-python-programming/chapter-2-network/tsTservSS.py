#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: SocketServerTCP

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 20:24:07 liyunteng>


from socketserver import TCPServer, StreamRequestHandler
from time import ctime


HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print('connected from: ', self.client_address)
        self.wfile.write(bytes('[%s] %s' % (ctime(),
                                            self.rfile.readline()), 'utf-8'))


tcpServ = TCPServer(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
