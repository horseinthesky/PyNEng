#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам,
    которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо
    выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан,
функция вызывает разные функции внутри.

Далее комбинация из аргумента и соответствующей функции:
* show -- функция send_show_command из задания 12.1
* config -- функция send_config_commands из задания 12.2, 12.2a или 12.2b
* filename -- функция send_commands_from_file
    (ее также надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt
'''

from netmiko import ConnectHandler
from pprint import pprint
import yaml

commands = ['logging 10.255.255.1',
            'logging buffered 20010',
            'no logging console']

command = "sh ip int br"


def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']
    return templates


def send_show_command(device_list, show_command):
    result = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_command(command)
            result[ip] = device_result

    return result


def send_config_commands(device_list, config_commands, output=True):
    result = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_config_set(config_commands)
            result[ip] = device_result
    return result


def send_commands_from_file(device_list, filename):
    result = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_config_from_file(filename)
            result[ip] = device_result
    return result


def send_commands(device_list, config=[], show='', filename=''):
    if device_list and show:
        pprint(send_show_command(device_list, show))
    elif device_list and config:
        pprint(send_config_commands(device_list, commands))
    elif device_list and filename:
        pprint(send_commands_from_file(device_list, filename))


devices_params = get_device_list('devices.yaml')

send_commands(devices_params, False, command, False)
send_commands(devices_params, commands, False, False)
send_commands(devices_params, False, False, 'config.txt')
