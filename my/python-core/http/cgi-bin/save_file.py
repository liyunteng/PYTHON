#!/usr/bin/env python
# -*- coding: utf-8 -*-

# save_file.py - save_file

# Date   : 2019/12/16

import cgi, os

form = cgi.FieldStorage()
dirname = os.path.abspath('share')

fileitem = form['filename']
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    try:
        with open(os.path.join(dirname, fn), 'wb') as f:
            f.write(fileitem.file.read())
        message = 'file ' + fn + ' upload success: ' + '/share/' + fn
    except Exception as e:
        message = 'file ' + fn + ' upload failed: ' + str(e)

else:
    message = 'file ' + fn + ' invalid'


print('''Content-Type: text/html\n
<html>
  <head>
	<meta charset="utf-8">
	<title> Upload File </title>
  </head>
  <body>
	<p>%s</p>
	</body>
</html>''' % (message,))
