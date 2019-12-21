#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mail.py - mail

# Date   : 2019/12/21
import smtplib
import imaplib
import os
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

smtp_host = 'smtp.163.com'
smtp_port = 25
smtp_user = 'li_yunteng'
smtp_pass = 'xxxxxx'

imap_host = "imap.163.com"
imap_port = 143
imap_user = 'li_yunteng'
imap_pass = 'xxxxxx'

sender = 'li_yunteng@163.com'
recivers = ['liyunteng@megarobo.tech', 'li_yunteng@163.com']
cc = ['liyunteng@gmail.com']

def sendmail():
    content1 = '''
    <p>This is a test from Python use smtplib ...</p>
    <p><a href="http://www.baidu.com">This is a link</a></p>
    <p><img src="cid:image1"></p>
    '''
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(recivers)
    msg['Cc'] = ','.join(cc)
    msg['Subject'] = 'Python SMTP Test2'
    msg['Date'] = formatdate()
    body1 = MIMEText(content1, 'html', 'utf-8')
    msg.attach(body1)

    fn1 = "/home/lyt/test.json"
    with open(fn1, 'rb') as f:
        fn1content = f.read()
    a = MIMEText(fn1content, 'base64', 'utf-8')
    a['Content-Type'] = 'application/octet-stream'
    a['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(fn1))
    msg.attach(a)

    fn2 = "httpd.py"
    with open(fn2, 'rb') as f:
        fn2content = f.read()
    a2 = MIMEText(fn2content, 'base64', 'utf-8')
    a2['Content-Type'] = 'application/octet-stream'
    a2['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(fn2))
    msg.attach(a2)

    fn3 = '/home/lyt/Pictures/a.png'
    with open(fn3, 'rb') as f:
        fn3content = f.read()
    a3 = MIMEImage(fn3content)
    a3.add_header('Content-ID', '<image1>')
    msg.attach(a3)

    print(msg.as_string())
    try:
        s = smtplib.SMTP(smtp_host, smtp_port)
        s.login(smtp_user, smtp_pass)
        s.sendmail(sender, recivers, msg.as_string())
        print('send done')
    except smtplib.SMTPException as e:
        print('send faile {}', e)
    finally:
        s.close()


def recvmail():
    try:
        s = imaplib.IMAP4(imap_host, imap_port)
        s.login(imap_user, imap_pass)
        s.select()
        # type, data = s.search(None, 'ALL')
        count = len(s.search(None, 'ALL')[1][0].split())
        type, content= s.fetch(f'{count}'.encode(), '(RFC822)')
        print(type)
        content = content[0][1].decode()
        print(content)
    except Exception as e:
        print('recv faile {}', e)
    finally:
        s.close()
        s.logout()


#sendmail()
#recvmail()
