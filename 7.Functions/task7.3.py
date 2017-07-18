#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 7.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:
	• словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
	{'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}

	• словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
	 {'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
"""

"""Решение"""
def get_int_vlan_map(config):
    """
    config - название файла конфигурации устройства.

    Функция создаёт словари access и trunk портов access_dist и trunk_dist соответственно.
    """
    access_dist = {}
    trunk_dist = {}

    with open(config) as f:
        f = f.read().replace('\n', '').split('!')
        for el in f:
            if 'access vlan' in el:
                access_dist[el.split()[1]] = int(el.split()[8])
            elif 'trunk' in el:
                trunk_dist[el.split()[1]] = [ int(v) for v in el.split()[10].split(',') ] 
            else:
                pass

    return access_dist, trunk_dist

access, trunk = get_int_vlan_map('config_sw1.txt')
print(access)
print(trunk)
