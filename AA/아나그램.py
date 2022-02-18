import sys
sys.stdin = open("input.txt", "rt")

# 딕셔너리 get 함수

## Anagram (아나그램 : 구글 인터뷰 문제)
'''내 답안
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
'''

'''모범답안1

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')
'''

'''모범답안2'''
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

sH = dict()
for x in a:
    sH[x] = sH.get(x, 0)+1
for x in b:
    sH[x] = sH.get(x, 0)-1

for x in a:
    if sH.get(x) > 0:
        print('NO')
        break
else:
    print('YES')