#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sqlite3

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

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

create_db(db_filename,schema_filename)
