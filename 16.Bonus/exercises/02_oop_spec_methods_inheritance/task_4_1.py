# -*- coding: utf-8 -*-

'''
Задание 4.1

В этом задании необходимо переделать класс CiscoTelnet.

Для отправки строки на оборудование, каждый раз надо преобразовывать строку в байты и добавлять перевод строки.

Необходимо создать метод _write_line, который принимает как аргумент строку и отправляет на оборудование строку преобразованную в байты и добавляет перевод строки в конце.

После этого надо сменить строки, где используется метод write, на использование метода _write_line (и в методе __init__ и в методе send_show_command).

Например, вместо строки self.telnet.write(username.encode('utf-8') + b'\n'),
должна быть строка self._write_line(username).

Проверить работу переделанного класса.
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

    def _write_line(self, string):
        return self.telnet.write(string.encode('utf-8') + b'\n')


if __name__ == '__main__':
    r1 = CiscoTelnet('192.168.0.150', 'admin', 'admin', 'admin')
    print(r1.send_show_command('sh ip int br'))
