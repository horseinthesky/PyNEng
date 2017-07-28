#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

with open('nonsber.txt') as f:
    for line in f:
        m = re.search('(\S+)/[ 124]+ +(\S+)', line)
        if m:
            print(m.group(1) + ' ' + m.group(2))
