## 백준 1303 전투
# 그래프

'''런타임 에러
import sys
input = sys.stdin.readline
from collections import deque

# 1. 인접행렬, 너비 우선 탐색
# 2. 방향 사용, 방문 사용

n, m = map(int, input().split())

lst = []

for _ in range(m):
    s = list(map(str, sys.stdin.readline().rstrip()))
    lst.append(s)


def bfs(x, y, s):
    global w_sum
    global b_sum

    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]

            if 0 <= xx < n and 0 <= yy < m:
                if visited[xx][yy] == 0 and lst[xx][yy] == s:
                    if s == 'W':
                        w_sum += 1
                    elif s == 'B':
                        b_sum += 1
                    visited[xx][yy] = 1
                    q.append([xx, yy])


# 방문처리
visited = [[0]*n for _ in range(m)]

# 방향 (좌우상하)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

w_total = 0
b_total = 0
w_sum = 0
b_sum = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] != 1 and lst[i][j] == 'W':
            w_sum = 1
            bfs(i, j, 'W')
            w_total += (w_sum**2)
        elif visited[i][j] != 1 and lst[i][j] == 'B':
            b_sum = 1
            bfs(i, j, 'B')
            b_total += (b_sum**2)

print(w_total, b_total)
'''
