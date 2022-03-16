## 백준 1931 회의실 배정

# 1. 회의의 최대 개수를 구하기 위해서는 회의가 끝나는 시간을 기준으로 오름차순 정렬되어 있어야 한다.
# 2. lst에 회의 정보 저장
# 3. for문으로 인덱스 0부터 돌기


import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, e))

lst.sort(key = lambda x : (x[1], x[0]))  # 끝나는 시간을 우선으로 정렬하고, 시작하는 시간으로도 오름차순 정렬을 해야한다. (끝나는 시간이 같을 경우, 시작 시간이 더 빠른 것부터 해야하므로)

et = 0  # 마지막 회의 끝난 시간 저장
cnt = 0
for s, e in lst:
    if s >= et:
        et = e
        cnt += 1

print(cnt)