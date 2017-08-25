#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.2

В этом задании нужно использовать функцию parse_output из задания 14.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки
команды sh ip int br (шаблон и вывод есть в разделе).
'''
from sys import argv
import textfsm
import csv

template_file = argv[1]
output_file = argv[2]
csv_file = argv[3]


def parse_output(template, output):
    with open(template) as t, open(output) as o:
        re_table = textfsm.TextFSM(t)
        header = re_table.header
        result = re_table.ParseText(o.read())
        result.insert(0, header)
    return result


def list_to_csv(params, filename):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter='|')
        for row in params:
            writer.writerow(row)


if __name__ == '__main__':
    list_to_csv(parse_output(template_file, output_file), csv_file)
