#!/usr/bin/python3

import os

ip_address = 'No address'
if 'REMOTE_ADDR' in os.environ:
  ip_address = os.environ['REMOTE_ADDR']

print('Content-type: text/html')
print()
print('<!doctype html>')
print('<html lang="ja">')
print('<head>')
print('  <meta charset="UTF-8">')
print('  <title>cgip</title>')
print('</head>')
print('<body>')
print(ip_address, '<br>', sep = '')
print('</body>')
print('</html>')