#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = "AAAA:BBBB:CCCC"
""")

MAC = 'AAAA:BBBB:CCCC'

"""Решение"""
mac_clean = MAC.replace(':', '')
bin_mac = '{:b}'.format(int(mac_clean, 16))
print(bin_mac)
