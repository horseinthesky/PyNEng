# -*- coding: utf-8 -*-

'''
Задание 2.1b

Изменить класс CiscoSSH из задания 2.1a.

Добавить метод send_and_parse_show, который:
    1. отправляет команду show на оборудование
    2. получает результат
    3. парсит его с помощью TextFSM
    4. возвращает результат в виде списка словарей

Для отправки команды и получения ее результата должен использоваться метод send_show_command.

Шаблон TextFSM должен выбираться динамически, на основании команды.


Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_and_parse_show:
In [3]: r1.send_and_parse_show('sh ip int br')
Out[3]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

Использование метода send_and_parse_show с явным указанием всех параметров:
In [4]: r1.send_and_parse_show('sh ip int br', index_file='index', templates_dir='templates')
Out[4]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

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

    def send_and_parse_show(self, command, index_file='index', templates='templates'):
        command_output = self.send_show_command(command)
        attributes = {'Command': command, 'Vendor': self.ssh.device_type}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]
