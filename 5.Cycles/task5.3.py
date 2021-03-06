#!/usr/bin/env python3
# -*- coding: utf-8 -*-

("""
Задание 5.3

В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.
В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать, что с ними делать.
Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка
указывает как воспринимать номера VLAN, которые идут дальше:
 add - значит VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
 del - значит VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
 only - значит, что на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)

Задача для портов 0/1, 0/2, 0/4:
 сгенерировать конфигурацию на основе шаблона trunk_template
 с учетом ключевых слов add, del, only
""")

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access': {'0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'},
            'trunk': {'0/1': ['add', '10', '20'],
                      '0/2': ['only', '11', '30'],
                      '0/4': ['del', '17']}}

for intf in fast_int['access']:
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, fast_int['access'][intf]))
        else:
            print(' {}'.format(command))

"""Решение"""
for intf in fast_int['trunk']:
    vlans = ','.join(fast_int['trunk'][intf][1:])
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if fast_int['trunk'][intf][0] == 'add':
            if command.endswith('allowed vlan'):
                print(' {} {} {}'.format(command, 'add', vlans))
            else:
                print(' {}'.format(command))
        elif 'only' in fast_int['trunk'][intf][0]:
            if command.endswith('allowed vlan'):
                print(' {} {}'.format(command, vlans))
            else:
                print(' {}'.format(command))
        else:
            if command.endswith('allowed vlan'):
                print(' {} {} {}'.format(command, 'remove', vlans))
            else:
                print(' {}'.format(command))
