#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from my_func import *

access_dict, trunk_dict = get_int_vlan_map('config_sw1.txt')

access_config = generate_access_config(access_dict)
trunk_config = generate_trunk_config(trunk_dict)

access_config_n = [line + '\n' for line in access_config]
trunk_config_n = [line + '\n' for line in trunk_config]

with open('result.txt', 'w') as f:
    f.writelines(access_config_n)
    f.writelines(trunk_config_n)
    f.close()
