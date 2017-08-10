#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.4

Обновить файл get_data из задания 11.2 или 11.2a.
Добавить поддержку столбца active, который мы добавили в задании 11.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные.

Например:
```
$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
----------------------------------------

=======================================
Inactive values:
----------------------------------------
mac         : 00:09:23:34:16:18
vlan        : 10
interface   : FastEthernet0/4
----------------------------------------
```
"""

"""Решение"""
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

def get_data_by_key_value(db_name, key, value):
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row

    query_all = 'select * from dhcp;'
    keys = connection.execute(query_all).fetchone().keys()

    if not key in keys:
        print('Данный параметр не поддерживается.',
              'Допустимые значения параметров: {}'.format(', '.join(keys)),
              sep='\n')
    else:
        keys.remove(key)
        query_active = "select * from dhcp where {} = ? and active = 1 ORDER BY active DESC".format(key)
        result_active = connection.execute(query_active, (value,))
        print('\nDetailed information for host(s) with', key, value)
        print('-'*80)
        for row in result_active:
            print('\n'.join('{:12}: {}'.format(k, row[k]) for k in keys[:-1]))
            print('-'*80)

        query_inactive = "select * from dhcp where {} = ? and active = 0 ORDER BY active DESC".format(key)
        result_inactive = connection.execute(query_inactive, (value,))
        print('\n' + '='*80, 'Inactive values:', '-'*80, sep='\n')
        for row in result_inactive:
            print('\n'.join('{:12}: {}'.format(k, row[k]) for k in keys[:-1]))
            print('-'*80)

def get_all_data(db_name):
    f = '{:17}  {:17} {:4}  {:17}  {:17}'
    print('В таблице dhcp такие записи:')
    print('-'*80)
    connection = sqlite3.connect(db_filename)
    for line in connection.execute('select * from dhcp;'):
        print(f.format(*line))

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0:
        get_all_data(db_filename)
    elif len(args) == 2:
        key, value = args
        get_data_by_key_value(db_filename, key, value)
    else:
        print('Пожалуйста, введите два или ноль аргументов')
