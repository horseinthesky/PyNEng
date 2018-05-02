# -*- coding: utf-8 -*-
'''
Задание 7.1

Переделать функцию netmiko_ssh таким образом, чтобы при отправке строки "close",
вместо команды, закрывалось соединение к устройству
и выводилось сообщение 'Соединение закрыто'.

'''

from netmiko import ConnectHandler

device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


def netmiko_ssh(params_dict):
    ssh = ConnectHandler(**params_dict)
    ssh.enable()
    def send_show_command(command):
        return ssh.send_command(command)
    return send_show_command


if __name__ == "__main__":
    r1 = netmiko_ssh(device_params)
    print(r1('sh clock'))

