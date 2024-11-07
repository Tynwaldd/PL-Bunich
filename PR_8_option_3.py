#1
from math import *
def gip(a, b):
    res = sqrt(a ** 2 + b ** 2)
    return res

katet_1 = float(input("Введите первый катет одного треугольника: "))
katet_2 = float(input("Введите второй катет одного треугольника: "))
katet_3 = float(input("Введите первый катет другого треугольника: "))
katet_4 = float(input("Введите второй катет другого треугольника: "))

gip1 = gip(katet_1, katet_2)
gip2 = gip(katet_3, katet_4)

if gip1 > gip2:
    print("Значение большего катета равно", gip1, ", а меньшего ", gip2)

else:
    print("Значение большего катета равно", gip2, ", а меньшего ", gip1)

#2

alfavit = "zxcvbnmasdfghjkqwertyuio"
alfavit = sorted(alfavit)
print(alfavit)
