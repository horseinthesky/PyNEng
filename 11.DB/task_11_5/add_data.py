#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.5

Теперь в БД остается и старая информация.
И, если какой-то MAC-адрес не появлялся в новых записях, запись с ним,
может оставаться в БД очень долго.

И, хотя это может быть полезно, чтобы посмотреть, где MAC-адрес находился в последний раз,
постоянно хранить эту информацию не очень полезно.

Например, если запись в БД уже больше месяца, то её можно удалить.

Для того, чтобы сделать такой критерий, нужно ввести новое поле,
в которое будет записываться последнее время добавления записи.

Новое поле называется last_active и в нем должна находиться строка,
в формате: ```YYYY-MM-DD HH:MM:SS```.

В этом задании необходимо:
* изменить, соответственно, таблицу dhcp и добавить новое поле.
 * таблицу можно поменять из cli sqlite, но файл dhcp_snooping_schema.sql тоже необходимо изменить
* изменить скрипт add_data.py, чтобы он добавлял к каждой записи время

Как получить строку со временем и датой, в указанном формате, показано в задании.
Раскомментируйте строку и посмотрите как она выглядит.

"""

"""Решение"""
import glob
import re
import sqlite3
import yaml
import os
import datetime

date = str(datetime.datetime.today().replace(microsecond=0))
db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

def parse_dhcp_snoop(filename):
    sw = filename.split('_')[0]
    with open(filename) as f:
        result = [match.groups()+(sw,) + (date,) + (1,) for match in regex.finditer(f.read())]
    return result

def add_data(db, query, data):                                  
    db_exist = os.path.exists(db)                               
    if db_exist:                                                
        connection = sqlite3.connect(db)                        
        try:                                                    
            with connection:                                    
                connection.executemany(query,data)              
        except sqlite3.IntegrityError as err:                   
            print('Error occured:', err)                        
            from pprint import pprint                           
            print('Error caused by data:')                      
            pprint(data)                                        
        finally:                                                
            connection.close()                                  
    else:                                                       
        print('Database doesn\'t exists. Please create it first.') 

def update_dhcp_data(filename, db):
    sw = filename.split('_')[0]
    update_query = 'update dhcp set active = "0" where switch = (?)'
    with sqlite3.connect(db) as conn:
        conn.execute(update_query, (sw,))

def add_sw_data(db_name, sw_data_file):
    query_switches = 'replace into switches values (?,?)'
    with open(sw_data_file) as f:
        switches = yaml.load(f)
        sw_data = list(switches['switches'].items())
        add_data(db_name, query_switches, sw_data)

def add_dhcp_data(db_name, data_files):
    query = "replace into dhcp values (?, ?, ?, ?, ?, ?, ?)"
    for filename in data_files:
        if sqlite3.connect(db_filename).execute('select * from dhcp').fetchone():
            update = update_dhcp_data(filename, db_name) 
        result = parse_dhcp_snoop(filename)
        add_data(db_name, query, result)

if __name__ == '__main__':
    add_sw_data(db_filename, 'switches.yml')
    add_dhcp_data(db_filename, dhcp_snoop_files)
