## 백준 2251 물통

import sys
input = sys.stdin.readline

from collections import deque

# 모든 경우의 수를 전부 찾는 완전탐색
# BFS 사용하여 a, b, c 세 가지 물병으로 주고 받을 수 있는 경우의 수를 구현

def visit(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        q.append((x, y))

def BFS():
    while q:
        # x : a물통에 들어있는 물의 양, y : b물통에 들어있는 물의 양, z : c물통에 들어있는 물의 양
        x, y = q.pop()
        z = c - x - y

        # a물통이 비어있을 때 c물통의 양 저장
        if x == 0:
            ans.append(z)

        # x -> y
        water = min(x, b-y)
        visit(x-water, y+water)

        # x -> z
        water = min(x, c-z)
        visit(x - water, y)

        # y -> x
        water = min(y, a-x)
        visit(x + water, y - water)

        # y -> z
        water = min(y, c-z)
        visit(x, y - water)

        # z -> x
        water = min(z, a-x)
        visit(x + water, y)

        # z -> y
        water = min(z, b - y)
        visit(x, y + water)


a, b, c = map(int, input().split())

# 경우의 수를 담을 큐 (a, b 물병의 남은 용량 표시)
q = deque()
q.append((0, 0))  # 처음 a, b는 0, 0이다.

# 방문 여부(visited[x][y])
visited = [[0] * (b+1) for _ in range(a+1)]
visited[0][0] = 1

# 답 저장할 배열(c 저장)
ans = []

BFS()

# 답 출력
ans.sort()
for x in ans:
    print(x, end=' ')