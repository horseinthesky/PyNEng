#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 9.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент имя файла, 
в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
	Interface
	IP-Address
	Status
	Protocol

Информация должна возвращаться в виде списка кортежей: 
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'), 
('FastEthernet0/1', '10.0.2.1', 'up', 'up'), 
('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.
"""

"""Решение"""
import re

regex = ('(\S+) +'                          # Интерфейс
        '(\S+) +'                           # IP адрес
        '\w+ +\w+ +'                        # OK? и Method
        '(up|down|administratively down) +' # Status
        '(up|down)')                        # Protocol

def parse_sh_ip_int_br(show):
    """
    Функция ожидает название файла с выводом
    sh ip int br с устройств Cisco

    Возвращает списко кортежей ('int', 'ip', 'status', 'protocol')
    для каждого интерфейса.
    """
    int_br_list = []

    with open(show) as f:
        f = f.read()
        result = re.finditer(regex, f)
        for match in result:
            int_br_list.append(match.groups())
    
    return int_br_list

print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
