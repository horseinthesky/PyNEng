#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.4a

Переделать функцию из задания 14.4:
* добавить аргумент show_output, который контролирует будет ли выводится результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться с помощью FormattedTable (пример есть в разделе)

'''
from tabulate import tabulate
import clitable

output_sh_ip_int_br = open('output/sh_ip_int_br.txt').read()
attributes_dict = {'Command': 'show ip int br', 'Vendor': 'cisco_ios'}


def parse_command_dynamic(attributes, output, show_output=False, index='index', templates='templates'):
    cli_table = clitable.CliTable(index, templates)
    cli_table.ParseCmd(output_sh_ip_int_br, attributes)

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)

    if show_output:
        print('Formatted Table:\n', cli_table.FormattedTable())

    result = {}
    for i in range(len(header)):
        column = [el[i] for el in data_rows]
        result[header[i]] = column
    return result


if __name__ == '__main__':
    print(tabulate(parse_command_dynamic(attributes_dict, output_sh_ip_int_br, True), headers='keys'))
