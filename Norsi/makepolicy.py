#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

regex = re.compile(r'set policy id \d+ .*"(10.\d+.\d+.\d+)/(\d+)" .*')

addresses = ['edit', ' set subnet', 'next']

policy = ['edit', '  set name', '  set srcintf TO_DSZN_VPN0479', '  set dstintf INET_GATE_Norsi', '  set srcaddr', '  set dstaddr all', '  set action accept', '  set schedule always', '  set service ALL', '  set logtraffic all', '  set nat enable']

with open('addresses.txt', 'a') as a:
    with open('policy.txt', 'a') as p:
        with open('sg.txt') as f:
            i = 0
            for line in f:
                match = regex.search(line)
                if match:
                    i += 1
                    for command in addresses:
                        if command.endswith('edit'):
                            if match.group(1) == '10.64.0.0':
                                a.write('{} SMS_Content_Filtering_VPN0591_{}/{}\n'.format(command, match.group(1), match.group(2)))
                            elif match.group(1) == '10.7.0.0':
                                a.write('{} WIFI_KF_VPN0577_{}/{}\n'.format(command, match.group(1), match.group(2)))
                            else:
                                a.write('{} DSZN_VPN0479_{}/{}\n'.format(command, match.group(1), match.group(2)))
                        elif command.endswith('subnet'):
                            if match.group(2) == '16':
                                a.write('{} {} 255.255.0.0\n'.format(command, match.group(1)))
                            elif match.group(2) == '22':
                                a.write('{} {} 255.255.252.0\n'.format(command, match.group(1)))
                            elif match.group(2) == '24':
                                a.write('{} {} 255.255.255.0\n'.format(command, match.group(1)))
                            elif match.group(2) == '26':
                                a.write('{} {} 255.255.255.192\n'.format(command, match.group(1)))
                            elif match.group(2) == '28':
                                a.write('{} {} 255.255.255.240\n'.format(command, match.group(1)))
                            elif match.group(2) == '29':
                                a.write('{} {} 255.255.255.248\n'.format(command, match.group(1)))
                        elif command.endswith('next'):
                            a.write(command + '\n')
                    for command in policy:
                        if command.endswith('edit'):
                            p.write('{} {}\n'.format(command, i))
                        elif command.endswith('set name'):
                            p.write('{} DSZN_Norsi_{}/{}\n'.format(command, match.group(1), match.group(2)))
                        elif command.endswith('srcaddr'):
                            if match.group(1) == '10.64.0.0':
                                p.write('{} SMS_Content_Filtering_VPN0591_{}/{}\n'.format(command, match.group(1), match.group(2)))
                            elif match.group(1) == '10.7.0.0':
                                p.write('{} WIFI_KF_VPN0577_{}/{}\n'.format(command, match.group(1), match.group(2)))
                            else:
                                p.write('{} DSZN_VPN0479_{}/{}\n'.format(command, match.group(1), match.group(2)))
                        else:
                            p.write(command + '\n')
                    p.write('next\n')
