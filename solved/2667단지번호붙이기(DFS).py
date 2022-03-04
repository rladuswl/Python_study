# 백준 2667 단지번호붙이기

# DFS
# 행열로 풀기, 방향 확인용 좌표 필요

import sys
input = sys.stdin.readline


# DFS 함수 정의
def DFS(x, y, c):
    global num  # 한 단지 안에 집 몇 개?
    visited[x][y] = 1
    num += 1
    graph[x][y] = c  # 단지 표시
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n:
            if graph[xx][yy] == 1 and visited[xx][yy] == 0:
                DFS(xx, yy, c)



n = int(input())

# 데이터 저장
graph = [[0]*n for _ in range(n)]
# 방문 내역 저장
visited = [[0]*n for _ in range(n)]

# graph에 입력받은 데이터 0 또는 1 저장
for i in range(n):
    lst = sys.stdin.readline().rstrip()
    for j, a in enumerate(lst):
        graph[i][j] = int(a)

# 방향 확인용 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 1  # 단지 (1단지, 2단지, 3단지 ...)
num_list = []  # 단지 별 집 개수를 리스트에 넣어놓기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            num = 0  # 단지 안에 집 몇 개?
            DFS(i, j, cnt)

            num_list.append(num)
            cnt += 1  # 단지 하나 증가

print(len(num_list))
for x in sorted(num_list):
    print(x)