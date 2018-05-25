#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: sendmail by smtp, recvmail by pop3

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/26 03:03:43 liyunteng>

from smtplib import SMTP
from poplib import POP3
from email.header import Header
from email.mime.text import MIMEText
from email.parser import Parser
from email.header import decode_header


SMTPHOST = 'smtp.163.com'
POPHOST = 'pop.163.com'

username = 'li_yunteng@163.com'
password = 'yun1988'                # 163邮箱为smtp授权码

# smtp
sender = 'li_yunteng@163.com'
receivers = ['li_yunteng@163.com']
subject = 'test msg'
content = 'this is from python.'

def sendEmail(sender, receivers,
              subject='', content=''):

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = '{}'.format(sender)
    msg['To'] = ','.join(receivers)
    msg['Subject'] = subject

    try:
        svr = SMTP(SMTPHOST)
        # svr.set_debuglevel(1)
        svr.login(username, password)
        svr.sendmail(sender, receivers, msg.as_string())
    except Exception as e:
        svr.quit()
        print('Error: %s' % e)


# pop
def recvEmail():
    try:
        svr = POP3(POPHOST)
        # svr.set_debuglevel(1)
        svr.user(username)
        svr.pass_(password)
        ret = svr.stat()

        rsp, lines, octets = svr.retr(ret[0])
        # rsp, lines, octets = svr.retr(1395)
        print(ret)
        # print(lines)

        content = b'\r\n'.join(lines).decode()
        msg = Parser().parsestr(content)
        print_mail(msg)
    except Exception as e:
        print('Error: %s' % e)
        svr.quit()

def print_mail(msg, multi=False):
    # print(msg)
    if not multi:
        for header in ['From', 'To', 'Subject', 'Date']:
            val = msg.get(header, '')
            if val:
                val, charset = decode_header(val)[0]
                if charset:
                    val = val.decode(charset)
            print(header + ': ' + val)

    # content_type = msg.get('Content-Type')
    content_type = msg.get_content_type()
    print('Content-Type: ' + content_type)

    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('part %s' % n)
            print('----------')
            print_mail(part, True)

    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # encoding = msg.get('Content-Transfer-Encoding')
            # print("encoding: %s" % encoding)
            content = msg.get_payload(decode=True)
            print()
            print(content)
        else:
            content = msg.get_payload()
            print()
            print(content)



if __name__ == '__main__':
    # sendEmail(username, receivers, subject, content)
    recvEmail()
