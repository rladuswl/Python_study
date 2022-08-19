import sys
input = sys.stdin.readline

lst = []
for _ in range(10):
    lst.append(int(input()))

s = 0
m = 2147000000
result = []
for x in lst:
    s += x
    if abs(100-s) <= m:
        m = abs(100-s)
        result.append(s)

print(max(result))