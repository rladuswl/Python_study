# https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6
# 다이나믹 프로그래밍
# 못 풀음
n = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위핸 dp 테이블
# 문제에 주어진 n의 범위 : 3 <= n <= 100
dp = [0] * 100

# 다이나믹 프로그래밍 (보텀업)
dp[0] = array[0]
dp[1] = max(array[0], array[1])
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])
print(dp)
print(dp[n-1])



