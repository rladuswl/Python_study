import sys
sys.stdin = open("input.txt", "rt")

# 해설 듣고 품

## 마구간 정하기 (결정알고리즘)
'''내 답안
def Count(length):
    cnt = 1
    p = 0
    for i in range(1, n):
        if li[i] - li[p] >= length:
            cnt += 1
            p = i
    return cnt


n, c = map(int, input().split())
li = []
res = 0
for _ in range(n):
    li.append(int(input()))
li.sort()

lt = 1
rt = max(li)
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
'''

'''모범답안'''
def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        if Line[i]-ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid)>=c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
