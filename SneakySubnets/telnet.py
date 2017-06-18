#!/usr/bin/python3
# -*- coding: utf-8 -*-

import telnetlib
import time

host = '10.10.30.1'

connect = telnetlib.Telnet(host)

connect.write(("admin\n").encode('ascii'))
connect.write(("admin\n").encode('ascii'))
connect.write(("conf t\n").encode('ascii'))
connect.write(("hostname R1\n").encode('ascii'))
time.sleep(1)
