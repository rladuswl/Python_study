import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# dis 사용하기!!!!

lst = []
for _ in range(7):
    lst.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visited = [[0]*7 for _ in range(7)]
dis = [[0]*7 for _ in range(7)]  # 출발지로부터의 거리를 나타내는 그래프

from collections import deque

q = deque()
q.append((0, 0))
visited[0][0] = 1
dis[0][0] = 0

while q:
    a, b = q.popleft()

    for i in range(4):
        aa = a + dx[i]
        bb = b + dy[i]

        if (0 <= aa < 7) and (0 <= bb < 7):
            if lst[aa][bb] == 0:
                if visited[aa][bb] == 0:
                    q.append((aa, bb))
                    visited[aa][bb] = 1
                    dis[aa][bb] = dis[a][b] + 1


if dis[6][6] != 0:
    print(dis[6][6])
else:
    print(-1)
