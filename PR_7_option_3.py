#1
dlina = int(input())
D = []
for n in range(dlina):
        D.append(n)
res = sum([int(i) for i in range(len(D)) if i % 2 != 0])
print(res)

#2
array = [1, 23, 4, 7, 8, 54, 14, 4]
for i in range(len(array)):
        if array[i] < 15:
                array[i] *= 2
print(array)
