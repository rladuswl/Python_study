import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# dis 사용하기!!!!
# 최단거리 문제는 무조건 BFS -> 한 번만에 방문할 수 있는 것 전부 방문, 두 번만에 방문할 수 있는 것 전부 방문, ...

'''내 풀이
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
'''

'''강사님 풀이'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1  # visited 리스트 따로 만들지 않고, 입력 받은 리스트에서 방문 체크 하기
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dx[i]
        if (0<=x<7) and (0<=y<7) and (board[x][y] == 0):
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])