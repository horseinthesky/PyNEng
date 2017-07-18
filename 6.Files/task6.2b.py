#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.2b

Дополнить скрипт из задания 6.2a:
    вместо вывода на стандартный поток вывода, 
    скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
"""
ignore = ['duplex', 'alias', 'Current configuration']

"""Решение"""
from sys import argv
config = argv[1]

with open(config, 'r') as f:
    for line in f:
        if set(line.split()) & set(ignore) or 'Current configuration' in line:
            pass
        else:
            with open('config_sw1_cleared.txt', 'a') as w:
               w.write(line)
