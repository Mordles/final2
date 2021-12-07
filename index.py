#!/usr/bin/python37all

import json
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
letter = form.getvalue("option")

print('Content-type:text/html\n\n')
print('<html>')
print('Direction = %s' % letter)
print('</html>')