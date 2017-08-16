#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from netmiko import ConnectHandler
import yaml
from pprint import pprint

commands = [ 'logging 10.255.255.1',
             'logging buffered 20010',
             'asdno logging console' ]


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
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in config_commands:
                result = ssh.send_config_set(command)
                error = check_for_errors(result)
                if error:
                    error_message = ('Error {} appeared in command {} '
                                     'execution on device {}')
                    print(error_message.format(error, command, device['ip']))
                    invalid_commands_output[device['ip']] = result
                else:
                    if output:
                        print(result)
                    valid_commands_output[device['ip']] = result
    return valid_commands_output, invalid_commands_output


with open('devices.yaml') as f:
    devices = yaml.load(f)

commands = [ 'logging 0255.255.1',
             'logging buffered 20010',
             'logging ' ]

success, fail = send_config_commands(devices['routers'], commands, output=False)
pprint(success)
pprint(fail)
