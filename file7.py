#!/usr/bin/env python
# -*- coding: utf-8 -*-

username = raw_input('Введите имя пользователя: ' )
password = raw_input('Введите пароль: ' )

if len(password) < 8:
    print 'Пароль слишком короткий'
elif username in password:
    print 'Пароль содержит имя пользователя'
else:
    print 'Пароль для пользователя %s установлен' % username

