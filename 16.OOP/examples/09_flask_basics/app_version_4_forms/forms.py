from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, IPAddress



class SendCommandForm(FlaskForm):
    device_type = StringField('Device type', validators=[DataRequired()])
    ipaddress = StringField('IP address', validators=[DataRequired(), IPAddress()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    enable_password = PasswordField('Enable Password', validators=[DataRequired()])
    command = StringField('Command', validators=[DataRequired()])
    submit = SubmitField('Send command')


class YamlFilenameForm(FlaskForm):
    filename = StringField('YAML file')
    submit = SubmitField('Send command')
