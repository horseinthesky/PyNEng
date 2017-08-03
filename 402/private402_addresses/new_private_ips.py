#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

template = ['edit', 'set subnet', 'next']

regex402 = 'permit ip (10)\.([0-6])\.(\d+)\.(0) 0\.0\.([037])\.255'
regex583 ='permit ip (10)\.(128|129)\.(\d+)\.(0)'

with open('402lists.txt') as f:
    for line in f:
        match = re.search(regex402, line)
        match583 = re.search(regex583, line)
        if match:
            with open('402addresses.txt', 'a') as r:
                for command in template:
                    if command.endswith('edit'):
                        r.write('{} VPN0402_{}.{}.{}.{}{}'.format(command, match.group(1), match.group(2), match.group(3), match.group(4), '\n'))
                    elif command.endswith('subnet'):
                        if '3' in match.group(5):
                            r.write(' {} {}{}{}{}{}{}{} {}'.format(command, match.group(1), '.', match.group(2), '.', match.group(3), '.', match.group(4), '255.255.252.0' + '\n'))
                        elif '7' in match.group(5):
                            r.write(' {} {}{}{}{}{}{}{} {}'.format(command, match.group(1), '.', match.group(2), '.', match.group(3), '.', match.group(4), '255.255.248.0' + '\n'))
                        else:
                            r.write(' {} {}{}{}{}{}{}{} {}'.format(command, match.group(1), '.', match.group(2), '.', match.group(3), '.', match.group(4), '255.255.255.0' + '\n'))          
                    else:
                        r.write(command + '\n')
        if match583:
            with open('583addresses.txt', 'a') as r:
                for command in template:
                    if command.endswith('edit'):
                        r.write('{} VPN0583_{}.{}.{}.{}{}'.format(command, match583.group(1), match583.group(2), match583.group(3), match583.group(4), '\n'))
                    elif command.endswith('subnet'):
                        r.write(' {} {}{}{}{}{}{}{} {}'.format(command, match583.group(1), '.', match583.group(2), '.', match583.group(3), '.', match583.group(4), '255.255.255.0' + '\n'))          
                    else:
                        r.write(command + '\n')
