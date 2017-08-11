#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import glob
import re
import sqlite3
import yaml
import os
from datetime import timedelta, datetime

dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

def create_db(db_name, schema):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print('Creating schema...')
        with open(schema, 'r') as f:
            schema_f = f.read()
            connection = sqlite3.connect(db_name)
            connection.executescript(schema_f)
            print('Done')
            connection.close()
    else:
        print('Database exists, assume dhcp table does, too.')

def add_data_switches(db_name, switches_list):
    query_switches = 'replace into switches values (?,?)'
    for sw in switches_list:
        with open(sw) as f:
            switches = yaml.load(f)
            sw_data = list(switches['switches'].items())
            add_data(db_name, query_switches, sw_data)

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

def get_data(db_name, key, value):
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
    connection = sqlite3.connect(db_name)
    for line in connection.execute('select * from dhcp;'):
        print(f.format(*line))
