#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*- 

"""
Задание 3.9

Найти индекс последнего вхождения элемента с конца.
Например, для списка num_list, индекс последнего вхождения элемента 10 - 4; 
для списка word_list, индекс последнего вхождения элемента 'ruby' - 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу) 
и проверить на разных списках и элементах.

Не использовать для решения циклы (for, while) и условия (if/else).
Подсказка: функция len() возвращает длину списка.

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
"""

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print(num_list)
print(word_list)

"""Решение"""
num = input('Введите элемент num_list: ')

num_list.reverse()
print('Номер последнего вхождения:', len(num_list) - num_list.index(int(num)) - 1)

word = input('\n' + 'Введите элемент word_list: ')

word_list.reverse()
print('Номер последнего вхождения:', len(word_list) - word_list.index(word) - 1)



