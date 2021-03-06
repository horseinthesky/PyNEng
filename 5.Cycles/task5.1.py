#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в десятично-точечном формате.
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
    'unicast' - если IP-адрес принадлежит классу A, B или C
    'multicast' - если IP-адрес принадлежит классу D
    'local broadcast' - если IP-адрес равен 255.255.255.255
    'unassigned' - если IP-адрес равен 0.0.0.0
    'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
    A: 1-127
    B: 128-191
    C: 192-223
    D: 224-239
"""

"""Решение"""
ip = input('Введите IP адрес в формате 10.1.1.5: ')

list = ip.split('.')

if int(list[0]) >= 1 and int(list[0]) <= 223:
    print('unicast')
elif int(list[0]) >= 224 and int(list[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
