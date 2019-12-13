#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http.py - http

# Date   : 2019/12/13

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


data = {'result' : 'this is a test'}
host = ('0.0.0.0', 8888)

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print('Starting server on %s:%d' % host)
    server.serve_forever()
