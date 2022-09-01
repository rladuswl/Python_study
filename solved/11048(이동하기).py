'''정답이지만 다시 풀어보기
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]  # dp 테이블 만들기

for i in range(n):
    for j in range(m):
        if i:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

        dp[i][j] += lst[i][j]

print(dp[n-1][m-1])
'''