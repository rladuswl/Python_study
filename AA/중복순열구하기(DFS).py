import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 중복순열 구하기(DFS)

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1

    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)


n, m = map(int, sys.stdin.readline().split())
res = [0]*m
cnt = 0
DFS(0)
print(cnt)