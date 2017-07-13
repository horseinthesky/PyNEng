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
while True:
    vl = input('Введите номер VLAN: ')
    if not (vl.isdigit() and 0 < int(vl) <= 4096):
        print('Таких VLAN не бывает!')
    else:
        break

with open('CAM_table.txt', 'r') as f:
    f = f.read().split('\n')
    for element in f:
        if not vl in element[:5]:
            pass
        else:
            vlan, mac, _, intf = element.split()
            print('{}    {}     {} '.format(vlan, mac, intf))
