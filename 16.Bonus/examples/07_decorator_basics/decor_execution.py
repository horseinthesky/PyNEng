
def decorator(func):
    #print('Запускаем decorator')
    def inner(*args, **kwargs):
        print('Вызываем', func.__name__)
        return func(*args, **kwargs)
    return inner


@decorator
def multiply(a, b):
    return a*b


@decorator
def mysumm(*args):
    return sum(args)

if __name__ == '__main__':
    multiply(3,4)
    mysumm(1,2,3,4)

