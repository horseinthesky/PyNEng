#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.3
"""
import glob
import re
import sqlite3
import yaml
import os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

def parse_dhcp_snoop(filename):
    sw = filename.split('_')[0]
    with open(filename) as f:
        result = [match.groups()+(sw,) + (1,) for match in regex.finditer(f.read())]
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
    query = "replace into dhcp values (?, ?, ?, ?, ?, ?)"
    for filename in data_files:
        update = update_dhcp_data(filename, db_name) 
        result = parse_dhcp_snoop(filename)
        add_data(db_name, query, result)

if __name__ == '__main__':
    add_sw_data(db_filename, 'switches.yml')
    add_dhcp_data(db_filename, dhcp_snoop_files)
