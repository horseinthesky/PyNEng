#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 7.3a

Сделать копию скрипта задания 7.3.
Дополнить скрипт:
    добавить поддержку конфигурации, когда настройка access-порта выглядит так:
    interface FastEthernet0/20
      switchport mode access
      duplex auto

То есть, порт находится в VLAN 1
В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

Пример словаря:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw2.txt
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
            elif 'mode access' in el and not 'access vlan' in el:
                access_dist[el.split()[1]] = 1
            else:
                pass

    return access_dist, trunk_dist

access, trunk = get_int_vlan_map('config_sw2.txt')
print(access)
print(trunk)
