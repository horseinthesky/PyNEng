# -*- coding: utf-8 -*-

'''
Задание 1.1

Создать класс Topology, который представляет топологию сети.

При создании экземпляра класса, как аргумент передается словарь, который описывает топологию.
Словарь может содержать дублирующиеся соединения.

Дублем считаются такие соединения:
('R1', 'Eth0/0'): ('SW1', 'Eth0/1') и ('SW1', 'Eth0/1'): ('R1', 'Eth0/0')

При создании класса должен быть создан атрибут topology, в котором содержится словарь топологии,
но уже без дублей.

Пример создания экземпляра класса:
In [2]: top = Topology(topology_example)

После этого, должен быть доступен атрибут topology:

In [3]: top.topology
Out[3]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}


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

'''Решение'''


class Topology:
    def __init__(self, raw_topology):
        self.raw_topology = raw_topology

    def topology(self):
        formatted_topology = {}
        for pair in self.raw_topology:
            r_device, l_device = pair, self.raw_topology[pair]
            if l_device not in formatted_topology.keys():
                formatted_topology.update({r_device: l_device})
        return formatted_topology
