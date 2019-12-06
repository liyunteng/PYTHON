#!/usr/bin/env python
# -*- coding: utf-8 -*-

# httpd.py - httpd

# All rights reserved.

from flask import Flask, jsonify, request

app = Flask(__name__)

hosts = []
@app.route('/', methods=['GET', 'POST'])
def index():
    host = {
        'host': request.environ['REMOTE_ADDR'],
        'port': request.environ['REMOTE_PORT'],
        'method': request.environ['REQUEST_METHOD'],
        'uri': request.environ['REQUEST_URI'],
        'agent': request.environ["HTTP_USER_AGENT"],
        'url': request.url
    }
    hosts.append(host)
    return jsonify(hosts=hosts)


def main():
    app.run(host='0.0.0.0', port=12345, debug=True)


if __name__ == '__main__':
    main()
