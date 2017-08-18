#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.4

В задании используется пример из раздела про [модуль threading](book/chapter12/5a_threading.md).

Переделать пример таким образом, чтобы:
* вместо функции connect_ssh, использовалась функция send_commands из задания 12.3
 * переделать функцию send_commands, чтобы использовалась очередь и функция conn_threads по-прежнему возвращала словарь с результатами.
 * Проверить работу со списком команд, с командами из файла, с командой show

'''

from netmiko import ConnectHandler
from pprint import pprint
import yaml
import threading
from queue import Queue

commands = ['logging 10.255.255.1',
            'logging buffered 20010',
            'no logging console']

command = "sh ip int br"

devices = yaml.load(open('devices.yaml'))


def send_show_command(device_list, show_command):
    result = {}

    for device_params in device_list:
        ip = device_params['ip']
        print('Connecting to {}'.format(ip))
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            device_result = ssh.send_command(command)
            result[ip] = device_result
    queue.put(result)
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


def send_commands(device_list, config=[], show='', filename='', queue):
    if show:
        queue.put(pprint(send_show_command(device_list, show)))
    elif config:
        queue.put(pprint(send_config_commands(device_list, commands)))
    elif filename:
        queue.put(pprint(send_commands_from_file(device_list, filename)))


def connect_ssh(device_dict, command, queue):

    ssh = ConnectHandler(**device_dict)
    ssh.enable()
    result = ssh.send_command(command)
    print("Connection to device %s" % device_dict['ip'])

    queue.put({device_dict['ip']: result})


def conn_threads(function, devices, command):
    threads = []
    q = Queue()

    for device in devices:
        th = threading.Thread(target=function, args=(device, False, command, False, q))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    results = []
    for t in threads:
        results.append(q.get())

    return results


print(conn_threads(send_commands, devices['routers'], command))
