#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 9.3a
Переделать функцию parse_cfg из задания 9.3 таким образом, чтобы она возвращала словарь:
	• ключ: имя интерфейса
	• значение: кортеж с двумя строками:
		○ IP-адрес
		○ маска

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.
Проверить работу функции на примере файла config_r1.txt.
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
                    ip[interface] = match.groups()
    return ip

print(parse_cfg('config_r1.txt'))
