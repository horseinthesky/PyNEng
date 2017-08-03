#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

with open('nonsber.txt') as n:
    n = n.read().rstrip().split('\n')

with open('translations.txt') as f:
    for line in f:
        x = re.search('NAT_VPN0402_(\S+)', line).group(1)
        if x in n:
            with open('testlist.txt', 'a') as w:
                w.write(line)
