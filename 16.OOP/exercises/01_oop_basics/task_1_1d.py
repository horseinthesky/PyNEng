# -*- coding: utf-8 -*-

'''
Задание 1.1d

Изменить класс Topology из задания 1.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


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
