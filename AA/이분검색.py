import sys
sys.stdin = open("input.txt", "rt")

# 이분검색 방법 모름
# 해설 보고 이분검색 방법 익히기

## 이분검색
'''내 답안
n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
for i in range(n):
    if li[i] == m:
        print(i+1)
'''
'''모범답안'''
# left -> lt와 right -> rt 필요
# mid 라는 중간 지점 변수 만들기
# mid = (lt + rt)//2
# log(n)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1

