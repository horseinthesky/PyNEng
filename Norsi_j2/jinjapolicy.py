#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import re

env = Environment(loader=FileSystemLoader('templates'))
address_template = env.get_template('addresses.j2')
policy_template = env.get_template('policy.j2')

regex = re.compile(r'set policy id \d+ .*"(10.\d+.\d+.\d+)/(\d+)" .*')


def convert_netmask_to_octets(netmask):
    bitline = int(netmask) * '1' + (32 - int(netmask)) * '0'
    return str(int(bitline[:8], 2)) + '.' + str(int(bitline[8:16], 2)) + '.' + str(int(bitline[16:24], 2)) + '.' + str(int(bitline[24:], 2))


def write_data(filename, data):
    with open(filename, 'a') as f:
        f.write(data)


with open('sg.txt') as f:
    i = 0
    for line in f:
        match = regex.search(line)
        if match:
            i += 1
            subnet, netmask = match.groups()
            policy_dict = {'policy_number': int(i),
                           'subnet': subnet,
                           'netmask': netmask,
                           'octet_mask': convert_netmask_to_octets(netmask),
                           }
            write_data('addresses.txt', address_template.render(policy_dict))
            write_data('policy.txt', policy_template.render(policy_dict))
