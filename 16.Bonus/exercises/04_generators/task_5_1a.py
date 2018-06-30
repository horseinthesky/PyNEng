# -*- coding: utf-8 -*-
'''
Задание 5.1a

Создать генератор get_intf_ip, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:
* первый элемент кортежа - имя интерфейса
* второй элемент кортежа - IP-адрес
* третий элемент кортежа - маска

Например: ('FastEthernet', '10.0.1.1', '255.255.255.0')

Для получения такого результата, используйте регулярные выражения.

Проверить работу генератора на примере файла config_r1.txt.
'''
import re


def get_intf_ip(filename):
    with open(filename) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            match = re.search(regex, line)
            if match:
                yield interface, match[1], match[2]


regex = 'ip address (\S+) (\S+)\n'
