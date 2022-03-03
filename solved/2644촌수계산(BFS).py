## 백준 2644 촌수계산
# BFS

import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        d = queue.popleft()
        for i in graph[d]:
            if visited[i] == 0:
                visited[i] = 1
                result[i] = result[d] + 1
                queue.append(i)


n = int(input())  # 사람 수
a, b = map(int, input().split())  # a와 b의 촌수
m = int(input())  # 부모와 자식들 간의 관계의 개수

graph = {}
for i in range(n):
    graph[i+1] = set()

for j in range(m):
    c, d = map(int, input().split())
    graph[c].add(d)
    graph[d].add(c)

visited = [0] * (n+1)
result = [0] * (n+1)
BFS(a)

if result[b] != 0:
    print(result[b])
else:
    print(-1)