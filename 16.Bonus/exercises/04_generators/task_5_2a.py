# -*- coding: utf-8 -*-
'''
Задание 5.2a

Изменить генератор read_file_in_chunks из задания 5.2 таким образом,
чтобы внутри использовалась функция islice из модуля itertools.

'''
from itertools import islice


def read_file_in_chunks(filename, number_of_lines):
    with open(filename) as f:
        while True:
            block = ''.join(islice(f, int(number_of_lines)))
            if block:
                yield block
            else:
                break
