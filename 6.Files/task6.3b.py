#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.3b

Сделать копию скрипта задания 6.3a
Дополнить скрипт:
    Запросить у пользователя ввод номера VLAN.
    Выводить информацию только по указанному VLAN.
"""

"""Решение"""
vl = input('Введите номер VLAN: ')

with open('CAM_table.txt', 'r') as f:
    f = f.read().split('\n')
    for element in f:
        element = element.rstrip('\n').split()
        if element and vl == element[0]:
            vlan, mac, _, intf = element
            print('{}    {}     {} '.format(vlan, mac, intf))
