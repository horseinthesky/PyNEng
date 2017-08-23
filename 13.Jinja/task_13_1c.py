#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 13.1c

Дополнить функцию generate_cfg_from_template из задания 13.1, 13.1a или 13.1b:
* добавить поддержку разных форматов для файла с данными

Должны поддерживаться такие форматы:
* YAML
* JSON
* словарь Python

Сделать для каждого формата свой параметр функции.
Например:
* YAML - yaml_file
* JSON - json_file
* словарь Python - py_dict

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import os
import json

data_dict = {'vlans': {
                        10: 'Marketing',
                        20: 'Voice',
                        30: 'Management'},
             'ospf': [{'network': '10.0.1.0 0.0.0.255', 'area': 0},
                      {'network': '10.0.2.0 0.0.0.255', 'area': 2},
                      {'network': '10.1.1.0 0.0.0.255', 'area': 0}],
             'id': 3,
             'name': 'R3'}


def generate_cfg_from_template(path, config, yaml_file=False, json_file=False, py_dict=False, **kwargs):
    env = Environment(loader=FileSystemLoader([os.getcwd(), path.split('/')[0]]), **kwargs)
    template = env.get_template(path.split('/')[1])
    if yaml_file:
        config_dict = yaml.load(open(config))
    elif json_file:
        config_dict = json.load(open(config))
    elif py_dict:
        config_dict = config
    else:
        print('Unknown data type')
        return
    result = template.render(config_dict)

    return result


if __name__ == '__main__':
    data_yaml = 'data_files/for.yml'
    data_json = 'data_files/for.json'
    template = 'templates/for.txt'

    print(generate_cfg_from_template(template, data_yaml, yaml_file=True, trim_blocks=True))
    print(generate_cfg_from_template(template, data_json, json_file=True, trim_blocks=True))
    print(generate_cfg_from_template(template, data_dict, py_dict=True, trim_blocks=True))
