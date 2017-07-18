#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*-

print("""  
Задание 3.3
Получить из строки CONFIG список VLAN вида ['1', '3', '10', '20', '30', '100']. 
""")                                                                            
 
CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
print(('CONFIG = '), CONFIG, '\n')

"""Решение"""
test = CONFIG.split()
VLAN = test[-1].split(',')
print(VLAN)

