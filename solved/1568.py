n = int(input())
tmp = 1
cnt = 0
while n:
    if n < tmp:
        tmp = 1
        continue
    n -= tmp
    tmp += 1
    cnt += 1

print(cnt)