import sys
input = sys.stdin.readline

n = int(input())

s = 0
for i in range(1, n+1):
    lst = list(map(int, str(i)))
    s = sum(lst)
    if i+s == n:
        print(i)
        break
else:
    print(0)