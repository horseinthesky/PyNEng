#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

template = ['edit', 'set startip', 'set endip', 'next']

with open('ips.txt') as f:
    for line in f:
        with open('newresultpools.txt', 'a') as w:
            for command in template:
                if command.endswith('edit'):
                    w.write('{} PUBLIC_{}'.format(command, line))
                elif command.endswith('startip'):
                    w.write(' {} {}'.format(command, line))
                elif command.endswith('endip'):
                    w.write(' {} {}'.format(command, line))
                else:
                    w.write(command + '\n')
