# -*- coding: utf-8 -*-
'''
Задание 8.1a

Переделать декоратор retry: добавить параметр delay, который контролирует через какое количество секунд будет выполняться повторная попытка.

'''

from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException
from time import sleep

r1_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.150',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',
}


def retry(times=1, delay=1):
    def decorator(func):
        def inner(*args, **kwargs):
            index = 0
            while times >= index:
                index += 1
                output = func(*args, **kwargs)
                if output:
                    return(output)
                sleep(delay)
        return inner
    return decorator


@retry(times=3, delay=10)
def send_show_command(device, show_command):
    print('Подключаюсь к', device['ip'])
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result
    except SSHException:
        return False


if __name__ == "__main__":
    output = send_show_command(r1_params, 'sh clock')
    print(output)
