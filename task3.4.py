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
vlan1_test = command1.split()
vlan2_test = command2.split() 


