#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*- 

print("""
Задание 3.8

Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод столбцами, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
столбцами
ширина столбца 10 символов
Пример вывода:
10        1         1         1
00001010  00000001  00000001  00000001

IP = '192.168.3.1'
""")

IP = '192.168.3.1'

"""Решение"""
num = IP.split('.')
print("{:10} {:10} {:10} {:10}".format(num[0], num[1], num[2], num[3]))
print("{:10} {:10} {:10} {:10}".format(bin(int(num[0], 10))[2:], bin(int(num[1], 10))[2:], bin(int(num[2], 10))[2:], bin(int(num[3], 10))[2:]))
