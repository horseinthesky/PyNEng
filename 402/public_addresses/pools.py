#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

template = ['edit', 'set startip', 'set endip', 'next']

regex = '((\d+)\.(\d+)\.(\d+)\.(\d+))'

with open('ips.txt') as f:
    for line in f:
        match = re.search (regex, line)
        if match:
            with open('result_pools.txt', 'a') as r:
                for command in template:
                    if command.endswith('edit'):
                        r.write('{} PUBLIC-{}-{}-{}-{}'.format(command, match.group(2), match.group(3), match.group(4), match.group(5)) + '\n')
                    elif command.endswith('startip'):
                        r.write(' {} {}'.format(command, match.group()) + '\n')
                    elif command.endswith('endip'):
                        r.write(' {} {}'.format(command, match.group()) + '\n')
                    else:
                        r.write(command + '\n')
