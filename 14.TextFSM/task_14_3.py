#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.3

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding.
Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* MacAddress
* IpAddress
* VLAN
* Interface

Проверить работу шаблона с помощью функции из задания 14.1.
'''
from sys import argv
from tabulate import tabulate
import textfsm

template_file = argv[1]
output_file = argv[2]


def parse_output(template, output):
    with open(template) as t, open(output) as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        result = re_table.ParseText(o.read())
        result.insert(0, header)
    return result


if __name__ == '__main__':
    headers, *routes = parse_output(template_file, output_file)
    print(tabulate(routes, headers=headers))
