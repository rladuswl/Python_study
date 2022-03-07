## 백준 1325 - 효율적인 해킹

import sys
input = sys.stdin.readline

# 1. 한 컴퓨터에서 신뢰하는 컴퓨터를 이어가므로 BFS..(?)
# 2. {1: [3], 2: [3], 3: [4, 5], 4: [], 5: []} 으로 현재 신뢰 관계 dict 형태로 만들기
# 3. 시작 노드부터 더이상 관계가 없을 때까지 내려가며 각 컴퓨터 개수 +1
# 4. 가장 많은 컴퓨터를 해킹하는 컴퓨터 번호를 max 라 하면, 컴퓨터 개수 비교해서 더 크면 그때의 시작 노드가 max 가 된다.

from collections import deque

'''메모리초과
def BFS(s):
    queue = deque()
    res = 0

    queue.append(s)
    res += 1
    while queue:
        a = queue.popleft()
        for i in d[a]:
            queue.append(i)
            res += 1
    return res


n, m = map(int, input().split())

d = {}
for i in range(1, n+1):
    d[i] = []
for _ in range(m):
    a, b = map(int, input().split())
    d[b].append(a)

ans = []  # 답
m = -2147000000
for i in range(1, n+1):
    cnt = BFS(i)
    if cnt >= m:
        ans.append(i)
        m = cnt

ans = sorted(ans)

for x in ans:
    print(x, end=' ')
'''

def BFS(start):
    queue = deque()
    queue.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    res = 1
    while queue:
        p = queue.popleft()
        for i in s[p]:
            if visited[i] == 0:
                queue.append(i)
                res += 1
                visited[i] = 1
    return res


n, m = map(int, input().split())

s = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)


ans = []  # 답
m = 0
for i in range(1, n+1):
    cnt = BFS(i)
    if cnt == m:
        ans.append(i)
    if cnt > m:
        ans = []
        ans.append(i)
        m = cnt

print(*ans)