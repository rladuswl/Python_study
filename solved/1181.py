# 백준 1181 단어정렬
import sys

n = int(input())

lst = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    lst.append(s)

lst_set = set(lst)
lst = list(lst_set)

lst.sort()
lst.sort(key = len)

for x in lst:
    print(x)