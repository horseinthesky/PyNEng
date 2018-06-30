from netmiko import ConnectHandler
import yaml
from functools import singledispatch
from collections.abc import Sequence


@singledispatch
def send_commands(command, device):
    print('Original send_commands')
    raise NotImplementedError('Поддерживается только список или строка')

# @send_commands.register(tuple)
@send_commands.register(list)
def _(config_commands, device):
    print('Выполняем config')
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


@send_commands.register(str)
def _(show_command, device):
    print('Выполняем show')
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show_command)
    return result


commands = ['logging 10.255.255.1',
            'logging buffered 20010',
            'no logging console']

show_command = "sh ip int br"


if __name__ == "__main__":
    with open('device.yaml') as f:
        r1 = yaml.load(f)

    #print(send_commands(commands, r1))
    print(send_commands(show_command, r1))
    #print(send_commands(('logging 10.255.255.1',), r1))
