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

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
    состоит из 4 чисел разделенных точкой,
    каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
    'Incorrect IPv4 address'
"""

"""Решение"""
ip = input('Введите IP адрес в формате 10.1.1.5: ')

list = ip.split('.')

pass_OK = False

while not pass_OK:
    if len(list) != 4:
        print('Incorrect IPv4 address')
        ip = input('Введите IP адрес в формате 10.1.1.5: ')
        list = ip.split('.')
    elif not list[0].isdigit() or not list[1].isdigit() or not list[2].isdigit() or not list[3].isdigit():
        print('Incorrect IPv4 address')
        ip = input('Введите IP адрес в формате 10.1.1.5: ')
        list = ip.split('.')
    elif not 0 < int(list[0]) < 255 or not 0 < int(list[1]) < 255 or not 0 < int(list[2]) < 255 or not 0 < int(list[3]) < 255:
        print('Incorrect IPv4 address')
        ip = input('Введите IP адрес в формате 10.1.1.5: ')
        list = ip.split('.')
    else:
        pass_OK = True
else:
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
