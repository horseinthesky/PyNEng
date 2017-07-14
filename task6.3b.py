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
        if len(element.split()) == 0:
            pass
        elif vl == element.split()[0]:
            vlan, mac, _, intf = element.split()
            print('{}    {}     {} '.format(vlan, mac, intf))
