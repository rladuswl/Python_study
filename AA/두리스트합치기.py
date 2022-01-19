import sys
sys.stdin = open("input.txt", "rt")

# 모범답안이 더 효율적

## 두 리스트 합치기
'''내 답안
totlist = []
for i in range(2):
    n = int(input())
    list1 = list(map(int, input().split()))
    for i in list1:
        totlist.append(i)

totlist.sort()
for i in totlist:
    print(i, end=' ')
'''

'''모범답안'''
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = []
p1 = p2 = 0

while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1<n:
    c = c + a[p1:]  # append로 합치면 리스트 안의 리스트가 됨
if p2<m:
    c = c + b[p2:]

for i in c:
    print(i, end=' ')


