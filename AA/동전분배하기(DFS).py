import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 동전 분배하기

# 1. 상태트리 그리기

def dfs(L):
    global m
    if L == n:
        if (max(money) - min(money)) < m:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                m = max(money) - min(money)

    else:
        for i in range(3):
            money[i] += graph[L]
            dfs(L+1)
            money[i] -= graph[L]


n = int(input())
graph = []
for _ in range(n):
    graph.append(int(input()))
money = [0, 0, 0]  # A, B, C
m = 2147000000
dfs(0)
print(m)