#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = "AAAA:BBBB:CCCC"
""")

MAC = 'AAAA:BBBB:CCCC'

"""Решение"""
mac_clean = bin(int(MAC.replace(':', ''), 16))[2:]
print(mac_clean)
