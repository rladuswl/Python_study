import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

## 동전교환

# L = 동전 사용 개수

def DFS(L, sum):
    global res

    if L > res:  # cut edge
        return

    if sum > m:
        return

    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(len(coin)):
            DFS(L+1, sum+coin[i])


n = int(input())
coin = list(map(int, input().split()))
m = int(input())
res = 2147000000  # 최소를 받을 변수
coin.sort(reverse=True)  # 내림차순
DFS(0, 0)
print(res)