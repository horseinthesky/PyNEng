def cool(func):
    print('Теперь функция', func.__name__, 'крутая')
    func.cool = True
    return func


@cool
def func1():
    pass


#func2 = cool(func2)
@cool
def func2():
    pass


def func3():
    pass


def func4():
    pass

if __name__ == "__main__":
    cool_funcs = {f.__name__: f
                  for name, f in globals().items()
                  if hasattr(f, 'cool') and f.cool}
    print(cool_funcs)

