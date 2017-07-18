#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 7.1a

Сделать копию скрипта задания 7.1.
Дополнить скрипт:
ввести дополнительный параметр, который контролирует будет ли настроен port-security
имя параметра 'psecurity'
по умолчанию значение False
Проверить работу функции на примере словаря access_dict, с генерацией конфигурации port-security и без.
"""

def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    access_config = []

    for intf in access:
        access_config.append('interface ' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                access_config.append('{} {}'.format(command, access[intf]))
            else:
                access_config.append(command)
        if psecurity:
        # Тут можно добавить просто список команд,
        # так как их не нужно никак модифицировать
        # для добавления содержимого списка, используется метод extend
            access_config.extend(port_security)
    return access_config

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

"""Решение"""
for x in generate_access_config(access_dict): print(x)
print()
for y in generate_access_config(access_dict, psecurity=True): print(y)


