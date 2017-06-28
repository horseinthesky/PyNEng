#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
"""

"""Решение"""
ip = 'ololo'

while len(ip) != 11: 
    ip = input('Введите IP-подсеть в формате: 10.1.1.0/24: \n')
    print('Неверный формат')

ip1 = ip.split('.')
ip2 = ip1[3].split('/')

mask = ip2[1]
mask_bin = '1' * int(mask) + '0' * (32 - int(mask))

print('\n' + 'Network:')
print("{:8}  {:8}  {:8}  {:8}".format(ip1[0], ip1[1], ip1[2], ip2[0]))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(int(ip1[0]), int(ip1[1]), int(ip1[2]), int(ip2[0])))

print('\n' + 'Mask:' + '\n' + '/' + ip2[1]) 
print("{:8}  {:8}  {:8}  {:8}".format(int(mask_bin[:8], 2), int(mask_bin[8:16], 2), int(mask_bin[16:24], 2), int(mask_bin[24:], 2)))
print("{:8}  {:8}  {:8}  {:8}".format(mask_bin[:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:]))
