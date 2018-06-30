import yaml
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import netmiko
from netmiko.ssh_exception import SSHException

myapp = Flask(__name__)
bootstrap = Bootstrap(myapp)


def netmiko_send_command(device_params, command):
    try:
        with netmiko.ConnectHandler(**device_params) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except SSHException as error:
        return error


@myapp.route('/')
@myapp.route('/home')
@myapp.route('/index')
def index():
    return render_template('index.html')


@myapp.route('/send_command/<device_ip>/<command>')
def send_command(device_ip, command):
    with open('devices_by_ip.yaml') as f:
        devices = yaml.load(f)
    device_params = devices.get(device_ip)
    result = None
    if device_params:
        result = netmiko_send_command(device_params, command)
    return render_template(
        'send_command.html', device_ip=device_ip,
        command=command, command_output=result)


@myapp.route('/devices')
def list_devices():
    with open('devices.yaml') as f:
        devices = yaml.load(f)
    return render_template('devices.html', devices=devices)


if __name__ == '__main__':
    myapp.run(debug=True)

