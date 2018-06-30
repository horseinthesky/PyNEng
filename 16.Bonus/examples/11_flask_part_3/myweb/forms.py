from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, IPAddress



class SendCommandForm(FlaskForm):
    device_type = StringField('Device type', validators=[DataRequired()])
    ipaddress = StringField('IP address', validators=[DataRequired(), IPAddress()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    enable_password = PasswordField('Enable Password', validators=[DataRequired()])
    command = StringField('Command', validators=[DataRequired()])
    parse_textfsm = BooleanField('Parse TextFSM')
    submit = SubmitField('Send command')


class YamlFilenameForm(FlaskForm):
    filename = StringField('YAML file')
    submit = SubmitField('Send command')


class RunScript(FlaskForm):
    scriptline = StringField('Script to run', validators=[DataRequired()])
    submit = SubmitField('Run script')


class SaveToFile(FlaskForm):
    submit = SubmitField('Save output to file')


class NetworkDeviceForm(FlaskForm):
    select_device = SelectField('Select device', choices=[])
    submit = SubmitField('Select device')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

