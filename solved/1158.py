# 백준 1158 요세푸스 문제

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

n_list = deque()
for i in range(n):
    n_list.append(i+1)

s = []
while len(n_list) != 0:
    for i in range(1, k+1):
        if i == k:
            s.append(str(n_list.popleft()))
        else:
            n_list.append(n_list.popleft())

print('<', end='')
str = ', '.join(s)
print(str, end='')
print('>')


