#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 13.1d

Переделать функцию generate_cfg_from_template из задания 13.1, 13.1a, 13.1b или 13.1c:
* сделать автоматическое распознавание разных форматов для файла с данными
* для передачи разных типов данных, должен использоваться один и тот же параметр data

Должны поддерживаться такие форматы:
* YAML - файлы с расширением yml или yaml
* JSON - файлы с расширением json
* словарь Python

Если не получилось определить тип данных, вывести сообщение error_message (перенести текст сообщения в тело функции), завершить работу функции и вернуть None.

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


def generate_cfg_from_template(path, config, **kwargs):
    env = Environment(loader=FileSystemLoader([os.getcwd(), path.split('/')[0]]), **kwargs)
    template = env.get_template(path.split('/')[1])
    if type(config) is dict:
        config_dict = config
    elif config.endswith('.yml') or config.endswith('.yaml'):
        config_dict = yaml.load(open(config))
    elif config.endswith('.json'):
        config_dict = json.load(open(config))
    else:
        error_message = '''
        Не получилось определить формат данных.
        Поддерживаются файлы с расширением .json, .yml, .yaml и словари Python
        '''
        print(error_message)
        return
    result = template.render(config_dict)

    return result


if __name__ == '__main__':
    data_yaml = 'data_files/for.yml'
    data_json = 'data_files/for.json'
    template = 'templates/for.txt'

    print(generate_cfg_from_template(template, data_yaml, trim_blocks=True))
    print(generate_cfg_from_template(template, data_json, trim_blocks=True))
    print(generate_cfg_from_template(template, data_dict, trim_blocks=True))
    print(generate_cfg_from_template(template, 'error.txt', trim_blocks=True))
