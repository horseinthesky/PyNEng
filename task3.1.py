#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 3.1
Обработать строку ospf_route и вывести информацию в виде:
Protocol:				OSPF
Prefix:					10.0.24.0/24
AD/Metric:				110/41
Next-Hop:				10.0.13.3
Last update:			3d18h
Outbound Interface:		FastEthernet0/0
'''

route_raw = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

commands = route_raw.split()

print('Protocol: \t\t + commands[0])
print('Prefix:\t\t\t' + commands[1])
print('AD/Metric:\t\t' + commands[2].strip('[]'))
print('Next-Hop:\t\t' + commands[4].strip(','))
print('Last update:\t\t' + commands[5].strip(','))
print('Outbound Interface:\t' + commands[6])
