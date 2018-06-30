def debug_function(func):
    def inner(*args, **kwargs):
        print('Вызываем', func.__name__)
        if args: print('Позиционные аргументы:', args)
        if kwargs: print('Ключевые аргументы:', kwargs)
        return func(*args, **kwargs)
    return inner


@debug_function
def mult(a,b):
    return a*b


if __name__ == '__main__':
    mult(4,5)
    mult(a=100, b=300)
