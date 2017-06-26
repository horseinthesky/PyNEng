#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*- 

print("""
Задание 3.6
Обработать строку NAT таким образом, чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
""")

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

"""Решение"""
NAT_NEW = NAT.replace('Fast', 'Gigabit')
print(NAT_NEW)

