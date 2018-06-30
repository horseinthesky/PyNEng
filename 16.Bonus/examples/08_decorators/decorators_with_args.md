## Декораторы с аргументами

### Базовые примеры

Функция do_magic ожидает один аргумент - arg1 и возвращает внутреннюю функцию decorator,
которая и будет декоратором функции. В данном случае, декоратор только выводит значение аргумента:
```python
def do_magic(arg1):
    def decorator(func):
        print('Значение аргумента arg1', arg1)
        return func
    return decorator
```

Применение декоратора:
```python
In [15]: @do_magic('magic')
    ...: def f(a,b):
    ...:     return a+b
    ...:
Значение аргумента arg1 magic
```

Запись выше аналогична такому вызову:
```python
In [16]: do_magic('magic')(f)
Значение аргумента arg1 magic
```

Пример функции со значением по умолчанию:
```python
def control_verbose(verbose=True):
    def decorator(func):
        if verbose: print('Вызываем', func.__name__)
        return func
    return decorator
```

Различные варианты вызова декоратора:
```python
In [20]: @control_verbose(verbose=True)
    ...: def f(a,b):
    ...:     return a+b
    ...:
Вызываем f

In [21]: @control_verbose(verbose=False)
    ...: def f(a,b):
    ...:     return a+b
    ...:

In [22]: @control_verbose(True)
    ...: def f(a,b):
    ...:     return a+b
    ...:
Вызываем f
```

### Маркировка функций с помощью декоратора

Декоратор добавляет к функции атрибут mark со значением, которое указано при вызове декоратора:
```python
def mark(value):
    def decorator(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        inner.mark = value
        return inner
    return decorator
```

Пример использования декоратора:
```python
In [4]: @mark('magic')
   ...: def f():
   ...:     return 42
   ...:

In [5]: f()
Out[5]: 42

In [6]: f.mark
Out[6]: 'magic'
```

### Создание соответствий route - function

Декоратор register добавляет в словарь url_map соответствие route - функция:
```python
url_map = {}

def register(route):
    def decorator(func):
        url_map[route] = func
        return func
    return decorator
```

Применение декоратора:
```python
In [16]: @register('/reports')
    ...: def func():
    ...:     return 42
    ...:
```

Теперь в словаре url_map добавилось соответствие:
```python
In [17]: url_map
Out[17]: {'/reports': <function __main__.func>}

In [18]: url_map['/reports']
Out[18]: <function __main__.func>

In [19]: url_map['/reports']()
Out[19]: 42
```

Добавление еще одного соответствия:
```python
In [20]: @register('/')
    ...: def func_index():
    ...:     return 42
    ...:

In [21]: url_map
Out[21]: {'/': <function __main__.func_index>, '/reports': <function __main__.func>}
```

### Декоратор, которые проверяет права пользователя

Класс User:
```python
class User:
    def __init__(self, username, permissions=None):
        self.username = username
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions
```

Экземпляры класса:
```python
In [29]: nata = User('nata', ['admin', 'user'])

In [30]: nata.has_permission('admin')
Out[30]: True

In [31]: nata.has_permission('superadmin')
Out[31]: False

In [32]: oleg = User('oleg', ['user'])

In [33]: oleg.has_permission('admin')
Out[33]: False

In [34]: current_user = oleg
```

Класс AccessDenied:
```python
class AccessDenied(Exception):
    pass
```

Пример неправильного варианта декоратора:
```python
def permission_required(permission):
    def decorator(func):
        if not current_user.has_permission(permission):
            raise AccessDenied('You shall not pass!')
        return func
    return decorator
```

Проблема с декоратором permission_required в том, что он вызывается при декорировании функции, а не при вызове. Соответветственно, при декорировании функции, будет возникать исключение, если у пользователя нет нужных прав:
```
In [40]: @permission_required('admin')
    ...: def supersecret():
    ...:     return 42
    ...:
---------------------------------------------------------------------------
AccessDenied                              Traceback (most recent call last)
<ipython-input-40-16ad7d346eb2> in <module>()
----> 1 @permission_required('admin')
      2 def supersecret():
      3     return 42

<ipython-input-35-5e6a908c07af> in decorator(func)
      2     def decorator(func):
      3         if not current_user.has_permission(permission):
----> 4             raise AccessDenied('You shall not pass!')
      5         return func
      6     return decorator

AccessDenied: You shall not pass!
```

Правильная реализация декоратора:
```python
In [47]: def permission_required(permission):
    ...:     def decorator(func):
    ...:         def inner(*args, **kwargs):
    ...:             if not current_user.has_permission(permission):
    ...:                 raise AccessDenied('You shall not pass!')
    ...:             return func(*args, **kwargs)
    ...:         return inner
    ...:     return decorator
    ...:

In [48]: @permission_required('admin')
    ...: def supersecret():
    ...:     return 42
    ...:

In [49]: current_user.permissions
Out[49]: ['user']

In [50]: supersecret()
---------------------------------------------------------------------------
AccessDenied                              Traceback (most recent call last)
<ipython-input-50-3bd1c49f6861> in <module>()
----> 1 supersecret()

<ipython-input-47-5023a15477c6> in inner(*args, **kwargs)
      3         def inner(*args, **kwargs):
      4             if not current_user.has_permission(permission):
----> 5                 raise AccessDenied('You shall not pass!')
      6             return func(*args, **kwargs)
      7         return inner

AccessDenied: You shall not pass!

In [51]: current_user = nata

In [52]: supersecret()
Out[52]: 42
```

### Стекирование декораторов

Декораторы можно стекировать:
```python
In [57]: @register('/topsecret')
    ...: @permission_required('admin')
    ...: def supersecret():
    ...:     return 42
    ...:

In [58]: supersecret()
Out[58]: 42
```

Пример простых декораторов, для демонстрации порядка применения декораторов, при стекировании:
```python
def debug(func):
    print('Применяю debug')
    def inner(*args, **kwargs):
        print('Вызываем', func.__name__)
        return func(*args, **kwargs)
    return inner

def cool(func):
    print('making cool', func.__name__)
    func.cool = True
    return func
```

Применение декораторов:
```python
In [70]: @debug
    ...: @cool
    ...: def f(a,b):
    ...:     return a*b
    ...:
making cool f
Применяю debug

In [71]: @cool
    ...: @debug
    ...: def f(a,b):
    ...:     return a*b
    ...:
Применяю debug
making cool inner
```

Последний вариант применения декораторов, равнозначен такому вызову:
```python
In [72]: f = cool(debug(f))
Применяю debug
making cool inner
```

