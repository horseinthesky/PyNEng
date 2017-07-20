#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 9.3b

Проверить работу функции parse_cfg из задания 9.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1 соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 9.3a таким образом, 
чтобы она возвращала список кортежей для каждого интерфейса. 
Если на интерфейсе назначен только один адрес, в списке будет один кортеж. 
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, 
что интерфейсу Ethernet0/1 соответствует список из двух кортежей.
"""

"""Решение"""
import re

int_regex = ('interface ' # Убрать лишнее
            '(.*)')       # IP Address

regex = ('ip address '    # Убрать лишнее
        '([0-9\.]+) '     # IP Address
        '([\d.]+)')       # Subnet Mask

def parse_cfg(config):
    """
    Функция ожидает название файла конфигурации и возвращает список кортежей
    ip, маска подсети для всех интерфейсов конфигурации.
    """
    ip = {}

    with open(config) as f:
        for line in f:
            int_match = re.search(int_regex, line)
            if int_match:
                interface = int_match.group(1)
            else:
                match = re.search(regex, line)
                if match:
                    if not interface in ip.keys():
                        ip[interface] = []
                        ip[interface].append(match.groups())
                    else:
                        ip[interface].append(match.groups())
    return ip

print(parse_cfg('config_r2.txt'))
