# -*- coding: utf-8 -*-

'''
Задание 4.3b

Дополнить класс MyNetmiko из задания 4.3a.

Переписать метод send_config_set netmiko, добавив в него проверку на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает вывод команд.

In [2]: from task_4_3b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

'''
from netmiko.cisco.cisco_ios import CiscoIosBase
import re


device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.150',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}


# Решение
class ErrorInCommand(Exception):
    """При выполнении команды возникла ошибка"""


class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = '^.+\n(.*\n)*% (?P<err>.+)'
        message = ('При выполнении команды "{cmd}" на устройстве {device} '
                   'возникла ошибка "{error}"')
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            raise ErrorInCommand(
                message.format(
                    cmd=command, device=self.ip, error=error_in_cmd.group('err')))

    def send_command(self, command):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ''
        self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output += result
            self._check_error_in_command(command, result)
        self.exit_config_mode()
        return commands_output
