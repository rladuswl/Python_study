import sys
sys.stdin = open("input.txt", "rt")

# 해설 보고 품
# 이해 잘 안됨 어려움

# 수들의 합
'''내 답안 -> 시간초과
n, m = map(int, input().split())
list1 = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        sum = 0
        for k in range(i, j+1):
            sum += list1[k]
        if sum == m:
            cnt += 1
            break
print(cnt)
'''

'''모범답안
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)
'''