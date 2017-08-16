#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Дополнить функцию send_config_commands из задания 12.2a или 12.2

Добавить проверку на ошибки:
* При выполнении команд, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком
устройстве.

Проверить функцию на команде с ошибкой.
'''

from pprint import pprint
import netmiko
import yaml

commands = ['logging',
            'loggiing buffered 20010',
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
    result_ok = {}
    result_ne_ok = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with netmiko.ConnectHandler(**device_params) as ssh:
            ok_list = []
            ne_ok_list = []
            ssh.enable()
            for command in commands:
                device_result = ssh.send_config_set(command)
                if 'Invalid input detected' in device_result:
                    print('Invalid input detected', 'with', command, 'on', ip)
                    ne_ok_list.append(device_result)
                elif 'Incomplete command' in device_result:
                    print('Incomplete command', 'with', command, 'on', ip)
                    ne_ok_list.append(device_result)
                elif 'Ambiguous command' in device_result:
                    print('Ambiguous command', 'with', command, 'on', ip)
                    ne_ok_list.append(device_result)
                else:
                    if output:
                        print(device_result)
                    ok_list.append(device_result)
                result_ok[ip] = ''.join(ok_list)
                result_ne_ok[ip] = ''.join(ne_ok_list)
    return result_ok, result_ne_ok


def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']

    return templates


pprint(send_config_commands(get_device_list('devices.yaml'), commands))
