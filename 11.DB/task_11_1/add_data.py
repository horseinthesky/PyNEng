#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import glob
import re
import sqlite3
import yaml

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

def parse_dhcp_snoop(filename):
    sw = filename.split('_')[0]
    with open(filename) as f:
        result = [match.groups()+(sw,) for match in regex.finditer(f.read())]
    return result

def add_data(db, query, data):
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

def add_sw_data(db_name, sw_data_file):
    query_switches = 'insert into switches values (?,?)'
    with open(sw_data_file) as f:
        switches = yaml.load(f)
        sw_data = list(switches['switches'].items())
        add_data(db_name, query_switches, sw_data)

def add_dhcp_data(db_name, data_files):
    query = "insert into dhcp values (?, ?, ?, ?, ?)"
    for filename in data_files:
        result = parse_dhcp_snoop(filename)
        add_data(db_name, query, result)

if __name__ == '__main__':
    add_sw_data(db_filename, 'switches.yml')
    add_dhcp_data(db_filename, dhcp_snoop_files)

