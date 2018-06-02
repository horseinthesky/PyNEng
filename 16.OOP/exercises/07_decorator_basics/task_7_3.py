# -*- coding: utf-8 -*-
'''
Задание 7.3

Переделать декоратор all_args_str таким образом, чтобы он проверял
не только позиционные аргументы, но и ключевые тоже

'''


def all_args_str(func):
    def inner(*args, **kwargs):
        if not all(isinstance(arg, str) for arg in args):
            raise ValueError('Все аргументы должны быть строками')
        if not all(isinstance(kwarg, str) for kwarg in kwargs.values()):
            raise ValueError('Все аргументы должны быть строками')
        return func(*args, **kwargs)
    return inner


@all_args_str
def concat_str(str1, str2):
    return str1 + str2


if __name__ == '__main__':
    concat_str(str1=2, str2=1)
