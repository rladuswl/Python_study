# 백준 2775 부녀회장이 될테야
# 수학, 구현

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호
    f = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            f[j] += f[j-1]
    print(f[-1])
