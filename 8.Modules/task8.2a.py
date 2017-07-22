#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
С помощью функции parse_cdp_neighbors из задания 8.2 и 
функции draw_topology из файла draw_network_graph.py, 
сгенерировать топологию, которая соответствует выводу 
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии. 
Результат должен выглядеть так же, как схема в файле task_8_2a_topology.svg
"""

"""Решение"""
from task82 import parse_cdp_neighbors
from draw_network_graph import draw_topology

draw_topology(parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'))
