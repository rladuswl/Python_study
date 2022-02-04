n = int(input())
li = [list(map(str, input())) for _ in range(n)]
d = {}

for i in range(len(li)):
    if li[i][0] in d:
        d[li[i][0]] += 1
    else:
        d[li[i][0]] = 1

s = ''
for x, y in d.items():
    if y >= 5:
        s += x

if len(s) == 0:
    print('PREDAJA')
else:
    print(''.join(sorted(s)))