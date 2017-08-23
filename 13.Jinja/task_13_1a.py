#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 13.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import os


def generate_cfg(path, config):
    env = Environment(loader=FileSystemLoader([os.getcwd(), path.split('/')[0]]), trim_blocks=True)
    template = env.get_template(path.split('/')[1])
    config_dict = yaml.load(open(config))
    result = template.render(config_dict)

    return result


if __name__ == '__main__':
    data_file = 'data_files/for.yml'
    template = 'templates/for.txt'

    print(generate_cfg(template, data_file))
