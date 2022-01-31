import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")

# 못 풀음
# deque

## 침몰하는 타이타닉 (그리디)
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)  # p를 deque라는 자료구조로 만들기
cnt = 0

while p:  # 비어있으면 False
    if len(p) == 1:
        cnt += 1
        break

    if p[0] + p[-1] > limit:  # 리스트의 마지막 자료는 [-1]
        p.pop()
        cnt += 1
    else:
        p.popleft()  # deque에서 사용 가능
        p.pop()
        cnt += 1

print(cnt)