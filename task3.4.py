#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*-

print("""
Задание 3.4

Из строк command1 и command2 получить список VLAN, которые есть 
и в команде command1 и в команде command2. 

Не использовать для решения задачи циклы, оператор if.
Для данного примера, результатом должен быть список: [1, 3, 100]

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
""")

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"

"""Решение"""
VLANS1 = command1.split()
VLANS2 = command2.split()

set1 = set(VLANS1[-1].split(','))
set2 = set(VLANS2[-1].split(','))

VLANS_set = set1.intersection(set2)
VLANS_LIST = list(VLANS_set)
print(VLANS_LIST)
