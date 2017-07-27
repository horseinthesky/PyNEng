#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

regex = '10\.(128|129|130).*'

with open('sber.txt') as f:
    for line in f:
        match = re.search(regex, line)    
        if match:
            with open('sber583.txt', 'a') as r:
                r.write(match.group(0) + '\n')
