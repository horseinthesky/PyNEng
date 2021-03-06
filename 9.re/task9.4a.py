#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 9.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
    список с названиями полей
    список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 9.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой): 
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'}, 
{'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
    первый аргумент - список headers
    второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать. 
Надо импортировать или саму функцию, и использовать 
то же регулярное выражение, что и в задании 9.4, 
или импортировать результат выполнения функции parse_show.
"""
headers = ['interface', 'address', 'status', 'protocol']

"""Решение"""
from task94 import *

def convert_to_dict(head, int_list):
    """
    Функция ждёт список заголовков для словаря
    и спосок кортежей из функции parse_sh_ip_int_br
    """
    result = parse_sh_ip_int_br(int_list)
    dict_list = []
    for el in result:
        x = {}
        interface, address, status, protocol = el
        x[head[0]] = interface    
        x[head[1]] = address
        x[head[2]] = status
        x[head[3]] = protocol
        dict_list.append(x)

    return dict_list

print(convert_to_dict(headers, 'sh_ip_int_br_2.txt'))
