import sys
#sys.stdin = open("input.txt", "rt")

## Anagram (아나그램 : 구글 인터뷰 문제)

first = list(sys.stdin.readline().rstrip())
second = list(sys.stdin.readline().rstrip())

d = {}
for x in first:
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] += 1

for v in second:
    if v in d.keys():
        d[v] -= 1
    else:
        print('NO')
        break
else:
    for i in d.values():
        if i != 0:
            print('NO')
            break
    else:
        print('YES')