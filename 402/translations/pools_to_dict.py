#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

regex = 'ip nat pool (VPN0402\S+) (\S+)'

pools_dict = {}

with open('pools.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            pools_dict[match.group(1)] = match.group(2)

print(pools_dict)
