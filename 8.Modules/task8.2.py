#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 8.2

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.
Функция ожидает, как аргумент, вывод команды одной строкой.
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt
"""

"""Решение"""
def get_cdp_dict(config):
    """
    Функция ожидает вывод команды show cdp neighbors
    на устройствах Cisco.

    Возвращает словарь, описывающий cdp соседства.
    """
    cdp_dict = {}
    with open(config) as f:
        el = f.read().split()
        cdp_dict[tuple([el[0].split('>')[0], el[42] + el[43]])] = tuple([el[41], el[49] + el[50]])
        cdp_dict[tuple([el[0].split('>')[0], el[52] + el[53]])] = tuple([el[51], el[59] + el[60]])
        cdp_dict[tuple([el[0].split('>')[0], el[62] + el[63]])] = tuple([el[61], el[69] + el[70]])

    return cdp_dict

print(get_cdp_dict('sw1_sh_cdp_neighbors.txt'))
