import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 송아지 찾기 (BFS : 상태트리탐색)

# S>E 이면 최상단 노드 S부터 시작, S<E 이면 최상단 노드 E부터 시작
# S부터 시작이라고 하면, 간선은 +1, -1, +5 로 세 갈래가 뻗음
# 해당 노드에서 3개의 간선을 모두 돌면서 큐에 매번 노드를 담음
'''내 풀이
from collections import deque

def bfs(N):
    q = deque()
    q.append(N)
    visited[N] = 1

    while q:
        p = q.popleft()
        for x in lst:
            if visited[p+x] == 0:  # 1 <= p+x <= 10000
                dis[p+x] = dis[p] + 1
                if p+x == E:
                    print(dis[p+x])
                    exit(1)  # 처음으로 찾은게 최소임 따라서 출력하고 바로 끝내면 됨
                visited[p+x] = 1
                q.append(p+x)


S, E = map(int, input().split())

lst = [1, -1, 5]
visited = [0]*10001
dis = [0]*10001
bfs(S)
'''

from collections import deque

MAX = 10000
ch = [0] * (MAX+1)  # 체크 리스트 (visited)
dis = [0] * (MAX+1)  # 점프 개수 저장해 놓을 리스트
n, m = map(int, input().split())
ch[n] = 1  # 시작 노드는 우선 방문처리 하기
dis[n] = 0  # 시작 노드는 출발점이므로 0으로 두기
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        print(dis[m])
        break
    for next in (now-1, now+1, now+5):  # next가 now-1, now+1, now+5가 되어 3번 돌음
        if (0<next<=MAX) and (ch[next] == 0):
            ch[next] = 1
            dis[next] = dis[now] + 1
            dQ.append(next)
