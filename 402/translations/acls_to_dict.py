#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

regex_list = 'ip access-list extended (\S+)'
regex_402 = 'permit ip (10\.[1-6]+\.\d+\.\d+)'
regex_583 = 'permit ip (10\.(128|129|130)\.\d+\.\d+)'

dict402 = {}
dict583 = {}

with open('acls.txt') as f:
    for line in f:
        match = re.search(regex_list, line)
        match_402 = re.search(regex_402, line)
        match_583 = re.search(regex_583, line)
        if match:
            x = match.group(1)
        elif match_402:
            dict402[x] = match_402.group(1)
        elif match_583:
            dict583[x] = match_583.group(1)

with open('dict402.txt', 'w') as r:
    r.write('dict402 = ' + str(dict402))

with open('dict583.txt', 'w') as r:
    r.write('dict583 = ' + str(dict583))
