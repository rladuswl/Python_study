import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 토마토 (BFS 활용)

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dis = [[0]*n for _ in range(m)]

Q = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            Q.append((i, j))

while Q:
    a, b = Q.popleft()
    for x in range(4):
        aa = a + dx[x]
        bb = b + dy[x]
        if (0<=aa<m) and (0<=bb<n) and (graph[aa][bb]==0):
            graph[aa][bb]=1
            dis[aa][bb]=dis[a][b]+1
            Q.append((aa, bb))

flag = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)