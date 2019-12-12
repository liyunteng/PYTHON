#!/usr/bin/env python
# -*- coding: utf-8 -*-

# asyncWeb.py - asyncWeb

# Date   : 2019/12/12
import asyncio
import time
import aiohttp
import async_timeout

msg = "http://www.ngchina.com.cn/photography/photo_of_the_day/{}.html"

urls = [msg.format(i) for i in range(4500, 4600)]


async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return response.status


async def main(url):
    async with aiohttp.ClientSession() as session:
        status = await fetch(session, url)
        return status

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [main(url) for url in urls]
    status_list = loop.run_until_complete(asyncio.gather(*tasks))
    # print(status_list)
    print(len([status for status in status_list if status == 200]))
    end = time.time()
    print("cost time:", end - start)
