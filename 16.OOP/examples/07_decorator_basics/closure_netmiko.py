from netmiko import ConnectHandler

device_params1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

device_params2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


def netmiko_ssh(params_dict):
    print('Подключаюсь...')
    ssh = ConnectHandler(**params_dict)
    ssh.enable()
    def send_show_command(command):
        print('Отправляю команду', command)
        return ssh.send_command(command)
    return send_show_command


if __name__ == "__main__":

    r1 = netmiko_ssh(device_params1)
    print(r1('sh clock'))

    r2 = netmiko_ssh(device_params2)
    print(r2('sh clock'))

