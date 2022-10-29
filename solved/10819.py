n = int(input())
a = list(map(int, input().split()))

from itertools import permutations

p = permutations(a)

m = 0
for i in p:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-(i[j+1]))
    if s > m:
        m = s
print(m)
