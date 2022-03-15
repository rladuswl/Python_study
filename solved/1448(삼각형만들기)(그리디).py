## 백준 1448 삼각형 만들기
# 그리디, 정렬

import sys
input = sys.stdin.readline

# 삼각형 결정 조건

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in range(len(lst)-2):
    if lst[i] < lst[i+1] + lst[i+2]:
        print(lst[i] + lst[i+1] + lst[i+2])
        break
else:
    print(-1)
