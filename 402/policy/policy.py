#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

vpn402 = ['edit', '  set name', '  set srcintf TO_VPN0402', '  set dstintf INET_GATE', '  set srcaddr', '  set dstaddr all', '  set action accept', '  set schedule always', '  set service ALL', '  set utm-status enable', '  set logtraffic all', '  set webfilter-profile default', '  set profile-protocol-options default', '  set ssl-ssh-profile certificate-inspection', '  set nat enable', '  set ippool enable', '  set poolname']

nonsber = ['edit', '  set name', '  set srcintf TO_VPN0402', '  set dstintf INET_GATE', '  set srcaddr', '  set dstaddr all', '  set action accept', '  set schedule always', '  set service ALL', '  set utm-status enable', '  set logtraffic all', '  set nat enable', '  set ippool enable', '  set poolname'] 

vpn583 = ['edit', '  set name', '  set srcintf TO_VPN0583', '  set dstintf INET_GATE', '  set srcaddr', '  set dstaddr all', '  set action accept', '  set schedule always', '  set service ALL', '  set utm-status enable', '  set logtraffic all', '  set nat enable', '  set ippool enable', '  set poolname']

regex = '(10)\.(\d+)\.(\d+)\.(0)/[24]+ +(\d+)\.(\d+)\.(\d+)\.(\d+)'

i = 3

with open('sber402.txt') as f:
    for line in f:
        if line:
            match = re.search(regex, line)
            if match:
                with open('testpolicy.txt', 'a') as r:
                    for command in vpn402:
                        if command.startswith('edit'):
                            r.write(command + ' {}'.format(i) + '\n')
                        elif command.endswith('set name'):
                            r.write(command + ' Sberbank-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('srcaddr'):
                            r.write(command + ' VPN0402-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('poolname'):
                            r.write(command + ' PUBLIC-{}-{}-{}-{}'.format(match.group(5), match.group(6), match.group(7), match.group(8)) + '\n')
                        else:
                            r.write(command + '\n')
                    r.write('next' + '\n')
        i = i + 1

with open('nonsber.txt') as f:
    for line in f:
        if line:
            match = re.search(regex, line)
            if match:
                with open('testpolicy.txt', 'a') as r:
                    for command in nonsber:
                        if command.startswith('edit'):
                            r.write(command + ' {}'.format(i) + '\n')
                        elif command.endswith('set name'):
                            r.write(command + ' FOR-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('srcaddr'):
                            r.write(command + ' VPN0402-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('poolname'):
                            r.write(command + ' PUBLIC-{}-{}-{}-{}'.format(match.group(5), match.group(6), match.group(7), match.group(8)) + '\n')
                        else:
                            r.write(command + '\n')
                    r.write('next' + '\n')
        i = i + 1

with open('sber583.txt') as f:
    for line in f:
        if line:
            match = re.search(regex, line)
            if match:
                with open('testpolicy.txt', 'a') as r:
                    for command in vpn583:
                        if command.startswith('edit'):
                            r.write(command + ' {}'.format(i) + '\n')
                        elif command.endswith('set name'):
                            r.write(command + ' SB_SMS-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('srcaddr'):
                            r.write(command + ' VPN0583-{}-{}-{}-{}'.format(match.group(1), match.group(2), match.group(3), match.group(4)) + '\n')
                        elif command.endswith('poolname'):
                            r.write(command + ' PUBLIC-{}-{}-{}-{}'.format(match.group(5), match.group(6), match.group(7), match.group(8)) + '\n')
                        else:
                            r.write(command + '\n')
                    r.write('next' + '\n')
        i = i + 1

