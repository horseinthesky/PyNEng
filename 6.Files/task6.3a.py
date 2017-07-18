#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.3a

Сделать копию скрипта задания 6.3
Дополнить скрипт:
    Отсортировать вывод по номеру VLAN
"""

"""Решение"""
with open('CAM_table.txt', 'r') as f:
    f = sorted(f.read().split('\n'))
    for element in f:
        element = element.rstrip('\n').split()
        if element and element[0].isdigit():
            vlan, mac, _, intf = element
            print('{}    {}     {} '.format(vlan, mac, intf))
