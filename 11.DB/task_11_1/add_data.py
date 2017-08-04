#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 11.1

* add_data.py
 * с помощью этого скрипта, мы будем добавлять данные в БД
  * теперь у нас есть не только данные из вывода sh ip dhcp snooping binding,
    но и информация о коммутаторах

Соответственно, в файле add_data.py у нас будет две части:
* запись информации о коммутаторах в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* запись информации на основании вывода sh ip dhcp snooping binding
 * теперь у нас есть вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch,
   нам нужно его заполнять. Имя коммутатора мы определяем по имени файла с данными

"""

import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print dhcp_snoop_files

"""Решение"""
import re
import sqlite3
import yaml
import pprint

con = sqlite3.connect(db_filename)

regex = '(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)'

switches_data = []

with open('switches.yml') as f:
    switches = yaml.load(f)
    for sw in switches['switches']:
        x = (sw, switches['switches'][sw])
        switches_data.append(x)

dhcp_data = []

for box in dhcp_snoop_files:
    with open(box) as f:
        hostname = box.split('_')[0]
        for line in f:
            match = re.search(regex, line)
            if match:
                b = [i for i in match.groups()]
                b.append(hostname)
                dhcp_data.append(tuple(b))

def insert_switches_data():
    for row in switches_data:
        try:
            with con:
                query = """insert into switches (hostname, location)
                        values (?, ?)"""
                con.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

def insert_dhcp_data():
    for row in dhcp_data:
        try:
            with con:
                query = """insert into dhcp (mac, ip, vlan, interface, switch)
                        values (?, ?, ?, ?, ?)"""
                con.execute(query, row)
        except sqlite3.IntegrityError as e:
            print("Error occured: ", e)

insert_switches_data()
insert_dhcp_data()
