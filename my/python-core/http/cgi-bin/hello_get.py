#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test.py - test

# Date   : 2019/12/13
import os
import cgi

form = cgi.FieldStorage()
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print('Content-Type: text/html')
print()
print('<html>')
print('<head>')
print('<title>Hello World!</title>')
print('</head>')
print('<body>')
print('<h2> Hello %s </h2>' % site_name)
print('<h2> %s </h2>' % site_url)
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key, os.environ[key]))
print('</body>')
print('</html>')
