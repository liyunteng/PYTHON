#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description:

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/26 03:06:41 liyunteng>

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

SMTPHOST = 'smtp.163.com'
username = 'li_yunteng@163.com'
passwd = 'xxx'                  # 163邮箱为smtp的授权码

sender = 'li_yunteng@163.com'
recivers = ['li_yunteng@163.com']

image = "/home/lyt/Pictures/a.png"

# multipart alternative: text and html
def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n', 'plain')
    email.attach(text)
    html = MIMEText('<html><body><h4>Hello World!</h4></body></html>', 'html')
    email.attach(html)
    return email

# multipart: images
def make_img_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition',
                     'attachment; filename="%s"' % fn)
    return email

def sendMsg(fr, to, msg):
    s = SMTP(SMTPHOST)
    s.login(username, passwd)
    errs = s.sendmail(fr, to, msg)
    s.quit

if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()
    msg['From'] = sender
    msg['To'] = ', '.join(recivers)
    msg['Subject'] = 'multipart alternative test'
    sendMsg(sender, recivers, msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg(image)
    msg['From'] = sender
    msg['To'] = ', '.join(recivers)
    msg['Subject'] = 'image file test'
    sendMsg(sender, recivers, msg.as_string())
