#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Задание 6.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
    считывались только строки, в которых указаны MAC-адреса
    каждая строка, где есть MAC-адрес, должна обрабатываться таким образом, 
    чтобы на стандартный поток вывода была выведена таблица вида:
100    aabb.cc80.7000     Gi0/1
200    aabb.cc80.7000     Gi0/2
300    aabb.cc80.7000     Gi0/3
100    aabb.cc80.7000     Gi0/4
500    aabb.cc80.7000     Gi0/5
200    aabb.cc80.7000     Gi0/6
300    aabb.cc80.7000     Gi0/7
"""

"""Решение"""
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if not 'aabb' in line:
            pass
        else:
            vlan, mac, _, intf = line.split()
            print('{}    {}     {} '.format(vlan, mac, intf))
