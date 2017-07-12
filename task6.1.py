#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.1

Файл ospf.txt
O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
O        10.0.28.0/24 [110/31] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.37.0/24 [110/11] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.78.0/24 [110/21] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.79.0/24 [110/20] via 10.0.19.9, 4d02h, FastEthernet0/2
O        10.0.81.0/24 [110/41] via 10.0.13.3, 3d20h, FastEthernet0/0
O        10.0.91.0/24 [110/60] via 10.0.19.9, 3d19h, FastEthernet0/2

Аналогично заданию 3.1 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде:
Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0

Так как это первое задание с открытием файла, заготовка для открытия файла уже сделана.
with open('ospf.txt', 'r') as f:
        for line in f:
                    print(line)
"""

"""Решение"""
with open('ospf.txt', 'r') as f:
    for line in f: 
        line = line.rstrip().split()
        print('Protocol:\t\t' + 'OSPF')
        print('Prefix:\t\t\t' + line[1])
        print('AD/Metric:\t\t' + line[2].strip('[]'))
        print('Next-Hop:\t\t' + line[4].strip(','))
        print('Last update:\t\t' + line[5].strip(','))
        print('Outbound Interface:\t' + line[6] + '\n')

