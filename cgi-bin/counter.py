#!/usr/bin/python3

import os
import sys

ip_address = 'No address'
if 'REMOTE_ADDR' in os.environ:
  ip_address = os.environ['REMOTE_ADDR']

with open('count.txt', mode='r') as f:
  l_strip = [s.strip() for s in f.readlines()]
  last_access_ip = l_strip[0]
  count = int(l_strip[1])
  if ip_address != last_access_ip:
    count += 1

with open('count.txt', mode='w') as f:
  f.write(ip_address + '\n')
  f.write(str(count))


print('Content-type: text/html')
print()
print('<!doctype html>')
print('<html lang="ja">')
print('<head>')
print('  <meta charset="UTF-8">')
print('  <title>cgip</title>')
print('</head>')
print('<body>')
print(str(count), '<br>', sep = '')
print('</body>')
print('</html>')
