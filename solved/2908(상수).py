import sys
input = sys.stdin.readline

a, b = map(str, input().split())

aa = ''
bb = ''
for i in range(3, 0, -1):
    aa += a[i-1]
    bb += b[i-1]

print(max(aa, bb))