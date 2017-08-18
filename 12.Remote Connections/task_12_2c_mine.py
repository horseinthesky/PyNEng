#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
                    decision = input('Should this command to executed on other devices? (y/n): ')
                    if decision is 'n':
                        commands.remove(command)
                elif 'Incomplete command' in device_result:
                    print('Incomplete command', 'with', command, 'on', ip)
                    ne_ok_list.append(device_result)
                    decision = input('Should this command to executed on other devices? (y/n): ')
                    if decision is 'n':
                        commands.remove(command)
                elif 'Ambiguous command' in device_result:
                    print('Ambiguous command', 'with', command, 'on', ip)
                    ne_ok_list.append(device_result)
                    decision = input('Should this command to executed on other devices? (y/n): ')
                    if decision is 'n':
                        commands.remove(command)
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
