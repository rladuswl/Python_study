## 백준 1449 수리공 항승
# 그리디, 정렬

'''방법1
import sys
input = sys.stdin.readline

n, l = map(int, input().split())  # 물이 새는 곳 개수 n과 테이프 길이 l

position = list(map(int, input().split()))

position.sort()

cnt = 0  # 테이프 개수
start = position[0]
end = start + l
cnt += 1  # 첫 번째 테이프

for i in range(n):
    if start <= position[i] < end:
        continue
    else:
        cnt += 1
        start = position[i]
        end = start + l

print(cnt)
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())  # 물이 새는 곳 개수 n과 테이프 길이 l

position = list(map(int, input().split()))

position.sort()

start = 0
cnt = 0

for loc in position:
    if start < loc:
        # start에 테이프 붙이기
        # start + (l-1) 까지는 테이프 붙여짐
        start = loc + (l-1)
        cnt += 1

print(cnt)