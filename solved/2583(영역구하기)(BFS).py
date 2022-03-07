## 백준 2583 영역 구하기 BFS

# 1. m*n의 이차원 배열을 만든다. (전부 0으로)
# 2. 입력받은 좌표 범위만큼을 전부 직사각형을 표시한다. (1로 표시)
# 3. 0인 부분으로 BFS 를 하여, 한 칸에 해당할 때마다 +1을 하여 한 영역의 넓이를 구한다.
# 4. 최종적으로 분리된 영역이 몇 개인지 구한다.

import sys
input = sys.stdin.readline

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

            if 0 <= aa < m and 0 <= bb < n and visited[aa][bb] == 0 and graph[aa][bb] == 0:
                q.append([aa, bb])
                visited[aa][bb] = 1
                cnt += 1
    return cnt



m, n, k = map(int, input().split())

graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


# 방향 (좌우상하)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0]*n for _ in range(m)]
cnt_list = []
count = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 0:
            cnt_list.append(BFS(i, j))
            count += 1

# 최종출력
print(count)
cnt_list = sorted(cnt_list)
for x in cnt_list:
    print(x, end=' ')