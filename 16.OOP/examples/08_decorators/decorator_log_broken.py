import sys
import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

def log(log_level, dest):
    def decorator(func):
        console = logging.StreamHandler(dest)
        console.setLevel(getattr(logging, log_level.upper(), logging.info))
        console.setFormatter(
            logging.Formatter('{asctime} - {name} - {levelname} - {message}',
                              datefmt='%H:%M:%S', style='{'))
        logger.addHandler(console)

        def inner(*args, **kwargs):
            logger.info('Функция {}'.format(func.__name__))
            if args:
                logger.debug(
                    'Функция {}. Позиционные аргументы: {}'.format(func.__name__, args))
            if kwargs:
                logger.debug(
                    'Функция {}. Ключевые аргументы: {}'.format(func.__name__, kwargs))
            result = func(*args, **kwargs)
            logger.debug(
                'Функция {}. Результат функции: {}'.format(func.__name__, result))
            return result
        return inner
    return decorator

@log('debug', sys.stderr)
def f(a,b):
    return a+b

f(4,5)


@log('info', sys.stdout)
def f(a,b):
    return a+b


f(4,5)

