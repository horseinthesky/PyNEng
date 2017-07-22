#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 8.2b

Для выполнения этого задания, должен быть установлен graphviz:
apt-get install graphviz

И модуль python для работы с graphviz:
pip install graphviz

С помощью функции parse_cdp_neighbors из задания 8.2 
и функции draw_topology из файла draw_network_graph.py, 
сгенерировать топологию, которая соответствует выводу команды sh cdp neighbor из файлов:
    sh_cdp_n_sw1.txt
    sh_cdp_n_r1.txt
    sh_cdp_n_r2.txt
    sh_cdp_n_r3.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.
В итоге, должен быть сгенерировано изображение топологии. 
Результат должен выглядеть так же, как схема в файле task_8_2b_topology.svg
"""

"""Решение"""
from task82 import parse_cdp_neighbors
from draw_network_graph import draw_topology

r1 = parse_cdp_neighbors(open('sh_cdp_n_r1.txt', 'r').read())
r2 = parse_cdp_neighbors(open('sh_cdp_n_r2.txt', 'r').read())
r3 = parse_cdp_neighbors(open('sh_cdp_n_r3.txt', 'r').read())
sw1 = parse_cdp_neighbors(open('sh_cdp_n_sw1.txt', 'r').read())

for x in [r2, r3]:
    r1.update(x)

draw_topology(r1)
