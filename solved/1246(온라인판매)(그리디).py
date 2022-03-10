## 백준 1246 온라인 판매
# 그리디, 정렬

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n은 총 달걀 개수, m은 잠재적인 고객

p_list = []
for _ in range(m):
    p = int(input())  # 각 고객이 달걀 하나를 살 수 있는 최대 가격
    p_list.append(p)

p_list.sort()

a = 0  # 달걀을 책정한 가격 (최소)
max_total = -2147000000  # 최대 수익

for i in range(m):
    total = 0
    if m-i <= n:
        total = (m-i)*p_list[i]
    else:
        total = n*p_list[i]

    if total > max_total:
        a = p_list[i]
        max_total = total

print(a, max_total)
