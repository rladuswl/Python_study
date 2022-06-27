# 런타임 에러

lst = []
for _ in range(28):
    x = int(input())
    lst.append(x)

lst.sort()

for i in range(30):
    if lst[i] != i+1:
        lst.insert(i, i+1)
        print(i+1)
