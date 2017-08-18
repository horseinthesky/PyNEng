#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 12.2c

Переделать функцию send_config_commands из задания 12.2b

Если при выполнении команды на одном из устройств возникла ошибка,
спросить пользователя надо ли выполнять эту команду на других устройствах.

Варианты ответа [y/n]:
* y - выполнять команду на оставшихся устройствах
* n - не выполнять команду на оставшихся устройствах

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение -  вложенный словарь:
   * ключ - команда
   * значение - вывод с выполнением команд

Проверить функцию на команде с ошибкой.
'''
from netmiko import ConnectHandler
import yaml
from pprint import pprint


def check_for_errors(command_output):
    errors = ['Invalid input detected',
              'Incomplete command',
              'Ambiguous command']
    for error in errors:
        if error in command_output:
            return error


def send_config_commands(device_list, config_commands, output=True):
    valid_commands_output = {}
    invalid_commands_output = {}
    for device in device_list:
        ip = device['ip']
        valid_commands_output[ip] = {}
        invalid_commands_output[ip] = {}
        bad_commands = []
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in config_commands:
                result = ssh.send_config_set(command)
                error = check_for_errors(result)
                if error:
                    error_message = ('Error "{}" appeared in command "{}" '
                                     'execution on device {}')
                    print(error_message.format(error, command, ip))
                    invalid_commands_output[ip][command] = result
                    decision = input('Should this command to be executed on other devices? (y/n): ')
                    if decision is 'n':
                        bad_commands.append(command)
                else:
                    if output:
                        print(result)
                    valid_commands_output[ip][command] = result
        for bad_command in bad_commands:
            config_commands.remove(bad_command)
    return valid_commands_output, invalid_commands_output


with open('devices.yaml') as f:
    devices = yaml.load(f)

commands = ['logging 0255.255.1',
            'logging buffered 20010',
            'logging ']

success, fail = send_config_commands(devices['routers'], commands, output=False)
pprint(success)
pprint(fail)
