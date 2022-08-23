import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    a = set()
    for _ in range(n):
        a.add(int(input()))

    b = set()
    for _ in range(m):
        b.add(int(input()))

    print(len(a & b))
