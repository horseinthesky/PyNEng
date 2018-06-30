from netmiko import ConnectHandler
import logging

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


def ssh_with_logging(log_level):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def netmiko_ssh(params_dict):
        logging.info('Подключаюсь...')
        ssh = ConnectHandler(**params_dict)
        ssh.enable()
        def send_show_command(command):
            logging.info('Отправляю команду %s', command)
            return ssh.send_command(command)
        return send_show_command
    return netmiko_ssh

if __name__ == "__main__":
    verbose_ssh = ssh_with_logging(logging.INFO)

    r1 = verbose_ssh(device_params1)
    print(r1('sh clock'))

    r2 = verbose_ssh(device_params2)
    print(r2('sh clock'))

