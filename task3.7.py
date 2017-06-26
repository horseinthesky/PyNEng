#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("""
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = "AAAA:BBBB:CCCC"
""")

MAC = 'AAAA:BBBB:CCCC'

"""Решение"""
a = MAC[:4]
b = MAC[5:9]
c = MAC[10:]
test = a + b + c

BIN = bin(int((test), 16))
print(BIN)
