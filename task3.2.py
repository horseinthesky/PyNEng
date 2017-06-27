#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('''
Задание 3.2
Преобразовать строку MAC с формата XXXX:XXXX:XXXX в XXXX.XXXX.XXXX.
''')
MAC = 'AAA:BBBB:CCCC'

print(('MAC = '), MAC, '\n')

"""Решение"""
MAC_NEW = MAC.replace(':', '.')
print(MAC_NEW)
