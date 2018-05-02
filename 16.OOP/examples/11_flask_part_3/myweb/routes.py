import os
import json
import yaml
from flask import (render_template, request, flash, redirect, url_for, session,
                   send_file)
from myweb import myapp, db
from myweb.forms import (SendCommandForm, YamlFilenameForm, RunScript,
                         SaveToFile, NetworkDeviceForm, LoginForm)
from myweb.models import NetworkDevice, User
from myweb.helper_functions import (netmiko_send_command, parse_textfsm,
                                    run_script_get_stdout)
from flask_login import current_user, login_user, logout_user, login_required
from io import BytesIO


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
    cmd_output = session.get('command_output')
    if form.validate_on_submit():
        filetype = '.txt'
        if not type(cmd_output) is str:
            cmd_output = json.dumps(cmd_output)
            filetype = '.json'
        buffer = BytesIO()
        buffer.write(cmd_output.encode('utf-8'))
        buffer.seek(0)
        session.clear()
        return send_file(buffer, as_attachment=True,
                         attachment_filename='output'+filetype)
    return render_template('command_output.html', form=form,
                           command=session.get('command'),
                           output=cmd_output)



@myapp.route('/devices', methods=['GET', 'POST'])
def list_devices():
    form = YamlFilenameForm()
    if form.validate_on_submit():
        with open(form.filename.data) as f:
            devices = yaml.load(f)
        return render_template('devices_from_file.html', devices=devices)
    return render_template('devices.html', form=form)


@myapp.route('/select_device', methods=['GET', 'POST'])
@login_required
def select_device():
    form = NetworkDeviceForm()
    form.select_device.choices = [(dev.hostname, dev.hostname)
                                  for dev in NetworkDevice.query.all()]

    if form.validate_on_submit():
        flash('Device selected: {}: {}'.format(
            request.form['select_device'],
            NetworkDevice.query.filter(
                NetworkDevice.hostname==request.form['select_device']).first()))
        return redirect(url_for('index'))
    return render_template('select_device.html', form=form)



@myapp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.password == form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@myapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
