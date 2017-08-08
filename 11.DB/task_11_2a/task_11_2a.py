#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.2a

Дополнить скрипт get_data.py из задания 11.2

Теперь должна выполняться проверка не только по количеству аргументов,
но и по значению аргументов.
Если имя аргумента введено неправильно, надо вывести сообщение об ошибке
(пример сообщения ниже).

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data_ver1.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch


"""

"""Решение"""
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'

def get_data_by_key_value(db_name, key, value):
    connection = sqlite3.connect(db_name)
    connection.row_factory = sqlite3.Row

    query = "select * from dhcp where {} = ?".format(key)
    result = connection.execute(query, (value,))

    print('\nDetailed information for host(s) with', key, value)
    print('-'*40)
    for row in result:
        keys = row.keys()
        if not key in keys:
            print("""Данный параметр не поддерживается.
                    Допустимые значения параметров: mac, ip, vlan, interface, switch""")
        else:
            keys.remove(key)
            for k in keys:
                print('{:12}: {}'.format(k, row[k]))
            print('-'*40)

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
