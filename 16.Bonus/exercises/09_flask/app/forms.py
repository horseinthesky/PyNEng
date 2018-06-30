#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
