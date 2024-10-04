a = int(input())
b = int(input())

s = []

if a > b:
    for i in range(b, a):
        if i % 2 != 0:
            s.append(i)

    print(sorted(s, reverse = True))

else:
    print("Введите первое значение больше второго")
