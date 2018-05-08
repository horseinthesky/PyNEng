# -*- coding: utf-8 -*-

'''
Задание 3.1

Дополнить любой из вариантов класса CiscoSSH из заданий 2.1a-2.1d.

Добавить метод, который закрывает сессию SSH при удалении объекта.

Пример использования:
In [4]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

In [5]: r1.send_show_command('sh clock')
Out[5]: '*11:19:39.596 UTC Sun Jan 14 2018'

In [6]: del r1
Соединение разорвано
'''

# Решение
import netmiko
import clitable

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands


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

    def _decision(self):
        return input('Продолжить выполнение команд? [y]/n ')

    def _check_for_errors(self, command_output):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        for error in errors:
            if error in command_output:
                return error

    def __del__(self):
        self.ssh.disconnect()
        print('Соединение разорвано')

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def send_cfg_commands(self, command_list=commands):
        successful_commands = {}
        failed_commands = {}
        for command in command_list:
            output = self.ssh.send_config_set(command)
            error = self._check_for_errors(output)
            if error:
                failed_commands[command] = output
                print("При выполнении команды '{}' на устройстве 192.168.0.150 возникла ошибка\n-> {}".format(command, error))
                if self._decision() is 'n':
                    break
            else:
                successful_commands[command] = output
        return successful_commands, failed_commands

    def send_and_parse_show(self, command, index_file='index', templates='templates'):
        command_output = self.send_show_command(command)
        attributes = {'Command': command, 'Vendor': self.ssh.device_type}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]
