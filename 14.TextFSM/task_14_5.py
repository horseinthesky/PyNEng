#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.5

В этом задании соединяется функциональность TextFSM и подключение к оборудованию.

Задача такая:
* подключиться к оборудованию
* выполнить команду show
* полученный вывод передавать на обработку TextFSM
* вернуть результат обработки

Для этого, воспользуемся функциями, которые были созданы ранее:
* функцией send_show_command из упражнения 12.1
* функцией parse_command_dynamic из упражнения 14.4

В этом упражнении нужно создать функцию send_and_parse_command:
* функция должна использовать внутри себя функции parse_command_dynamic и send_show_command.
* какие аргументы должны быть у функции send_and_parse_command, нужно решить самостоятельно
 * но, надо иметь в виду, какие аргументы ожидают две готовые функции, которые мы используем
* функция send_and_parse_command должна возвращать:
 * функция send_show_command возвращает словарь с результатами выполнения команды:
    * ключ - IP устройства
    * значение - результат выполнения команды
 * затем, нужно отправить полученный вывод на обработку функции parse_command_dynamic
 * в результате, должен получиться словарь, в котором:
    * ключ - IP устройства
    * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции send_show_command создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command на команде sh ip int br.
'''
from task_14_4 import parse_command_dynamic
from tabulate import tabulate
import netmiko
import yaml

command = "sh ip int br"
attributes_dict = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}


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

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with netmiko.ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_command(command)
            result[ip] = device_result
    return result


def get_device_list(filename):
    with open(filename) as f:
        templates = yaml.load(f)['routers']

    return templates


def send_and_parse_command(filename, command, attributes):
    output_dict = send_show_command(get_device_list(filename), command)
    result = {}
    for box, output in output_dict.items():
        result[box] = parse_command_dynamic(attributes, output, index='index', templates='templates')
    return result


if __name__ == '__main__':
    table_view = send_and_parse_command('devices.yaml', command, attributes_dict)
    for box in table_view:
        print(tabulate(table_view[box], headers='keys'), '\n' + '='*60)
