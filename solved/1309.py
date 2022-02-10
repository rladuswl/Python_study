# 1309 동물원
# 다이나믹 프로그래밍 (보텀업)
# 해설참고

import sys
input = sys.stdin.readline
n = int(input())

# 경우의 수 저장
d = [0] * (n+1)

for i in range(n+1):
    d[i] = [0, 0, 0]

d[1][0] = 1
d[1][1] = 1
d[1][2] = 1

# d[i][0] = 사자 없을 때, d[i][1] = 사자 왼쪽, d[i][2] = 사자 오른쪽
for i in range(2, n+1):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % 9901
    d[i][1] = (d[i-1][0] + d[i-1][2]) % 9901
    d[i][2] = (d[i-1][0] + d[i-1][1]) % 9901

print(sum(d[n])%9901)