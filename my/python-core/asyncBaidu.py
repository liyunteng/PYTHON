#!/usr/bin/env python
# -*- coding: utf-8 -*-

# asyncBaidu.py - asyncBaidu

# Date   : 2019/12/12

from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import socket
from types import coroutine
from urllib.parse import urlparse

@coroutine
def until_readable(fileobj):
    yield fileobj, EVENT_READ

@coroutine
def until_writeable(fileobj):
    yield fileobj, EVENT_WRITE


async def connect(sock, address):
    try:
        sock.connect(address)
    except BlockingIOError:
        await until_writeable(sock)


async def recv(fileobj):
    result = b''
    while True:
        try:
            data = fileobj.recv(4096)
            if not data:
                return result
            result += data
        except BlockingIOError:
            await until_readable(fileobj)


async def send(fileobj, data):
    while data:
        try:
            send_bytes = fileobj.send(data)
            data = data[send_bytes:]
        except BlockingIOError:
            await until_writeable(fileobj)


async def fetch_url(url):
    parsed_url = urlparse(url)
    if parsed_url.port is None:
        port = 443 if parsed_url.scheme == 'https' else 80
    else:
        port = parsed_url.port

    with socket.socket() as sock:
        sock.setblocking(0)
        await connect(sock, (parsed_url.hostname, port))
        path = parsed_url.path if parsed_url.path else '/'
        path_with_query = '{}?{}'.format(path, parsed_url.query) if parsed_url.query else path
        await send(sock, 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: Close\r\n\r\n'.format(
            path_with_query, parsed_url.netloc).encode())
        content = await recv(sock)
        print('{}: {}'.format(url, content))


def main():
    urls = [
        'http://www.baidu.com/s?wd={}'.format(i) for i in range(10)
    ]
    tasks = [fetch_url(url) for url in urls]

    with DefaultSelector() as selector:
        while tasks or selector.get_map():
            events = selector.select(0 if tasks else 1)
            for key, event in events:
                task = key.data
                tasks.append(task)
                selector.unregister(key.fileobj)

            for task in tasks:
                try:
                    fileobj, event = task.send(None)
                except StopIteration:
                    pass
                else:
                    selector.register(fileobj, event, task)

            tasks.clear()


main()
