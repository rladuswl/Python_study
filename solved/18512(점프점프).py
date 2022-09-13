import sys
input = sys.stdin.readline

x, y, p1, p2 = map(int, input().split())

run_x = set(range(p1, 10**6, x))
run_y = set(range(p2, 10**6, y))

r = run_x & run_y
print(min(r) if r else -1)

