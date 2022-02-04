a, b = map(str, input().split())

atmp = 0
btmp = 0
for i in a:
    atmp += int(i)
for j in b:
    btmp += int(j)

print(atmp*btmp)