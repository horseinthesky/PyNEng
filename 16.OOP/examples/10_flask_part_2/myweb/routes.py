import os
import yaml
from flask import render_template, request, flash, redirect, url_for, session
from myweb import myapp
from myweb.forms import SendCommandForm, YamlFilenameForm, RunScript, SaveToFile
from myweb.helper_functions import (netmiko_send_command, parse_textfsm,
                                    run_script_get_stdout)


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
        if form.parse_textfsm.data:
            result = parse_textfsm(result, 'textfsm_templates/sh_ip_int_br.template')
        session['command'] = form.command.data
        session['command_output'] = result
        return redirect(url_for('command_output'))
    return render_template('send_command.html', form=form)


@myapp.route('/run_script', methods=['GET', 'POST'])
def run_script():
    form = RunScript()
    if form.validate_on_submit():
        script_stdout = run_script_get_stdout(form.scriptline.data)
        session['command_output'] = script_stdout
        session['command'] = form.scriptline.data
        return redirect(url_for('command_output'))
    return render_template('run_script.html', form=form)


@myapp.route('/command_output', methods=['GET', 'POST'])
def command_output():
    form = SaveToFile()
    if form.validate_on_submit():
        with open(form.dest_file.data, 'w', encoding='utf-8') as f:
            if not type(session.get('command_output')) is str:
                yaml.dump(session.get('command_output'), f)
            else:
                f.write(session.get('command_output'))
        session.clear()
        #return render_template('success.html',
        #                       message='Файл {} успешно сохранен'.format(
        #                           os.path.abspath(form.dest_file.data)))
        flash('Файл {} успешно сохранен'.format(
              os.path.abspath(form.dest_file.data)))
        return redirect(url_for('run_script'))
    return render_template('command_output.html', form=form,
                           command=session.get('command'),
                           output=session.get('command_output'))



@myapp.route('/devices', methods=['GET', 'POST'])
def list_devices():
    form = YamlFilenameForm()
    if form.validate_on_submit():
        with open(form.filename.data) as f:
            devices = yaml.load(f)
        return render_template('devices_from_file.html', devices=devices)
    return render_template('devices.html', form=form)

