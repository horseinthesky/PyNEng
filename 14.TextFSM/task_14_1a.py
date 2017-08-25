#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.1a

Переделать функцию parse_output из задания 14.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.
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
        result_dict = {}
        for i in range(len(header)):
            column = [el[i] for el in result]
            result_dict[header[i]] = column
    return result_dict


if __name__ == '__main__':
    print(tabulate(parse_output(template_file, output_file), headers='keys'))
