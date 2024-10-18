n = int(input())
stepen = 1
cnt = 0
while stepen <= n:
    cnt += 1
    stepen *= 2
print(cnt -1, stepen // 2)
