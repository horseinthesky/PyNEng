import netmiko
import re

DEVICE_PARAMS = {
        'device_type': 'cisco_ios',
        'ip': '192.168.100.1',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'
}


class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()


r1 = CiscoSSH(**DEVICE_PARAMS)
print(r1.ssh)
print(r1.ssh.send_command('sh ip int br'))


## Создание метода
class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)



r1 = CiscoSSH(**DEVICE_PARAMS)
print(r1.ssh.send_command('sh ip int br'))
print(r1.send_show_command('sh ip int br'))


### Специальный метод __str__

class CiscoSSH:
    def __init__(self, **device_params):
        self._device_params = device_params
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def __str__(self):
        return 'Connection to {}'.format(self._device_params['ip'])


### Атрибут класса

class CiscoSSH:
    known_devices = {}

    def __init__(self, **device_params):
        self._device_params = device_params
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        CiscoSSH.known_devices[device_params['ip']] = device_params.copy()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

r1 = CiscoSSH(**DEVICE_PARAMS)
print(r1.known_devices)
print(CiscoSSH.known_devices)

r2_params = {'device_type': 'cisco_ios',
 'ip': '192.168.100.2',
 'password': 'cisco',
 'secret': 'cisco',
 'username': 'cisco'}

r2 = CiscoSSH(**r2_params)
print(CiscoSSH.known_devices)


### Менеджер контекта (with)

with netmiko.ConnectHandler(**DEVICE_PARAMS) as ssh:
    ssh.send_command('sh ip int br')

print(ssh.is_alive())


### добавление методов __enter__, __exit__

class CiscoSSH:
    def __init__(self, **device_params):
        self._device_params = device_params
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        print('CiscoSSH __init__ called')

    def __enter__(self):
        print('CiscoSSH __enter__ called')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print('CiscoSSH __exit__ called')
        self.ssh.disconnect()


with CiscoSSH(**DEVICE_PARAMS) as r1:
    print('Внутри with')
    print(r1.ssh.send_command('sh ip int br'))


### обработка исключение в exit

class CiscoSSH:
    def __init__(self, **device_params):
        self._device_params = device_params
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        print('CiscoSSH __init__ called')

    def __enter__(self):
        print('CiscoSSH __enter__ called')
        return self

    def __exit__(self, *args):
        print('CiscoSSH __exit__ called')
        print(args)
        self.ssh.disconnect()
        return True



with CiscoSSH(**DEVICE_PARAMS) as r1:
    print('Внутри with')
    print(r1.ssh.send_command('sh ip int br'))
    raise ValueError('Ошибкаааааа')


### __getattr__

class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def __getattr__(self, attr):
        if attr == 'sh_version':
            print('Создаю атрибут sh_version')
            output = self.ssh.send_command('sh version')
            self.sh_version = re.search('Version (.*?),', output).group(1)
            return self.sh_version


r1 = CiscoSSH(**DEVICE_PARAMS)

print(r1.sh_version)
print(r1.sh_version)

### Добавление исключения для остальных атрибутов
class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def __getattr__(self, attr):
        if attr == 'sh_version':
            print('Создаю атрибут sh_version')
            output = self.ssh.send_command('sh version')
            self.sh_version = re.search('Version (.*?),', output).group(1)
            return self.sh_version
        else:
            raise AttributeError("'CiscoSSH' object has no attribute '{}'".format(attr))



r1 = CiscoSSH(**DEVICE_PARAMS)

print(r1.sh_version)
print(r1.sh_clock)

