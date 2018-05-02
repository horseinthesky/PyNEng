import subprocess
import textfsm
import yaml
import netmiko
from netmiko.ssh_exception import SSHException


def netmiko_send_command(command, **device_params):
    try:
        with netmiko.ConnectHandler(**device_params) as ssh:
            print('Connecting to device', ssh.ip)
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except SSHException as error:
        return error


def parse_textfsm(output, template_filename):

    template = open(template_filename)
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)
    return [fsm.header] + result


def run_script_get_stdout(script_to_run_line):
    result = subprocess.run(script_to_run_line, shell=True,
			    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
			    encoding='utf-8')
    return result.stderr+result.stdout

