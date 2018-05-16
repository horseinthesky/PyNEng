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
from itertools import dropwhile, takewhile


def get_intf_ip(filename):
    with open(filename) as f:
        while True:
            begin = dropwhile(lambda x: 'interface' not in x, f)
            lines = takewhile(lambda y: '!' not in y, begin)
            int_ip = ''.join(lines)
            print(int_ip)
            if not int_ip:
                return
            else:
                match = re.search(regex, int_ip)
                if match:
                    yield match.groups()


regex = 'interface (\S+)\n.*ip address (\S+) (\S+)\n'
