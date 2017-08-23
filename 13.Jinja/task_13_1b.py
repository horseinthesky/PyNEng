#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 13.1b

Дополнить функцию generate_cfg_from_template из задания 13.1 или 13.1a:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''
from jinja2 import Environment, FileSystemLoader
import yaml
import os


def generate_cfg_from_template(path, config, **kwargs):
    env = Environment(loader=FileSystemLoader([os.getcwd(), path.split('/')[0]]), **kwargs)
    template = env.get_template(path.split('/')[1])
    config_dict = yaml.load(open(config))
    result = template.render(config_dict)

    return result


if __name__ == '__main__':
    data_file = 'data_files/for.yml'
    template = 'templates/for.txt'

    print(generate_cfg_from_template(template, data_file, trim_blocks=True, lstrip_blocks=True))
    print(generate_cfg_from_template(template, data_file, trim_blocks=False, lstrip_blocks=True))
    print(generate_cfg_from_template(template, data_file, trim_blocks=True, lstrip_blocks=False))
