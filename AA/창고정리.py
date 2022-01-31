import sys
sys.stdin = open("input.txt", "rt")

## 창고정리
'''내 답안
l = int(input())
box = list(map(int, input().split()))
m = int(input())

for i in range(m):
    box.sort(reverse=True)
    box[0] -= 1
    box[l-1] += 1

print(max(box)-min(box))
'''

'''모범답안'''
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()
print(a[L-1]-a[0])