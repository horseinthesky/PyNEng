#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 10.3b

Переделать функциональность скрипта из задания 10.3a, в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
    list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
    save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
        значение по умолчанию - True
    topology_filename - имя файла, в который сохранится топология.
        по умолчанию, должно использоваться имя topology.yaml.
        топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию. Словарь должен быть в том же формате, что и в задании 10.3a.

Проверить работу функции generate_topology_from_cdp на файлах:
    sh_cdp_n_sw1.txt
    sh_cdp_n_r1.txt
    sh_cdp_n_r2.txt
    sh_cdp_n_r3.txt
    sh_cdp_n_r4.txt
    sh_cdp_n_r5.txt
    sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.
Не копировать код функции parse_sh_cdp_neighbors
"""

"""Решение"""
import re
import glob
import yaml
from task10_3 import parse_sh_cdp_neighbors

def generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology.yaml'):
    """
    Функция ожидает: 
        список файлов,
        опциональный параметр save_to_file (по умолчанию True), 
        который определяет, будет ли записан в файл, итоговый словарь
        имя файла, в который сохранится топология.
    """
    topology = {}

    for filename in list_of_files:
        with open(filename) as f:
            topology.update(parse_sh_cdp_neighbors(f.read()))

    if save_to_file:
        with open(topology_filename, 'w') as f:
            yaml.dump(topology, f, default_flow_style=False)

files = glob.glob('sh_cdp_n*')

generate_topology_from_cdp(files)
