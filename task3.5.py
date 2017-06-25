#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*-

print("""
Задание 3.5

Список VLANS - это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.
Из списка нужно получить уникальный список VLANов, отсортированный по возрастанию номеров.
Не использовать для решения задачи циклы, оператор if.
VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
""")

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

"""Решение"""
set = set(VLANS)
VLANS_LIST = list(set)
print(sorted(VLANS_LIST))

