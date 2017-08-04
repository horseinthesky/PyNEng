#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.1

* create_db.py
 * сюда должна быть вынесена функциональность по созданию БД:
  * должна выполняться проверка наличия файла БД
  * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
    должна быть создана БД (БД отличается от примера в разделе)

В БД теперь будут две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

"""

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

"""Решение"""
import sqlite3
import os

db_exist = os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

def schema_create():
    if not db_exist:
        print('Creating schema...')
        with open(schema_filename) as f:
            schema = f.read()
        conn.executescript(schema)
        print('Done')
    else:
        print('Database exist, assume dhcp table does, too.')

schema_create()
