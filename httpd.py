#!/usr/bin/env python
# -*- coding: utf-8 -*-

# httpd.py - httpd

# All rights reserved.

import os
import shutil
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

hosts = []


@app.route('/list', methods=['GET'])
@app.route('/list/<uid>', methods=['GET'])
def listFile(uid=None):
    files = []
    if uid is not None:
        if os.path.exists(uid):
            files = os.listdir(os.path.abspath(uid))
        return jsonify(files)
    else:
        files = os.listdir(os.path.abspath('.'))
        return jsonify(files)


@app.route('/delete/<uid>', methods=['GET'])
@app.route('/delete/<uid>/<filename>', methods=['GET'])
def delFile(uid, filename=None):
    print('delete %s %s' % (uid, filename))
    if not os.path.exists(uid):
        abort(404)

    if filename is not None:
        filepath = os.path.join(os.path.abspath(uid), filename)
        try:
            os.unlink(filepath)
            return jsonify('ok')
        except Exception as e:
            print(e)
            abort(404)
    else:
        try:
            shutil.rmtree(os.path.abspath(uid))
            return jsonify('ok')
        except Exception as e:
            print(e)
            abort(404)


@app.route('/upload/<uid>/<filename>', methods=['POST'])
def uploadFile(uid, filename):
    filepath = filename
    print(len(request.get_data()))

    if not os.path.exists(uid):
        os.mkdir(uid)

    filepath = os.path.join(os.path.abspath(uid), filename)
    with open(filepath, 'wb') as f:
        f.write(request.get_data())
    print('save to %s size %d' % (filepath, len(request.get_data())))
    return jsonify('ok')


@app.route('/download/<uid>/<filename>', methods=['GET'])
def downloadFile(uid, filename):
    filepath = filename
    if not os.path.exists(uid):
        abort(404)

    filepath = os.path.join(os.path.abspath(uid), filename)
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except Exception as e:
        print(e)
        abort(404)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.environ['REQUEST_METHOD'] == 'POST':
        # print(request.get_json())
        print(request.get_data())

    host = {
        'host': request.environ['REMOTE_ADDR'],
        'port': request.environ['REMOTE_PORT'],
        'method': request.environ['REQUEST_METHOD'],
        'uri': request.environ['REQUEST_URI'],
        'agent': request.environ["HTTP_USER_AGENT"],
        'url': request.url
    }

    hosts.append(host)
    print(hosts)
    return jsonify(hosts=hosts)


@app.route('/liveId', methods=['GET', 'POST'])
def liveId():
    reply = {
        'liveId': 'abcdefg',
        'iceAddr': 'turn:118.89.227.65:3478',
        'signalAddr': 'ws://52.81.24.35:18888'
        # 'signalAddr': 'ws://118.89.227.65:8015'
        # 'signalAddr': 'ws://127.0.0.1:12345'
    }
    return jsonify(reply)


@app.route('/device/123456789', methods=['GET', 'POST'])
def device():
    _ = {
        'Key': 'value'
    }
    print(request)


def main():
    # app.run(host='0.0.0.0', port=443, debug=True,
    #         ssl_context=('/Users/yli/ca/cert.crt',
    #                      '/Users/yli/ca/rsa_private.key'))
    # app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='0.0.0.0', port=80, debug=False)

# if __name__ == '__main__':
#     main()


main()
