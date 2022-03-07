## 백준 1926 그림

import sys
input = sys.stdin.readline

# 1. 입력받은 n, m으로 이차원배열 만든다. 그래프 하나씩 돌면서 BFS 를 실행한다.
# 2. 실행할 때마다 한 영역이 시작되는 것이므로 최종 영역이 몇 개인지 나타내는 변수 count를 +1 한다.
# 3. BFS 안에서는 한 조각(?)마다 cnt를 +1 하여 한 영역 안에 조각이 몇 개 있는지 센다.
# 4. count와 각 영역의 cnt 중에 max를 출력한다.

from collections import deque
def BFS(x, y):
    q = deque()
    cnt = 1
    q.append([x, y])
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            aa = a + dx[i]
            bb = b + dy[i]
            if 0 <= aa < n and 0 <= bb < m and graph[aa][bb] == 1 and visited[aa][bb] == 0:
                visited[aa][bb] = 1
                q.append([aa, bb])
                cnt += 1
    return cnt



n, m = map(int, input().split())

graph = []
for _ in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)

# 방향 (좌우상하)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
cnt_list = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt_list.append(BFS(i, j))
            count += 1  # 그림의 개수

if count != 0:
    print(count)
    print(max(cnt_list))
else:
    print(count)
    print(0)
