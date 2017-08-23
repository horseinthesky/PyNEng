#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.6

В задании используется пример из раздела про [модуль multiprocessing](book/chapter12/5b_multiprocessing.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_processes по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show


Пример из раздела:
"""

from netmiko import ConnectHandler
import multiprocessing
import yaml
from pprint import pprint


def send_show_command(device, show_command):
    output_dict = {}
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
        output_dict[device['ip']] = result
    return output_dict


def send_config_commands(device, config_commands, output=True):
    output_dict = {}
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
        if output:
            pprint(result)
        output_dict[device['ip']] = result
    return output_dict


def send_commands_from_file(device, filename):
    output_dict = {}
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_from_file(filename)
        output_dict[device['ip']] = result
    return output_dict


def send_commands(device, queue, config=[], show='', filename=''):
    if show:
        result = send_show_command(device, show)
    if config:
        result = send_config_commands(device, config)
    if filename:
        result = send_commands_from_file(device, filename)
    queue.put(result)


def conn_processes(function, devices, **kwargs):
    processes = []
    queue = multiprocessing.Queue()

    for device in devices:
        p = multiprocessing.Process(target=function,
                                    args=(device, queue),
                                    kwargs=kwargs)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    results = []
    for p in processes:
        results.append(queue.get())

    return results


if __name__ == "__main__":
    commands = ['logging 10.255.255.1',
                'logging buffered 20010',
                'no logging console']
    devices = yaml.load(open('devices.yaml'))

    # pprint(conn_processes(send_commands, devices['routers'], show='sh ip int br'))
    pprint(conn_processes(send_commands, devices['routers'], config=commands))
    # pprint(conn_processes(send_commands, devices['routers'], filename='config.txt'))
