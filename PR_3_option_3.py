n = int(input())
minut = n % 60
chas = n % (60 * 24) // 60
if 0 < n <= 1440:
   print(chas,":",minut)
else:
    print("Введено минут больше чем кол-во минут в сутках")
