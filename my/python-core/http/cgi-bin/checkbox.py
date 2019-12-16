#!/usr/bin/env python
# -*- coding: utf-8 -*-

# checkbox.py - checkbox

# Date   : 2019/12/16
import cgi


form = cgi.FieldStorage()

google_flag = True if form.getvalue('google') else False
runoob_flag = True if form.getvalue('runoob') else False

print('COntent-Type: text/html')
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title> CheckBox </title>')
print('</head>')
print('<body>')
print('<h2>google_flags: %s</h2>' % google_flag)
print('<h2>runoob_flags: %s</h2>' % runoob_flag)
print('</body>')
print('</html>')
