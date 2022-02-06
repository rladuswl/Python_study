'''시간초과
n, m = map(int, input().split())
tot = [list(map(int, input().split())) for _ in range(n)]
k = int(input())


def solution(tot):
    i, j, x, y = map(int, input().split())
    sum = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            sum += tot[a-1][b-1]

    return sum


for _ in range(k):
    print(solution(tot))
'''

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 누적합 테이블 만들기
dp = [[0]*(m+1) for _ in range(n+1)]
for a in range(1, n+1):
    for b in range(1, m+1):
        dp[a][b] = lst[a-1][b-1] + dp[a][b-1] + dp[a-1][b] - dp[a-1][b-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

