#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import yaml

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

def generate_access_config(access, psecurity=False):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}
    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    for intf in access:
        result.append('interface ' + intf)
        with open('sw_templates.yaml') as f:
            templates = yaml.load(f)
            for command in templates['access']:
                if command.endswith('vlan'):
                    result.append(' {} {}'.format(command, access[intf]))
                else:
                    result.append(' {}'.format(command))
            if psecurity:
                result.extend(templates['psecurity'])

    return result

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    for intf in trunk:
        result.append('interface ' + intf)
        with open('sw_templates.yaml') as f:
            templates = yaml.load(f)
            for command in templates['trunk']:
                if command.endswith('alloved vlan'):
                    vlans = ','.join(str(vlan) for vlan in trunk[intf])
                    result.append(' {} {}'.format(command, vlans))
                else:
                    result.append(' {}'.format(command))

    return result

def generate_ospf_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон ospf.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    with open(filename) as f:
        templates = yaml.load(f)
        for command in templates['ospf']:
            result.append(command)

    return result

def generate_mngmt_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон mngmt.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    with open(filename) as f:
        templates = yaml.load(f)
        for command in templates['mngmt']:
            result.append(command)

    return result

def generate_alias_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон alias.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    with open(filename) as f:
        templates = yaml.load(f)
        for command in templates['alias']:
            result.append(command)

    return result

def generate_switch_config(access=True, psecurity=False, trunk=True,
                           ospf=True, mngmt=True, alias=False):
    """
    Аргументы контролируют какие настройки надо выполнить.
    По умолчанию, будет настроено все, кроме psecurity и alias.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    result = []

    if access:
        if psecurity:
            x = generate_access_config(access_dict, psecurity=True)
        else:
            x = generate_access_config(access_dict)
        result.extend(x)

    if trunk:
        x = generate_trunk_config(trunk_dict)
        result.extend(x)

    if ospf:
        x = generate_ospf_config('templates.yaml')
        result.extend(x)

    if mngmt:
        x = generate_mngmt_config('templates.yaml')
        result.extend(x)

    if alias:
        x = generate_alias_config('templates.yaml')
        result.extend(x)

# Сгенерировать конфигурации для разных коммутаторов:

sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

print(sw1)
print(sw2)
print(sw3)
