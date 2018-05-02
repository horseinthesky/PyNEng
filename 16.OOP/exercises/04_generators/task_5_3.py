# -*- coding: utf-8 -*-

'''
Задание 5.3

Сначала надо скачать файл:
wget https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz

Распаковать:
gunzip rib.table.lg.ba.ptt.br-BGP.csv.gz

Создать генератор filter_route_by_attr, который фильтрует маршруты на основании указанного атрибута и значения.

Аргументы генератора:
* итерируемый объект
* имя атрибута
* значение атрибута

Заменить генераторы filter_by_nexthop и filter_by_mask генератором filter_route_by_attr в коде ниже.

Подсказка: в этом задании пригодится функция getattr

Пример использования функции:

In [1]: import csv
   ...: from collections import namedtuple
   ...:
   ...: f =  open('rib.table.lg.ba.ptt.br-BGP.csv')
   ...: reader = csv.reader(f)
   ...:
   ...: headers = next(reader)
   ...: Route = namedtuple("Route", headers)
   ...: route_tuples = map(Route._make, reader)
   ...:

In [2]: nhop_23 = filter_route_by_attr(route_tuples, 'nexthop', '200.219.145.23')

In [3]: mask_22 = filter_route_by_attr(nhop_23, 'netmask', '22')

In [4]: next(mask_22)
Out[4]: Route(status='*>', network='1.0.28.0', netmask='22', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 2516 2519', origin='i')

In [5]: next(mask_22)
Out[5]: Route(status='*>', network='1.0.208.0', netmask='22', nexthop='200.219.145.23', metric='NA', locprf='NA', weight='0', path='53242 12956 6453 4651 9737 23969', origin='i')


'''

import csv
from collections import namedtuple


def filter_by_nexthop(iterable, nexthop):
    for line in iterable:
        if line[3] == nexthop:
            yield line


def filter_by_mask(iterable, mask):
    for line in iterable:
        if line[2] == mask:
            yield line


f =  open('rib.table.lg.ba.ptt.br-BGP.csv')
reader = csv.reader(f)

headers = next(reader)
Route = namedtuple("Route", headers)
route_tuples = map(Route._make, reader)

nhop_23 = filter_by_nexthop(route_tuples, '200.219.145.23')
mask_23 = filter_by_mask(nhop_23, '22')

