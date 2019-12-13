#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sockserver.py - sockserver

# Date   : 2019/12/13
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        if self.data is not None:
            print("%s:%d => %s" % (self.client_address[0],
                                   self.client_address[1],
                                   self.data.decode('utf-8')))
            self.request.sendall(self.data.upper())


if __name__ == '__main__':
    HOST, PORT = "localhost", 9999
    socketserver.TCPServer.allow_reuse_address = True
    # server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
