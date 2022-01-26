import sys
#sys.stdin = open("input.txt", "rt")

# 아예 못 풀음
# 결정 알고리즘 익히기
# 결정 알고리즘 - 답이 특정 범위 안에 있음을 예측할 수 있음.
# 범위에서 이분탐색 이용하기

## 랜선자르기 (결정알고리즘)
'''모범답안'''
def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

k, n = map(int, input().split())
Line = []
res = 0
largest = 0
for _ in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2  # mid는 계속 바뀌어야 하기 때문에 while문 안에 있어야함
    if Count(mid) >= n:  # 참이면 mid는 답이 될 수 있음
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)