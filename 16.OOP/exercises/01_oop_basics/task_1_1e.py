# -*- coding: utf-8 -*-

'''
Задание 1.1e

Изменить класс Topology из задания 1.1x.

Добавить метод, который позволит выполнять сложение двух объектов (экземпляров) Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
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

topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                     ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}


# Решение
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, raw_topology):
        print(raw_topology)
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

    def add_link(self, r_device, l_device):
        if r_device in self.topology.keys() and self.topology[r_device] == l_device:
            print('Такое соединение существует')
        elif (
            r_device in self.topology.keys() or
            l_device in self.topology.keys() or
            r_device in self.topology.values() or
            l_device in self.topology.values()
        ):
            print('Cоединение с одним из портов существует')
        else:
            self.topology.update({r_device: l_device})

    def __add__(self, other):
        new_topology = self.topology.copy()
        new_topology.update(other.topology)
        return Topology(new_topology)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
