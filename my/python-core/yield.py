#!/usr/bin/env python
# -*- coding: utf-8 -*-

# yield.py - yield

# Date   : 2019/12/12
import select
import socket


def corountine():
    sock = socket.socket()
    sock.setblocking(0)
    print(1)
    address = yield sock
    print(address)
    print(2)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    print(3)
    data = yield
    print(4)
    size = yield sock.send(data)
    print(5)
    yield sock.recv(size)
    print(6)


def main():
    coro = corountine()
    print('#')
    sock = coro.send(None)
    print('##')
    wait_list = (sock.fileno(),)
    print('###')
    coro.send(('www.baidu.com', 80))
    print('#' * 4)
    select.select((), wait_list, ())
    print('#' * 5)
    coro.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: Close\r\n\r\n')
    print('#' * 6)
    select.select(wait_list, (), ())
    print('#' * 7)
    print(coro.send(40960))
    print('#' * 8)


main()
