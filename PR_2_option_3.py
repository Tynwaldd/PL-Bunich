import math
x = float(input("Введите первую переменную: ")) #x = 0.0374
y = float(input("Введите первую переменную: ")) #y = -0.825
z = float(input("Введите первую переменную: ")) #z = 16

s = ((1 + (math.sin(x + y)) ** 2)/abs(x - ((2 * y)/(1 + x ** 2 * y ** 2)))) * x ** abs(y) + (math.cos(math.atan(1 / z))) ** 2

print(s)
