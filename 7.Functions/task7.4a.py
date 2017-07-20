#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 7.4a
Задача такая же, как и задании 7.4. Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл. В нем есть разделы с большей вложенностью, например, разделы:
	• interface Ethernet0/3.100
	• router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности. При этом, не привязываясь к конкретным разделам. Она должна быть универсальной, и сработать, если это будут другие разделы.

Теперь:
	• если уровня 2, то команды верхнего уровня будут ключами словаря, а команды подуровней - списками;
	• если уровня 3, то самый вложенный должен быть списком, а остальные - словарями.

На примере interface Ethernet0/3.100
{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}
"""

ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False

    for word in ignore:
        if word in command:
            ignore_command = True

    return ignore_command

def config_to_dict(config):
    """
    config - имя конфигурационного файла
    """
    config_dict = {}

    with open(config) as f:
        for line in f:
            line = line.rstrip()
            if line and not (line.startswith('!') or check_ignore(line, ignore)):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                elif line.startswith(' ') and not line.startswith('  '):
                    options = line
                    config_dict[section].append(line)
                elif line.startswith('  '):
                    if type(config_dict[section]) == list:
                        config_dict[section] = { i: [] for i in config_dict[section] }
                    config_dict[section][options].append(line)

    return config_dict

print(config_to_dict('config_r1.txt'))
