#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 7.1
Создать функцию, которая генерирует конфигурацию для access-портов.
Параметр access ожидает, как аргумент, словарь access-портов, вида:
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17,
      'FastEthernet0/17':150 }
Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.
В конце строк в списке не должно быть символа перевода строки.
Пример итогового списка:
```python
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
```
Проверить работу функции на примере словаря access_dict.
'''

def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    result = []

    for intf in access:
        result.append('interface ' + intf,)
        for command in access_template:
            if command.endswith('access vlan'):
                result.append('{} {}'.format(command, access[intf]))
            else:
                result.append(command)
    return result


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

"""Решение"""
config = generate_access_config(access_dict)

for x in config: print(x)

