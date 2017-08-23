#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 13.3b

Измените шаблон templates/ospf.txt из задания 13.3a таким образом,
чтобы для перечисленных переменных были указаны значения по умолчанию,
которые используются в том случае, если переменная не задана или,
если в переменной пустое значение.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf3.yml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.

'''
from task_13_1d import generate_cfg_from_template
import yaml

router_info = {'hostname': 'R1'}

if __name__ == '__main__':
    template = 'templates/ospf.txt'
    ospf_dict = yaml.load('data_files/ospf3.yml')

    print(generate_cfg_from_template(template, ospf_dict, trim_blocks=True, lstrip_blocks=True))
