# -*- coding: utf-8 -*-
'''
Задание 7.3

Переделать декоратор all_args_str таким образом, чтобы он проверял
не только позиционные аргументы, но и ключевые тоже

'''

def all_args_str(func):
    def inner(*args):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError('Все аргументы должны быть строками')
        return func(*args)
    return inner


@all_args_str
def concat_str(str1, str2):
    return str1+str2


if __name__ == '__main__':
    concat_str(str1=2, str2=1)
