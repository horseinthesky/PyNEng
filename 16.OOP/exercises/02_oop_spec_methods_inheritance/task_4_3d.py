# -*- coding: utf-8 -*-

'''
Задание 4.3d

Дополнить класс MyNetmiko из задания 4.3c или задания 4.3b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен работать точно так же как метод send_config_set в netmiko.

Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_4_3d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

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

    def send_command(self, command, *agrs, **kwargs):
        command_output = super().send_command(command)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, command, ignore_errors=True):
        command_output = super().send_config_set(command)
        if not ignore_errors:
            self._check_error_in_command(command, command_output)
        return command_output


class ErrorInCommand(Exception):
    """При выполнении команды возникла ошибка"""
