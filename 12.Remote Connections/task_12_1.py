#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройствам из списка, и выполняет  команду
на основании переданных аргументов.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Проверить работу функции на примере:
* устройств из файла templates.yaml (для этого надо считать информацию из файла)
* и команды command

'''

import netmiko
import yaml
from pprint import pprint

command = "sh ip int br"

def send_show_command(device_list, command):
    """
    Функция подключается по SSH к устройствам из списка, и выполняет команду
    на основании переданных аргументов.

    Параметры функции:
    - devices_list - список словарей с параметрами подключения к устройствам,
      которым надо передать команды
    - command - команда, которую надо выполнить

    Функция возвращает словарь с результатами выполнения команды:
        - ключ - IP устройства
        - значение - результат выполнения команды
    """
    result = {}

    with open('devices.yaml') as f:
        templates = yaml.load(f)['routers']
        for ip in device_list:
            print('Connecting to {}'.format(ip))
            for device_params in templates:
                with netmiko.ConnectHandler(**device_params) as ssh:
                    ssh.enable()
                    device_result = ssh.send_command(command)
                    result[ip] = device_result

    return result

def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']
        device_list = []
        for device_params in templates:
            device_list.append(device_params['ip'])

    return device_list

pprint(send_show_command(get_device_list('devices.yaml'), command))
