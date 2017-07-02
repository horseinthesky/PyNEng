#!/usr/bin/env python3

import telnetlib
import time

hosts = open('hosts', 'r')
for line in hosts:
    line = line[:-1]
    print(line + ' working')
    tn = telnetlib.Telnet(line)
    tn.write(('admin\n').encode('ascii'))
    tn.write(('admin\n').encode('ascii'))
    tn.write(('\n').encode('ascii'))
    tn.write(('term leng 0\n').encode('ascii'))
    tn.read_until(('term leng 0').encode('ascii'))
    tn.write(('show run\n').encode('ascii'))
    time.sleep(1)
    z = tn.read_very_eager()
    filename = 'Backups/' + line + '.txt'
    file = open(filename, 'w')
    file.write((z).decode('ascii'))

