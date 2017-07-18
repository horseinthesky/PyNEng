#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 7.2a

Сделать копию скрипта задания 7.2
Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    ключи: имена интерфейсов, вида 'FastEthernet0/1'
    значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.
"""

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
 
    trunk_config = {}

    for intf in trunk:
        trunk_config[intf] = []
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vlans = ','.join(str(vlan) for vlan in trunk[intf])
                trunk_config[intf].append(' {} {}'.format(command, vlans))
            else:
                trunk_config[intf].append(' {}'.format(command))
    return trunk_config

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

"""Решение"""
print(generate_trunk_config(trunk_dict))
