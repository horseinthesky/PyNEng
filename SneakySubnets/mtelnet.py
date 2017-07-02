#!/usr/bin/env python3

import telnetlib
import time

for x in range (1,11):
    host = '10.10.30.' + str(x)
    print(host + ' working')
    tn = telnetlib.Telnet(host)
    tn.write(('admin\n').encode('ascii'))
    tn.write(('admin\n').encode('ascii'))
    tn.write(('\n').encode('ascii'))
    tn.write(('term leng 0\n').encode('ascii'))
    tn.read_until(('R').encode('ascii'))
    tn.write(('show run\n').encode('ascii'))
    time.sleep(1)
    z = tn.read_very_eager()
    filename = 'Backups/' + host + '.txt'
    file = open(filename, 'w')
    file.write((z).decode('ascii'))

    

