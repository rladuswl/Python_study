import sys

sys.stdin = open("input.txt", "rt")

# 못풀음
# 내 답 틀림

## 뮤직비디오 (결정알고리즘)
'''내 답안'''
n, m = map(int, input().split())
li = list(map(int, input().split()))


def Count(capa):
    s = 0
    cnt = 0
    for i in range(n):
        s += li[i]
        if s > capa:
            cnt += 1
            s = li[i]

    print(cnt)
    return cnt


res = 0  # DVD 용량 크기 범위 : 1~sum(li) = 1~45
lt = 1
rt = sum(li)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m:
        rt = mid - 1
        res = mid
    elif Count(mid) < m:
        rt = mid - 1
        res = mid
    else:
        lt = mid + 1

print(res)

'''모범답안

def Count(capacity):
    sum = 0
    cnt = 1
    for x in Music:
        if sum+x > capacity:  # x도 저장할 수 있는지 확인
            cnt += 1
            sum = x
        else:
            sum += x
    print(cnt)

    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)

lt = 1
rt = sum(Music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
'''
