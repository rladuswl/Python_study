import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 섹션 6. 인접행렬 (가중치 방향그래프)

# 인접행렬은 행->열 로 생각해야 한다.
# 무방향 그래프(양방향), 단방향 그래프(가중치 방향)


n, m = map(int, input().split())

graph = [[0]*n for _ in range(n)]  # 0으로 초기화한 이차원 배열 만들기 (a*a)

'''가중치방향'''
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c


'''무방향
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c
'''

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()