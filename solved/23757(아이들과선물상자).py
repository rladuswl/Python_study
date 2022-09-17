import sys
input = sys.stdin.readline

# 선물이 가장 많이 담겨있는 상자에서 각자 원하는 만큼 선물을 가져간다.
# 우선순위 높은 값을 조회해주는 최대힙 사용 -> 파이썬은 최소힙이 기본, 최대힙은 음수로 구현

import heapq as h

n, m = map(int, input().split())

max_heap = []
for c in map(int, input().split()):
    h.heappush(max_heap, -c)

for w in map(int, input().split()):
    max_gift = -h.heappop(max_heap)

    if max_gift < w:
        print(0)
        break
    else:
        h.heappush(max_heap, -(max_gift - w))
else:
    print(1)