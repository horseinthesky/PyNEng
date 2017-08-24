#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 14.1

Переделать пример, который использовался в разделе TextFSM, в функцию.

Функция должна называться parse_output. Параметры функции:
* template - шаблон TextFSM (это должно быть имя файла, в котором находится шаблон)
* output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов (в примере ниже, находится в переменной header)
* остальные элементы это списки, в котором находятся результаты обработки вывода (в примере ниже, находится в переменной result)

Проверить работу функции на каком-то из примеров раздела.

Пример из раздела:
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
    return [header] + result


if __name__ == '__main__':
    headers, *routes = parse_output(template_file, output_file)
    print(tabulate(routes, headers=headers))
