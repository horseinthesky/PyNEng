#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 10.3a
С помощью функции parse_sh_cdp_neighbors из задания 10.3, обработать вывод команды sh cdp neighbor из файлов:
	• sh_cdp_n_sw1.txt
	• sh_cdp_n_r1.txt
	• sh_cdp_n_r2.txt
	• sh_cdp_n_r3.txt
	• sh_cdp_n_r4.txt
	• sh_cdp_n_r5.txt
	• sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors, в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

Не копировать код функции parse_sh_cdp_neighbors
"""

"""Решение"""
import re
import glob
import yaml
from task10_3 import parse_sh_cdp_neighbors

files = glob.glob('sh_cdp_n*')

topology = {}

for filename in files:
    with open(filename) as f:
        parsed = parse_sh_cdp_neighbors(f.read())
        for box in parsed:
            topology[box] = parsed[box]

with open('topology.yaml', 'w') as f:
    yaml.dump(topology, f, default_flow_style=False)
