#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.4

На основе примера textfsm_clitable.py из раздела TextFSM
сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера,
     который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 14.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

Пример из раздела:
'''
from tabulate import tabulate
import clitable

output_sh_ip_int_br = open('output/sh_ip_int_br.txt').read()
attributes_dict = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}


def parse_command_dynamic(attributes, output, index='index', templates='templates'):
    cli_table = clitable.CliTable(index, templates)
    cli_table.ParseCmd(output_sh_ip_int_br, attributes)

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)

    result = {}
    for i in range(len(header)):
        column = [el[i] for el in data_rows]
        result[header[i]] = column
    return result


if __name__ == '__main__':
    print(tabulate(parse_command_dynamic(attributes_dict, output_sh_ip_int_br), headers='keys'))
