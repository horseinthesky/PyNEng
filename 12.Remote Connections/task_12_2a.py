#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.2a

Дополнить функцию send_config_commands из задания 12.2

Добавить аргумент output, который контролирует будет ли
результат выполнения команд выводится на стандартный поток вывода.

По умолчанию, результат должен выводиться.
'''

from pprint import pprint
import netmiko
import yaml

commands = ['logging 10.255.255.1',
            'logging buffered 20010',
            'no logging console']


def send_config_commands(device_list, config_commands, output=True):
    """
    Функция подключается по SSH к устройствам из списка,
    и выполняет команды в конфигурационном режиме.

    Параметры функции:
        - devices_list - список словарей с параметрами подключения к
            устройствам, которым надо передать команды
        - config_commands - список команд, которые надо выполнить

    Функция возвращает словарь с результатами выполнения команды:
        - ключ - IP устройства
        - значение - вывод с выполнением команд
    """
    result = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with netmiko.ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_config_set(config_commands)
            result[ip] = device_result
            if output:
                print(device_result)
    return result


def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']

    return templates


pprint(send_config_commands(get_device_list('devices.yaml'), commands))
