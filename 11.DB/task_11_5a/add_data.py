#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.5a

После выполнения задания 11.5, в таблице dhcp есть новое поле last_active.

Обновите скрипт add_data.py, таким образом, чтобы он удалял все записи,
которые были активными более 7 дней назад.

Для того, чтобы получить такие записи, можно просто вручную обновить поле last_active.

В файле задания описан пример работы с объектами модуля datetime.
Обратите внимание, что объекты, как и строки с датой, которые пишутся в БД,
можно сравнивать между собой.

"""

"""Решение"""
import glob
import re
import sqlite3
import yaml
import os
import datetime
from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days = 7)

date = str(datetime.today().replace(microsecond=0))
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

def delete_old_data(db_name, amount_of_days):
    query_all = 'select * from dhcp'
    delete_query = 'delete from dhcp where last_active = ?'
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        keys = conn.execute(query_all).fetchone().keys()
        result = conn.execute(query_all)

        dates = []
        for row in result:
            for k in keys:
                if k == 'last_active': 
                    dates.append(row[k])

        old_data = []
        for el in dates:
            if el < str(now - timedelta(days = amount_of_days)):
                old_data.append(el)

        for el in old_data:
            conn.execute(delete_query, (el,))

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
    if sqlite3.connect(db_filename).execute('select * from dhcp').fetchone():
        delete_old_data(db_filename, 7)
    add_sw_data(db_filename, 'switches.yml')
    add_dhcp_data(db_filename, dhcp_snoop_files)
