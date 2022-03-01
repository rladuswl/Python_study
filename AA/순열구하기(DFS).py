import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 수열 추측하기(순열, 파스칼 응용)

'''내 답안
def DFS(L):
    if L == n:
        sum = 0
        for j in range(len(p)):
            sum += p[j]*b[j]
        if sum == f:
            for k in range(len(p)):
                print(p[k], end=' ')
            print()
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] != 1:
                p[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0


n, f = map(int, input().split())
b = [1]*n
p = [0]*n
ch = [0]*(n+1)

for i in range(1, n):
    b[i] = (b[i-1]*(n-i))//i

DFS(0)
'''

'''모범답안'''
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i] = 0



n, f = map(int, input().split())
b = [1]*n
p = [0]*n
ch = [0]*(n+1)

for i in range(1, n):
    b[i] = (b[i-1]*(n-i))//i

DFS(0, 0)