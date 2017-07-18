#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.2c

Переделать скрипт из задания 6.2b:
    передавать как аргументы:
        имя исходного файла конфигурации
        имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации, в которых содержатся слова из списка ignore. И затем записать оставшиеся строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt
"""
ignore = ['duplex', 'alias', 'Current configuration']

"""Решение"""
from sys import argv
config, cleared = argv[1:]

with open(config, 'r') as f:
    for line in f:
        if set(line.split()) & set(ignore) or 'Current configuration' in line:
            pass
        else:
            with open(cleared, 'a') as w:
               w.write(line)
