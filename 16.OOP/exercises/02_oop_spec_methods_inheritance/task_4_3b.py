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

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.150',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin'
}


# Решение
class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.ip = device_params['ip']
        self.enable()

    def _check_error_in_command(self, command, command_output):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        for error in errors:
            if error in command_output:
                raise ErrorInCommand('''При выполнении команды "{}" на устройстве {} возникла ошибка {}'''.format(command, self.ip, error))

    def send_command(self, command):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, command):
        command_output = super().send_config_set(command)
        self._check_error_in_command(command, command_output)
        return command_output


class ErrorInCommand(Exception):
    """При выполнении команды возникла ошибка"""
