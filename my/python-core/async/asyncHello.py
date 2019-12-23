#!/usr/bin/env python
# -*- coding: utf-8 -*-

# asyncHello.py - asyncHello

# Date   : 2019/12/12
import threading
import asyncio


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


async def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break;
        # print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    print('wget %s done! (%s)' % (host, threading.currentThread()))
    writer.close()
    # reader.close()


hosts = [
    'www.sina.com.cn',
    'www.baidu.com',
    'www.sohu.com',
    'www.163.com'
]
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
tasks += [wget(host) for host in hosts]
loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
