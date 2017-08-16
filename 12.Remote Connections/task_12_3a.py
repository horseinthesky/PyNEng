# -*- coding: utf-8 -*-
'''
Задание 12.3a


Изменить функцию send_commands таким образом,
чтобы в списке словарей device_list
не надо было указывать имя пользователя, пароль, и пароль на enable.

Функция должна запрашивать имя пользователя,
пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

В файле devices2.yaml эти параметры уже удалены.
'''
from netmiko import ConnectHandler
from pprint import pprint
from getpass import getpass
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
    username = input('Введите логин: ')
    password = getpass('Введите пароль: ')
    secret = getpass('Введите secret: ')
    for box in device_list:
        box['username'] = username
        box['password'] = password
        box['secret'] = secret
    if device_list and show:
        pprint(send_show_command(device_list, show))
    elif device_list and config:
        pprint(send_config_commands(device_list, commands))
    elif device_list and filename:
        pprint(send_commands_from_file(device_list, filename))


devices_params = get_device_list('devices2.yaml')

send_commands(devices_params, False, command, False)
# send_commands(devices_params, commands, False, False)
# send_commands(devices_params, False, False, 'config.txt')
