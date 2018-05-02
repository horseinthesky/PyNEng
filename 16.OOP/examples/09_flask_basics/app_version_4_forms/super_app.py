import yaml
from flask import Flask, render_template, request, flash, redirect, url_for
import netmiko
from netmiko.ssh_exception import SSHException
from forms import SendCommandForm, YamlFilenameForm
from flask_bootstrap import Bootstrap


myapp = Flask(__name__)
myapp.config['SECRET_KEY'] = 'super-secret-key'
bootstrap = Bootstrap(myapp)



def netmiko_send_command(command, **device_params):
    try:
        with netmiko.ConnectHandler(**device_params) as ssh:
            print('Connecting to device', ssh.ip)
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


@myapp.route('/send_command', methods=['GET', 'POST'])
def send_command():
    form = SendCommandForm()
    if form.validate_on_submit():
        result = netmiko_send_command(
            command=form.command.data,
            device_type=form.device_type.data,
            ip=form.ipaddress.data,
            username=form.username.data,
            password=form.password.data,
            secret=form.enable_password.data)
        return render_template('command_output.html', command=form.command.data,
                               output=result)
    return render_template('send_command.html', form=form)


@myapp.route('/devices', methods=['GET', 'POST'])
def list_devices():
    form = YamlFilenameForm()
    if form.validate_on_submit():
        with open(form.filename.data) as f:
            devices = yaml.load(f)
        return render_template('devices_from_file.html', devices=devices)
    return render_template('devices.html', form=form)



if __name__ == '__main__':
    myapp.run(debug=True)

