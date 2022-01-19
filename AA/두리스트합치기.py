import sys
sys.stdin = open("input.txt", "rt")

## 두 리스트 합치기
totlist = []
for i in range(2):
    n = int(input())
    list1 = list(map(int, input().split()))
    for i in list1:
        totlist.append(i)

totlist.sort()
for i in totlist:
    print(i, end=' ')

