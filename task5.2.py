#!/usr/bin/env python3
# -*- coding: utf-8 -*-

("""
Задание 5.2

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании Cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco.

Усложненный вариант: сделать преобразование в одной строке скрипта.
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []
""")

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

"""Решение"""
mac_cisco.extend(m.replace(':', '.') for m in mac)
print(mac_cisco)
