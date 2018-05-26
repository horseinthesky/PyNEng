# -*- coding: utf-8 -*-
'''
Задание 5.1b

Переделать генератор get_intf_ip из задания 5.1a таким образом,
чтобы он принимал как аргумент любое количество файлов.

Генератор должен обрабатывать конфигурацию и возвращать словарь
для каждой конфигурации на каждой итерации:
* ключ - hostname
* значение словарь, в котором:
    * ключ - имя интерфейса
    * значение - кортеж с IP-адресом и маской

Например: {'r1': {'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
                  'FastEthernet0/2': ('10.0.2.2', '255.255.255.0')}}

Проверить работу генератора на примере конфигураций config_r1.txt и config_r2.txt.

'''
import re


def get_intf_ip(list_of_files):
    if isinstance(list_of_files, str):
        list_of_files = [list_of_files]
    for filename in list_of_files:
        with open(filename) as f:
            device_dict = {}
            for line in f:
                if 'hostname' in line:
                    hostname = line.split()[1]
                if 'interface' in line:
                    interface = line.split()[1]
                match = re.search(regex, line)
                if match:
                    device_dict.update({interface: match.groups()})
            yield {hostname: device_dict}


regex = 'ip address (\S+) (\S+)\n'
