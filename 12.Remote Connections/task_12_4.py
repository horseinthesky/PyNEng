#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from netmiko import ConnectHandler
import yaml
import threading
from queue import Queue
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


def send_commands(device_list, queue, config=[], show='', filename=''):
    if show:
        result = send_show_command(device_list, show)
    if config:
        result = send_config_commands(device_list, config)
    if filename:
        result = send_commands_from_file(device_list, filename)
    queue.put(result)


def conn_threads(function, devices, **kwargs):
    threads = []
    queue = Queue()

    for device in devices:
        th = threading.Thread(target=function,
                              args=(device, queue),
                              kwargs=kwargs)
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    results = {}
    for t in threads:
        results.update(queue.get())

    return results


if __name__ == "__main__":
    commands = ['logging 10.255.255.1',
                'logging buffered 20010',
                'no logging console']
    devices = yaml.load(open('devices.yaml'))

    # pprint(conn_threads(send_commands, devices['routers'], show='sh ip int br'))
    pprint(conn_threads(send_commands, devices['routers'], config=commands))
    # pprint(conn_threads(send_commands, devices['routers'], filename='config.txt'))
