import sys
input = sys.stdin.readline

n, m = map(int, input().split())

card = list(map(int, input().split()))

from itertools import combinations

result = []
for combi in combinations(card, 3):
    if sum(combi) == m:
        print(m)
        break
    elif sum(combi) < m:
        result.append(sum(combi))

else:
    print(max(result))