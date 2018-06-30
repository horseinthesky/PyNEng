function_information = '''
    Информация о функции: {}
    Имя функции: {}
    Docstring: {}
'''


def all_args_str_1(func):
    def inner(*args):
        if not all([isinstance(arg, str) for arg in args]):
            raise ValueError('Все аргументы должны быть строками')
        return func(*args)
    return inner


@all_args_str_1
def concat_str(str1, str2):
    """Функция ожидает две строки"""
    return str1+str2

#Информация о функции concat_str теряется:
print('До применения wraps:')
print(function_information.format(
    concat_str, concat_str.__name__, concat_str.__doc__))


###################################################################
#Декоратор wraps из модуля functools позволяет перенести информацию
from functools import wraps

def all_args_str_2(func):
    @wraps(func)
    def inner(*args):
        if not all([isinstance(arg, str) for arg in args]):
            raise ValueError('Все аргументы должны быть строками')
        return func(*args)
    return inner


@all_args_str_2
def concat_str(str1, str2):
    """Функция ожидает две строки"""
    return str1+str2

#Теперь информация сохраняется
print('После применения wraps:')
print(function_information.format(
    concat_str, concat_str.__name__, concat_str.__doc__))

