def multiply(num1):
    def mult(num2):
        return num1*num2
    return mult


multiply(2)
multiply(2)(3)

mult_by_3 = multiply(3)
print(mult_by_3(5))
print(mult_by_3(10))

mult_by_10 = multiply(10)
print(mult_by_10(10))

