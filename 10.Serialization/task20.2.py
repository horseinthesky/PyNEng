#!/usr/bin/env python3
#-*- coding: utf-8 -*-

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
    pass

def generate_trunk_config(trunk):
    """
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_ospf_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон ospf.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_mngmt_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон mngmt.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_alias_config(filename):
    """
    filename - имя файла в формате YAML, в котором находится шаблон alias.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

def generate_switch_config(access=True, psecurity=False, trunk=True,
                           ospf=True, mngmt=True, alias=False):
    """
    Аргументы контролируют какие настройки надо выполнить.
    По умолчанию, будет настроено все, кроме psecurity и alias.
    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    """
    pass

# Сгенерировать конфигурации для разных коммутаторов:

sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

