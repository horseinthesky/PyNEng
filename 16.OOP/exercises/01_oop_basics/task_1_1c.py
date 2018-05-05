# -*- coding: utf-8 -*-

'''
Задание 1.1c

Изменить класс Topology из задания 1.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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


# Решение
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, raw_topology):
        formatted_topology = {}
        for pair in raw_topology:
            r_device, l_device = pair, raw_topology[pair]
            if l_device not in formatted_topology.keys():
                formatted_topology.update({r_device: l_device})
        return formatted_topology

    def delete_link(self, r_device, l_device):
        if r_device in self.topology:
            del(self.topology[r_device])
            if l_device in self.topology:
                del(self.topology[l_device])
        elif l_device in self.topology:
            del(self.topology[l_device])
        else:
            print('Такого соединения нет')

    def delete_node(self, node):
        x = len(self.topology)
        for pair in self.topology.copy():
            if node in pair or node in self.topology[pair]:
                del(self.topology[pair])
        if len(self.topology) == x:
            print('Такого устройства нет')
