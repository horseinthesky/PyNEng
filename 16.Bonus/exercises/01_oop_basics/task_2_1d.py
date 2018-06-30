# -*- coding: utf-8 -*-

'''
Задание 2.1d

Изменить метод send_cfg_commands из задания 2.1c и добавить в метод проверку на ошибки.

Метод должен обнаруживать ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении команды возникла ошибка, вывести сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

А также спросить у пользователя надо ли продолжать выполнять команды на этом устройстве.

Метод send_cfg_commands должен возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_cfg_commands:
In [3]: r1.send_cfg_commands(commands)
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка
-> Invalid input detected at '^' marker.
Продолжить выполнение команд? [y]/n y
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка
-> Incomplete command.
Продолжить выполнение команд? [y]/n n
Out[3]:
({},
 {'logging': 'logging\n% Incomplete command.\n\nR1(config)#',
  'logging 0255.255.1': "logging 0255.255.1\n                   ^\n% Invalid input detected at '^' marker.\n\nR1(config)#"})

'''

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
