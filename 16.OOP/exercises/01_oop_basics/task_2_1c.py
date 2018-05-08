# -*- coding: utf-8 -*-

'''
Задание 2.1c

Изменить класс CiscoSSH из задания 2.1b:
* добавить метод send_cfg_commands, который повторяет функциональность метода send_config_set netmiko

Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_cfg_commands:
In [3]: r1.send_cfg_commands('logging 10.1.1.1')
Out[3]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#logging 10.1.1.1\nR1(config)#end\nR1#'

'''

import netmiko
import clitable


# Решение
class CiscoSSH:
    def __init__(self, username, password, enable_password, ip):
        device_params = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
            'secret': enable_password
        }
        self.ssh = self._connection(device_params)

    def _connection(self, params):
        conn = netmiko.ConnectHandler(**params)
        conn.enable()
        return conn

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def send_cfg_commands(self, command_list):
        return self.ssh.send_config_set(command_list)

    def send_and_parse_show(self, command, index_file='index', templates='templates'):
        command_output = self.send_show_command(command)
        attributes = {'Command': command, 'Vendor': self.ssh.device_type}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]
