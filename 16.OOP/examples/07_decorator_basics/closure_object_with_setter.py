def object_func(num1, num2):
    def mul():
        return num1*num2
    def add():
        return num1+num2
    def sub():
        return num1-num2
    def set_num1(value):
        nonlocal num1
        num1 = value

    object_func.mul = mul
    object_func.add = add
    object_func.sub = sub
    object_func.set_num1 = set_num1
    return object_func


o = object_func(10, 20)
o.set_num1(100)
print(o.mul())
