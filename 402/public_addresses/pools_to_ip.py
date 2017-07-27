#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re
regex = ' ([\d\.]+) prefix'

with open('asr_pools.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            r = open('ips.txt', 'a')
            r.write(match.group(1) + '\n')

                
