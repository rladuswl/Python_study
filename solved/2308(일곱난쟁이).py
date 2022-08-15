import sys
input = sys.stdin.readline
from itertools import combinations

h = []
result = []
for _ in range(9):
    h.append(int(input()))

for combi in combinations(h, 7):
    if sum(combi) == 100:
        result = list(combi)

result.sort()
for x in result:
    print(x)
