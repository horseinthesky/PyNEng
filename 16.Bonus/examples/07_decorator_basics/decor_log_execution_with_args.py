import logging


def log(func):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def inner(*args, **kwargs):
        logging.debug('Функция {}'.format(func.__name__))
        if args:
            logging.debug(
                'Функция {}. Позиционные аргументы: {}'.format(func.__name__, args))
        if kwargs:
            logging.debug(
                'Функция {}. Ключевые аргументы: {}'.format(func.__name__, kwargs))
        result = func(*args, **kwargs)
        logging.debug(
            'Функция {}. Результат функции: {}'.format(func.__name__, result))
        return result
    return inner


@log
def mult(a,b):
    return a*b

@log
def sub(a,b):
    return a-b


if __name__ == '__main__':
    mult(4,5)
    mult(a=100, b=300)
    sub(100,44)
