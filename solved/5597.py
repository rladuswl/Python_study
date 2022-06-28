# 런타임 에러
# if 추가해서 break 걸었지만 다시 런타임 에러

lst = []
for _ in range(28):
    x = int(input())
    lst.append(x)

lst.sort()

cnt = 0
for i in range(30):
    if lst[i] != i+1:
        lst.insert(i, i+1)
        print(i+1)
        cnt += 1
        if cnt == 2:
            break
