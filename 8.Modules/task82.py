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
def parse_cdp_neighbors(cdp):
    """
    Функция ожидает вывод команды show cdp neighbors
    на устройствах Cisco.

    Возвращает словарь, описывающий cdp соседства.
    """
    cdp_dict = {}
    for line in cdp.split('\n'):
        if '>' in line:
            hostname = line.split('>')[0]
        elif '#' in line:
            hostname = line.split('#')[0]
        elif line and line.strip()[-1].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = line.split()
            cdp_dict[(hostname, l_int+l_int_num)] = (r_host, r_int+r_int_num)

    return cdp_dict
