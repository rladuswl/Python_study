# 1919 애너그램 만들기
# 구현, 문자열

import sys
input = sys.stdin.readline

a = input()
b = input()


for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a = a.replace(a[i], ' ', 1)
            b = b.replace(b[j], ' ', 1)
            break
cnt = 0
for i in range(len(a)):
    if a[i] != ' ':
        cnt += 1
for j in range(len(b)):
    if b[j] != ' ':
        cnt += 1

print(cnt)