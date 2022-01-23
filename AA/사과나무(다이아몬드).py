import sys
#sys.stdin = open("input.txt", "rt")

# 틀렸어!!!!!!!! ㅠㅠ

## 사과나무 (다이아몬드)
'''내 답안 -------------- 틀림
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
sum = 0

for i in range(0, n):
    if i in range(0, n//2+1):
        for j in range(n//2-i, i+3, 1):
            sum+=apple[i][j]
    else:
        for k in range(i-n//2, n-i+2, 1):
            sum+=apple[i][k]

print(sum)
'''

'''모범답안
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
'''

