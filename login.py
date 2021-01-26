#!/usr/bin/env python3
import os
import json
import cgi
import sys

from templates import login_page, secret_page
from secret import username, password

# print('Content-Type: text/html')
# print()
# print(cgi.FieldStorage()["username"])
# print(cgi.FieldStorage()["password"])

# New line declares that the stuff below is HTTP content
# print()
# print(json.dumps(dict(os.environ), indent=2))

print('Content-Type: text/html')
# Credits go to Hazel Campbell https://eclass.srv.ualberta.ca/mod/page/view.php?id=4987525
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    for line in posted.splitlines():
        print(line)
        post_username, post_password =  line.split('&')
        if post_username.split('=')[1] == username and post_password.split('=')[1] == password:
          print(f"Set-Cookie: actual-creds={username+','+password}")
# END Credit

print()
# #List headers as HTML
# print(f"""
# <!doctype html>
# <html>
# <body>
# <h1>YOOOO</h1>
# <ul>""")
# {json.dumps(dict(os.environ), indent=2)}
# for parameter in os.environ['QUERY_STRING'].split('&'):
#   (name, value) = parameter.split('=')
#   print(f"<li><em>{name}</em> = {value}")
# print("""
# </ul>
# </body
# </html>
# """)



print(login_page())
# print(os.environ)
print(os.environ['HTTP_COOKIE'])
found = False
if('HTTP_COOKIE' in os.environ):
  for cookie in os.environ['HTTP_COOKIE'].split('; '):
    print(cookie)
    if len(cookie.split('=')) >= 2 and cookie.split('=')[1] == f'{username},{password}':
      found = True
      print(secret_page(username,password))

if not found:
  print('no secret')