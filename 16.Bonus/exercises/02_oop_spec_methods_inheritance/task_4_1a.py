# -*- coding: utf-8 -*-

'''
Задание 4.1a

Добавить к классу CiscoTelnet из задания 4.1 метод send_config_commands.

Метод принимает как аргумент список команд или одну команду (строку).

Метод send_config_commands должен переходить в конфигурационный режим,
отправлять команды и выходить из конфигурационного режима.

Метод должен возвращать вывод, который показывает ввод каждой команды.

In [1]: from task_4_1a import CiscoTelnet

In [2]: r1 = CiscoTelnet('192.168.100.1', 'cisco','cisco','cisco')

In [3]: print(r1.send_config_commands(['logging 10.1.1.1', 'logging 10.2.2.2']))
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.1.1.1
R1(config)#logging 10.2.2.2
R1(config)#end
R1#
'''

import time
import telnetlib


class CiscoTelnet:
    def __init__(self, ip, username, password, enable, disable_paging=True):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        self._write_line(username)
        self.telnet.read_until(b'Password:')
        self._write_line(password)
        self._write_line('enable')
        self.telnet.read_until(b'Password:')
        self._write_line(enable)
        if disable_paging:
            self._write_line('terminal length 0')
            time.sleep(1)
            self.telnet.read_very_eager()

    def send_show_command(self, command):
        self._write_line(command)
        time.sleep(2)
        command_output = self.telnet.read_very_eager().decode('utf-8')
        return command_output

    def send_config_commands(self, commands):
        commands.insert(0, 'conf t')
        commands.append('end')
        for command in commands:
            self._write_line(command)
            time.sleep(2)
        command_output = self.telnet.read_very_eager().decode('utf-8')
        return command_output

    def _write_line(self, string):
        return self.telnet.write(string.encode('utf-8') + b'\n')


if __name__ == '__main__':
    r1 = CiscoTelnet('192.168.0.150', 'admin', 'admin', 'admin')
    print(r1.send_show_command('sh ip int br'))
