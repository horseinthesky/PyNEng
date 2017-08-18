#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.3b

Переделать функцию send_config_commands из задания 12.2a или 12.2

Добавить проверку на ошибки:
* При выполнении команд, скрипт должен проверять результат на такие ошибки:
    * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр output также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить функцию на команде с ошибкой.
'''

from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
import yaml
import subprocess

commands = ['logging 10.255.255.1',
            'logging buffered 20010',
            'no logging console']

command = "sh ip int br"


def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']
    return templates


def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
    if reply.returncode == 0:
        return True
    else:
        return False


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
    username = input('Введите логин: ')
    password = getpass('Введите пароль: ')
    secret = getpass('Введите пароль для enable: ')

    for box in device_list.copy():
        box['username'] = username
        box['password'] = password
        box['secret'] = secret
        if not ping_ip(box['ip']):
            print('Device {} Unreachable'.format(box['ip']))
            device_list.remove(box)
    if show:
        pprint(send_show_command(device_list, show))
    elif config:
        pprint(send_config_commands(device_list, commands))
    elif filename:
        pprint(send_commands_from_file(device_list, filename))


devices_params = get_device_list('devices2.yaml')

send_commands(devices_params, False, command, False)
# send_commands(devices_params, commands, False, False)
# send_commands(devices_params, False, False, 'config.txt')
