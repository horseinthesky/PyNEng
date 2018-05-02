# -*- coding: utf-8 -*-
'''
Задание 7.4

Создать декоратор add_verbose, который добавляет в функцию
дополнительный параметр verbose.
Когда параметру передано значение True, на стандартный поток вывода
должна отображаться информация о вызове функции и ее параметрах
(пример работы декоратора показан ниже).

По умолчанию, значение параметра должно быть равным False.

Проверить работу декоратора на функции send_show_command.

Пример вывода:
In [3]: @add_verbose
   ...: def send_show_command(params, command):
   ...:     with ConnectHandler(**params) as ssh:
   ...:         ssh.enable()
   ...:         result = ssh.send_command(command)
   ...:     return result
   ...:

In [4]: print(send_show_command(device_params, 'sh clock', verbose=True))
Вызываем send_show_command
Позиционные аргументы: ({'device_type': 'cisco_ios', 'ip': '192.168.100.1', 'username': 'cisco', 'password': 'cisco', 'secret': 'cisco'}, 'sh clock')
*14:01:07.353 UTC Mon Feb 26 2018

In [5]: print(send_show_command(device_params, 'sh clock', verbose=False))
*14:01:18.141 UTC Mon Feb 26 2018
'''

from netmiko import ConnectHandler

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}



def send_show_command(params, command):
    with ConnectHandler(**params) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


