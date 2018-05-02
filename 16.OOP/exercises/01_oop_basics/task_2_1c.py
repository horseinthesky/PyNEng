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


