# 백준 1966 프린터 큐

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 0
    n, m = map(int, sys.stdin.readline().split())

    ip = [(p, v) for p, v in enumerate(list(map(int, sys.stdin.readline().split())))]
    ip = deque(ip)

    while True:
        p = ip.popleft()
        if any(p[1] < x[1] for x in ip):  # 뒤에 위험도가 높은 사람이 한 명이라도 있으면 true
            ip.append(p)
        else:
            cnt += 1
            if p[0] == m:
                break
    print(cnt)