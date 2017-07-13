#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
    Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
"""
ignore = ['duplex', 'alias', 'Current configuration']

"""Решение"""
from sys import argv
config = argv[1]

with open(config, 'r') as f:
    for line in f:
        if line.startswith('!') or set(line.split()) & set(ignore) or 'Current configuration' in line:
            pass
        else:
            print(line.rstrip())
