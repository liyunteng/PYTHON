#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test_lhs.py - test_lhs

# Author : liyunteng <liyunteng@streamocean.com>
# Date   : 2019/10/16

# Copyright (C) 2019 StreamOcean, Inc.
# All rights reserved.
import json
import time
import socket
import threading
from urllib import request


class httpClient:
    def __init__(self, url, timeout=10):
        self.url = url
        self.timeout = 10

    def get(self, url, timeout=20):
        try:
            req = request.Request(url)
            res = request.urlopen(req, timeout=timeout)
        except Exception as e:
            print(url + ' Exception: ' + str(e))
            return
        r = res.read().decode('utf-8')
        print(url + ' ==> response:' + r)
        return r

    def post(self, data_json, timeout=10):
        try:
            data = json.dumps(data_json).encode('utf-8')
        except Exception as e:
            print(e)
            return
        headers = {
            'Conetent-Type': 'application/json',
            'Connection': 'Closed'
        }
        try:
            req = request.Request(self.url, headers=headers, data=data)
            res = request.urlopen(req, timeout=timeout)
        except Exception as e:
            print(e)
            return
        # print(str(data) + '  ==> response:' + res.read().decode('utf-8'))
        try:
            output = json.loads(res.read().decode('utf-8'))
            print(data.decode() + '  ==> response:' + str(output))
        except Exception as e:
            print(e)
            return


class socketServer:
    def __init__(self, ip, port, callback=None):
        self.ip = ip
        self.port = port
        self.sock = 0
        self.clis = {}
        self.callback = callback

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        print('listen ' + self.ip + ':' + str(self.port))
        while True:
            try:
                c, addr = self.sock.accept()
                print('## [%s:%d] connected' % (addr[0], addr[1]))
                if (addr in self.clis):
                    print('duplicate clis')
                    continue
                else:
                    self.clis[addr] = c
                    if self.callback is not None:
                        self.callback(self, c, addr)

            except Exception as e:
                print(e)
                raise(e)

    def send(self, sock, addr, cmd):
        try:
            # print("[%s:%d] %-10s: " % (addr[0], addr[1], cmd), end='', flush=True)
            print('[%s:%d] <= %s' % (addr[0], addr[1], cmd))
            sock.send(cmd.encode('utf-8'))
            data = sock.recv(1024)
            print('[%s:%d] => %s' % (addr[0], addr[1], str(data.decode('utf-8'))))
        except Exception as e:
            # print(e)
            sock.close()
            del self.clis[addr]
            print("## [%s:%d] disconnected %s" % (addr[0], addr[1], e))
            raise(e)


def test1():
    h = httpClient('http://192.168.1.159:8081', 10)
    h.post({'action': 'logon'}, 60)
    time.sleep(2)
    h.post({'action': 'setRemoteMode', 'mode': 'on'})
    time.sleep(2)
    h.post({'action': 'sysInfo'})
    time.sleep(2)
    h.post({'action': 'status'})
    time.sleep(2)
    h.post({'action': 'init'})
    time.sleep(2)
    h.post({'action': 'loadScript', 'name': 'NewScript.esc'})
    time.sleep(2)
    h.post({'action': 'runScript'})
    time.sleep(2)
    h.post({'action': 'scriptStatus'})
    time.sleep(2)
    h.post({'action': 'lcInfo'})
    time.sleep(2)
    h.post({'action': 'rackInfo'})
    time.sleep(2)
    h.post({'action': 'addCarrier'})
    time.sleep(2)
    h.post({'action': 'deleteCarrier'})
    time.sleep(2)
    h.post({'action': 'addLabware'})
    time.sleep(2)
    h.post({'action': 'deleteLabware'})
    time.sleep(2)
    h.post({'action': 'setVariable', 'name': 'test', 'value': 15})
    time.sleep(2)
    h.post({'action': 'getVariable', 'name': 'test'})
    time.sleep(2)
    h.post({'action': 'stopScript'})
    time.sleep(2)
    h.post({'action': 'resumeScript'})
    # h.post({'action': 'pauseScript'})

    time.sleep(2)
    # h.post({'action': 'setDoorLock', 'mode': 'on'})
    h.post({'action': 'setDoorLock', 'mode': 'off'})
    h.post({'action': 'setLamp', 'mode': 1})
    h.post({'action': 'setLamp', 'mode': 2})
    h.post({'action': 'setLamp', 'mode': 3})
    time.sleep(2)
    h.post({'action': 'logoff'})


def connCallback(s, sock, addr):
    while True:
        try:
            time.sleep(3)
            s.send(sock, addr, 'getstatus')
            time.sleep(3)
            s.send(sock, addr, 'init')
            time.sleep(3)
            s.send(sock, addr, 'getstatus')
            time.sleep(3)
            s.send(sock, addr, 'run')
            time.sleep(3)
            s.send(sock, addr, 'getstatus')
            time.sleep(3)
            s.send(sock, addr, 'uninit')
        except Exception:
            return


threads = []


def socketConnectThread(s, sock, addr):
    t = threading.Thread(target=connCallback, args=(s, sock, addr), daemon=True)
    threads.append(t)
    t.start()


def test2():
    s = socketServer('0.0.0.0', 8090, socketConnectThread)
    t1 = threading.Thread(target=lambda x: x.start(), args=(s,), daemon=True)
    threads.append(t1)
    t1.start()
    t1.join()


def test3():
    h = httpClient('192.168.1.159', 44300)
    s = h.get('http://192.168.1.159:44300/api/Tecan/status')
    if s != "IDEL":
        h.get('http://192.168.1.159:44300/api/Tecan/uninit', timeout=60)
        s = h.get('http://192.168.1.159:44300/api/Tecan/status')

    if s == 'IDEL':
        h.get('http://192.168.1.159:44300/api/Tecan/init', timeout=60)
        s = h.get('http://192.168.1.159:44300/api/Tecan/status')

    if s == 'READY':
        h.get('http://192.168.1.159:44300/api/Tecan/run')
        time.sleep(1)
        s = h.get('http://192.168.1.159:44300/api/Tecan/status')

    if s == 'BUSY':
        while True:
            time.sleep(5)
            s = h.get('http://192.168.1.159:44300/api/Tecan/status')
            if s == 'READY':
                break

    if s == 'READY':
        h.get('http://192.168.1.159:44300/api/Tecan/uninit', timeout=60)
        s = h.get('http://192.168.1.159:44300/api/Tecan/status')


def main():
    test3()


if __name__ == '__main__':
    main()
