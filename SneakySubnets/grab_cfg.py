#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from telnetlib import Telnet
from concurrent.futures import ProcessPoolExecutor

eve_ip = '192.168.0.11'

devices = [{'hostname': 'r1', 'port': '32769'},
           {'hostname': 'r2', 'port': '32770'},
           {'hostname': 'r3', 'port': '32771'},
           {'hostname': 'r4', 'port': '32772'},
           {'hostname': 'r5', 'port': '32773'},
           {'hostname': 'r6', 'port': '32774'},
           {'hostname': 'r7', 'port': '32775'},
           {'hostname': 'r8', 'port': '32776'},
           {'hostname': 'r9', 'port': '32777'},
           {'hostname': 'r10', 'port': '32778'},
           {'hostname': 'sw1', 'port': '32779'},
           {'hostname': 'sw2', 'port': '32780'},
           {'hostname': 'sw3', 'port': '32781'},
           {'hostname': 'sw4', 'port': '32782'}]


def save_cfg(device_dict, data):
    with open(device_dict['hostname'] + '.txt', 'w') as f:
        f.write(data.decode('ascii'))
    print('Data from ' + device_dict['hostname'] + ' saved to' + f)


def grab_cfg(device_dict):
    tn = Telnet(eve_ip, device_dict['port'])
    tn.write(('\r\n').encode('ascii'))
    tn.write(('term leng 0\n').encode('ascii'))
    tn.read_until(('term leng 0').encode('ascii'))
    tn.write(('show run\n').encode('ascii'))
    time.sleep(1)
    tn.read_until(('Current configuration').encode('ascii'))
    data = tn.read_very_eager()
    save_cfg(device_dict, data)
    print('Data from ' + device_dict['hostname'] + ' grabbed')


def multi_conn(function, devices, limit=10):
    with ProcessPoolExecutor(max_workers=limit) as executor:
        executor.map(function, devices)


multi_conn(grab_cfg, devices)
print('All done')
