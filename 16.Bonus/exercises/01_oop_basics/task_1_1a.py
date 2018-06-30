# -*- coding: utf-8 -*-

'''
Задание 1.1a

Изменить класс Topology из задания 1.1.

Если в задании 1.1 удаление дублей выполнялось в методе __init__,
надо перенести функциональность удаления дублей в метод _normalize.

'''

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}


# Метод __init__ должен выглядеть таким образом:
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    '''Решение'''
    def _normalize(self, raw_topology):
        formatted_topology = {}
        for pair in raw_topology:
            r_device, l_device = pair, raw_topology[pair]
            if l_device not in formatted_topology.keys():
                formatted_topology.update({r_device: l_device})
        return formatted_topology
