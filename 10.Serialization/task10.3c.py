#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 10.3c

С помощью функции draw_topology из файла draw_network_graph.py сгенерировать топологию, которая соответствует описанию в файле topology.yaml
Обратите внимание на то, какой формат данных ожидает функция draw_topology. Описание топологии из файла topology.yaml нужно преобразовать соответствую� им образом, чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.
В итоге, должно быть сгенерировано изображение топологии. Результат должен выглядеть так же, как схема в файле task_10_3c_topology.svg
Не копировать код функции draw_topology.
"""

"""Решение"""
import yaml
from draw_network_graph import draw_topology

with open('topology.yaml') as f:
    topology = yaml.load(f)

topology_dict = {}

for box in topology:
    for el in topology[box]:
        for nei in topology[box][el]:
            if not (nei, topology[box][el][nei]) in topology_dict:
                topology_dict[(box, el)] = (nei, topology[box][el][nei])

# print(topology_dict)
draw_topology(topology_dict)
